#!/usr/bin/env python3
#
# *****************************COPYRIGHT*******************************
# (C) Crown copyright Met Office. All rights reserved.
# For further details please refer to the file COPYRIGHT.txt
# which you should have received as part of this distribution.
# *****************************COPYRIGHT*******************************
'''
## NOTE ##
This module is one of several for which the Master copy is in the
UM repository. When making changes, please ensure the changes are made in the UM
repository or they will be lost during the release process when the UM copy is
copied over.

Module containing various functions used to apply UMDP3 style indentation
to Fortran source code
'''
import re
import sys
from fstring_parse import *

# Number of spaces of indent to apply per indentation level
INDENT = 2

# Patterns which match any line which indicates the following line should
# be indented by the above amount
INDENTATION_START = [
    # DO statement - possible label prefix followed by "DO"
    r"(^\s*|^\s*\w+\s*:\s*)DO(\s+|$)",
    # SELECT statement - possible label prefix followed by "SELECT CASE"
    r"(^\s*|^\s*\w+\s*:\s*)SELECT\s+(CASE|TYPE)(\s*|\()",
    # CASE statement
    r"^\s*CASE(\s*|\()",
    # CLASS IS statement
    r"^\s*CLASS\s*IS(\s*|\()",
    # IF statement - must end in "THEN" with possible label prefix
    r"^\s*(|\w+\s*:|[0-9]*)\s*IF\s*\(.*?\)\s*THEN\s*$",
    # ELSE statement - as above but allow "ELSE IF"
    r"^\s*ELSE\s*(IF|$)",
    # TYPE definition statement - must be followed by a word but can
    # contain optional arguments
    r"^\s*TYPE\s*((,\s*\w+(|\s*\(\s*\w+\s*\)\s*)\s*)*\s*::|)\s*\w+\s*$",
    # WHERE statement - only if missing assignment statement
    r"^\s*WHERE\s*\([^\(]*?\)\s*$",
    # ELSEWHERE statement
    r"^\s*ELSE\s*WHERE\s*(\(.*?\)[^\w]*$|$)",
    # (ABSTRACT) INTERFACE statement - possibly followed by label suffix
    r"^\s*(ABSTRACT\s*)?INTERFACE" \
    r"(\s+\w+\s*$|\s*$|" \
    r"\s+ASSIGNMENT\s*\(\s*=\s*\)\s*$|" \
    r"\s+OPERATOR\s*\(.*\)\s*$|" \
    r"\s+(READ|WRITE)\s*\(\s*(UN)?FORMATTED\s*\)\s*$)",
    # ENUMs
    r"^\s*ENUM\s*,\s*BIND\s*\(\s*C\s*\)\s*$",
]

# Patterns which match any line which signifies that it and subsequent
# lines should be dedented by the above amount
INDENTATION_END = [
    # END DO statement - possibly followed by label suffix
    r"^\s*([0-9]*\s*)END\s*DO(\s+\w+\s*$|\s*$)",
    # END SELECT statement - possibly followed by label suffix
    r"^\s*END\s*SELECT(\s+\w+\s*$|\s*$)",
    # CASE statement
    r"^\s*CASE(\s*|\()",
    # CLASS IS statement
    r"^\s*CLASS\s*IS(\s*|\()",
    # ELSE statement - as above, counts as beggining and end
    r"^\s*ELSE\s*(IF|$)",
    # END IF statement - possibly followed by label suffix
    r"^\s*END\s*IF(\s+\w+\s*$|\s*$)",
    # END TYPE statement
    r"^\s*END\s*TYPE(\s+\w+|)\s*$",
    # END WHERE statement
    r"^\s*END\s*WHERE\s*$",
    # ELSEWHERE statement
    r"^\s*ELSE\s*WHERE\s*(\(.*?\)[^\w]*$|$)",
    # END INTERFACE statement - possibly followed by label suffix
    r"^\s*END\s*INTERFACE" \
    r"(\s+\w+\s*$|\s*$|" \
    r"\s+ASSIGNMENT\s*\(\s*=\s*\)\s*$|" \
    r"\s+OPERATOR\s*\(.*\)\s*$|" \
    r"\s+(READ|WRITE)\s*\(\s*(UN)?FORMATTED\s*\)\s*$)",
    # END ENUM statement
    r"^\s*END\s*ENUM\s*$",
]


def get_current_indent(line):
    "Returns the white-space at the start of a given line"
    return re.search(r"^(?P<space>\s*)([^\s]|$)", line).group("space")


def indent_line(line, indentation):
    "Returns the given line adjusted by the required amount"
    indentation_str = " "*abs(indentation)
    if indentation > 0:
        return indentation_str + line
    elif indentation < 0:
        if re.search("^"+indentation_str, line):
            return re.sub(indentation_str, "", line, count=1)
        else:
            return line.lstrip()
    else:
        return line


def apply_indentation(lines, debug=False):
    "Apply the indentation rules to a list of lines"
    indentation = 0
    relative_indent = -1
    continuation = False
    str_continuation = [False, False]
    pp_continuation = False
    new_lines = []
    indent_pp_level = 0
    indent_pp_level_start = {}
    rel_indent_pp_level_start = {}
    indent_pp_level_max = {}
    rel_indent_pp_level_max = {}

    for iline, line in enumerate(lines):

        if debug:
            print("\n{0:d}: \"{1:s}\"".format(iline, line))

        # If this line is continuing a previous preprocessing line,
        # just ignore indentation
        if pp_continuation:
            new_lines.append(line)
            # If the next line is not a continuation reset the flag
            if not is_pp_continuation(line):
                if debug:
                    print("    (End of pre-processor continuation)")
                pp_continuation = False

        # Ignore line if an OMP directive
        elif (re.search(r"^\s*!\$.*", line, flags=re.IGNORECASE)):
            if debug:
                print("    (OMP comment)")
            new_lines.append(re.sub(r"^\s*!", "!", line))

        # Ignore line if an fcm DEPENDS ON comment
        elif (re.search(r"^\s*!\s*DEPENDS\s*ON\s*:",
                        line, flags=re.IGNORECASE)):
            if debug:
                print("    (DEPENDS ON comment)")
            new_lines.append(re.sub(r"^\s*!", "!", line))

        # Ignore line if a misc compiler directive
        elif (re.search(r"^\s*!(DIR|DEC|HPF|GCC|PGI|FPP|MIC)\$.*",
                        line, flags=re.IGNORECASE)):
            if debug:
                print("    (Compiler Directive comment)")
            new_lines.append(re.sub(r"^\s*!", "!", line))

        # If the entire line is a comment with the comment character
        # in the first position on the line, indent just the comment
        # text to line up with the current indentation level
        elif re.search("^!.*$", line, flags=re.IGNORECASE) and indentation > 0:
            if debug:
                print("    (Comment only line (from zero indent))")

            # Get the current indentation level of the line
            current_indent = get_current_indent(line)

            # Calculate the relative indent (how far the line must be
            # shifted by to meet the desired indentation level)
            relative_indent = indentation - len(current_indent)

            new_lines.append(indent_line(line, relative_indent))

        # If the line contains a pre-processor directive, set to
        # zero indentation.
        elif re.search(r"^\s*#\w+", line, flags=re.IGNORECASE):
            if debug:
                print("    (Pre-processor line)")
            if re.search(r"^\s*#if", line, flags=re.IGNORECASE):
                if debug:
                    print("    (Pre-processor if line)")
                indent_pp_level = indent_pp_level + 1
                indent_pp_level_start[indent_pp_level] = indentation
                rel_indent_pp_level_start[indent_pp_level] = relative_indent
                indent_pp_level_max[indent_pp_level] = 0
                rel_indent_pp_level_max[indent_pp_level] = 0
            elif re.search(r"^\s*#el(se|if)", line, flags=re.IGNORECASE):
                if debug:
                    print("    (Pre-processor else/elif line)")
                imax = max(indentation, indent_pp_level_max[indent_pp_level])
                indent_pp_level_max[indent_pp_level] = imax
                if indentation == indent_pp_level_max[indent_pp_level]:
                    rel_indent_pp_level_max[indent_pp_level] = relative_indent
                indentation = indent_pp_level_start[indent_pp_level]
                relative_indent = rel_indent_pp_level_start[indent_pp_level]
            elif re.search(r"^\s*#endif", line, flags=re.IGNORECASE):
                if debug:
                    print("    (Pre-processor endif line)")
                indent_pp_level_start.pop(indent_pp_level)
                rel_indent_pp_level_start.pop(indent_pp_level)
                imax = max(indentation, indent_pp_level_max[indent_pp_level])
                indent_pp_level_max[indent_pp_level] = imax
                if indentation == indent_pp_level_max[indent_pp_level]:
                    rel_indent_pp_level_max[indent_pp_level] = relative_indent
                indentation = indent_pp_level_max[indent_pp_level]
                relative_indent = rel_indent_pp_level_max[indent_pp_level]
                indent_pp_level_max.pop(indent_pp_level)
                rel_indent_pp_level_max.pop(indent_pp_level)
                indent_pp_level = indent_pp_level - 1
            new_lines.append(re.sub(r"^\s*#", "#", line))

        # If the line is entirely blank, don't mess with the settings
        # for continuation or the indentation value
        elif re.search(r"^\s*$", line, flags=re.IGNORECASE):
            if debug:
                print("    (Blank line)")
            new_lines.append(line)

        # If the line is only a comment not starting in the first column
        # copy the indentation of the previous line, unless that would
        # push the comment to a lower indentation level than the current
        # level (in which case re-indent it like a normal line of code)
        elif re.search(r"^\s*!.*$", line, flags=re.IGNORECASE):
            if debug:
                print("    (Comment only line)")

            # Get the current indentation level of the line
            current_indent = get_current_indent(line)
            if debug:
                print("    current indent = " + str(len(current_indent)))
                print("    required indent = " + str(indentation))
            # Check to see if the current relative indent will push this
            # line below the current level (and adjust the relative
            # indent if necessary)
            if relative_indent + len(current_indent) < indentation:
                relative_indent = indentation - len(current_indent)
            if debug:
                print("    relative_indent = " + str(relative_indent))
            new_lines.append(indent_line(line, relative_indent))

        # If this line is continuing a previous line, instead of
        # trying to calculate its indentation just apply the same
        # indentation as the previous line and move on
        elif continuation:
            new_lines.append(indent_line(line, relative_indent))
            # If the next line is not a continuation reset the flag
            if is_continuation(line, str_continuation):
                # check if still string continuation
                str_continuation = is_str_continuation(line, str_continuation)
            else:
                if debug:
                    print("    (End of continuation)")
                continuation = False
                str_continuation = [False, False]
        else:
            # Generate a simplified version of the line for use in
            # pattern matches
            simple_line = simplify_line(lines[iline:])

            if debug:
                print("??" + " "*len("{0:d}".format(iline)) +
                      "\"{0:s}\"".format(simple_line))

            # Check for ending statements first - since the indentation
            # shift for the end of a block must also be applied to the
            # line containing the block ending statement
            for pattern in INDENTATION_END:
                if re.search(pattern, simple_line, flags=re.IGNORECASE):
                    if debug:
                        print("    (End, matches {0:s})".format(pattern))
                    indentation -= INDENT

            # Get the current indentation level of the line
            current_indent = get_current_indent(line)

            # Calculate the relative indent (how far the line must be
            # shifted by to meet the desired indentation level)
            relative_indent = indentation - len(current_indent)

            # Indent the line by the required amount and save it to
            # the output array
            indented_line = indent_line(line, relative_indent)

            if debug:
                print("=>" + " "*len("{0:d}".format(iline)) +
                      "\"{0:s}\"".format(indented_line))

            new_lines.append(indented_line)

            # Now check for starting statements - these will affect
            # the indentation level of future lines (but not the
            # current line)
            for pattern in INDENTATION_START:
                if re.search(pattern, simple_line, flags=re.IGNORECASE):
                    if debug:
                        print("    (Start, matches {0:s})".format(pattern))
                    indentation += INDENT

            # Finally, detect if the following line is a continuation
            # of this one (and therefore requires no indentation)
            if is_continuation(line):
                if debug:
                    print("    (Next line continues)")
                continuation = True
                str_continuation = is_str_continuation(line)

        if debug:
            if continuation:
                print("    (continuation is live)")

            if pp_continuation:
                print("    (pre-processing continuation is live)")

        # Check for the start of new pre-processor continuation
        if is_pp_continuation(line) and not pp_continuation:
            if debug:
                print("    (Next line pre-processor continues)")
            pp_continuation = True

    # Sanity check - indentation should be back to 0 by the end,
    # if not then error

    if indent_pp_level != 0:
        print("Pre-processing branch level non-zero")
        return None

    if indentation != 0:
        print("Final indentation level non-zero ({0:d})".format(indentation))
        return None

    return new_lines


def main():
    '''Main toplevel function for testing'''
    input_file = sys.argv[1]

    with open(input_file, "r+") as file_in:
        lines_in = file_in.read().split("\n")
        new_lines = apply_indentation(lines_in, debug=len(sys.argv) > 2)
        if new_lines is not None:
            file_in.seek(0)
            file_in.write("\n".join(new_lines))
            file_in.truncate()
        else:
            sys.exit(1)


if __name__ == "__main__":
    main()
