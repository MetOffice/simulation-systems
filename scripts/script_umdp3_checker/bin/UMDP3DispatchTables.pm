# *****************************COPYRIGHT*******************************
# (C) Crown copyright Met Office. All rights reserved.
# For further details please refer to the file COPYRIGHT.txt
# which you should have received as part of this distribution.
# *****************************COPYRIGHT*******************************

# Standalone version of the dispatch tables from UDMP3Job

package UMDP3DispatchTables;
use strict;
use warnings;
use 5.010;

# Declare version - this is the last UM version this script was updated for:
our $VERSION = '13.2.0';

my %dispatch_table_diff_fortran = (
  'Lowercase Fortran keywords not permitted' => \&UMDP3::capitalised_keywords,
  'OpenMP sentinels not in column one' => \&UMDP3::openmp_sentinels_in_column_one,
  'Omitted optional space in keywords' => \&UMDP3::unseparated_keywords,
  'GO TO other than 9999' => \&UMDP3::go_to_other_than_9999,
  'WRITE without format' => \&UMDP3::write_using_default_format,
  'Lowercase or CamelCase variable names only' => \&UMDP3::lowercase_variable_names,
  'Use of dimension attribute' => \&UMDP3::dimension_forbidden,
  'Continuation lines shouldn\'t start with &' => \&UMDP3::ampersand_continuation,
  'Use of EQUIVALENCE or PAUSE' => \&UMDP3::forbidden_keywords,
  'Use of older form of relational operator (.GT. etc.)' => \&UMDP3::forbidden_operators,
  'Line longer than 80 characters' => \&UMDP3::line_over_80chars,
  'Line includes tab character' => \&UMDP3::tab_detection,
  'USEd printstatus_mod instead of umPrintMgr' => \&UMDP3::printstatus_mod,
  'Used PRINT rather than umMessage and umPrint' => \&UMDP3::printstar,
  'Used WRITE(6) rather than umMessage and umPrint' => \&UMDP3::write6,
  'Used um_fort_flush rather than umPrintFlush' => \&UMDP3::um_fort_flush,
  'Used Subversion keyword substitution which is prohibited' => \&UMDP3::svn_keyword_subst,
  'Used !OMP instead of !$OMP' => \&UMDP3::omp_missing_dollar,
  'Used #ifdef or #ifndef rather than #if defined() or #if !defined()' => \&UMDP3::cpp_ifdef,
  'Presence of fortran comment in CPP directive' => \&UMDP3::cpp_comment,
  'Used an archaic fortran intrinsic function' => \&UMDP3::obsolescent_fortran_intrinsic,
  'EXIT statements should be labelled' => \&UMDP3::exit_stmt_label,
  'Intrinsic modules must be USEd with an INTRINSIC keyword specifier' => \&UMDP3::intrinsic_modules,
  'READ statements should have an explicit UNIT= as their first argument' => \&UMDP3::read_unit_args,
                      );

my %dispatch_table_file_fortran = (
  'Warning - used an if-def due for retirement' => \&UMDP3::retire_if_def,
  'File is missing at least one IMPLICIT NONE' => \&UMDP3::implicit_none,
  'Never use STOP or CALL abort' => \&UMDP3::forbidden_stop,
  'Use of Fortran function as a variable name' => \&UMDP3::intrinsic_as_variable,
  'File missing crown copyright statement or agreement reference' => \&UMDP3::check_crown_copyright,
  'File missing correct code owner comment' => \&UMDP3::check_code_owner,
  'Used (/ 1,2,3 /) form of array initialisation, rather than [1,2,3] form' => \&UMDP3::array_init_form,
                      );

my %dispatch_table_diff_c = (
  'Line longer than 80 characters' => \&UMDP3::line_over_80chars,
  'Line includes tab character' => \&UMDP3::tab_detection,
  'Fixed-width Integer format specifiers must have a space between themselves and the string delimiter (the " character)' => \&UMDP3::c_integral_format_specifiers,
                      );

my %dispatch_table_file_c = (
  'Warning - used an if-def due for retirement' => \&UMDP3::retire_if_def,
  'Used a deprecated C identifier' => \&UMDP3::c_deprecated,
  'File missing crown copyright statement or agreement reference' => \&UMDP3::check_crown_copyright,
  'File missing correct code owner comment' => \&UMDP3::check_code_owner,
  'Used an _OPENMP if-def without also testing against SHUM_USE_C_OPENMP_VIA_THREAD_UTILS. (Or _OPENMP does not come first in the test.)' => \&UMDP3::c_openmp_define_pair_thread_utils,
  'Used an _OPENMP && SHUM_USE_C_OPENMP_VIA_THREAD_UTILS if-def test in a logical combination with a third macro' => \&UMDP3::c_openmp_define_no_combine,
  'Used !defined(_OPENMP) rather than defined(_OPENMP) with #else branch' => \&UMDP3::c_openmp_define_not,
  'Used an omp #pragma (or #include <omp.h>) without protecting it with an _OPENMP if-def' => \&UMDP3::c_protect_omp_pragma,
  'Used the #ifdef style of if-def, rather than the #if defined() style' => \&UMDP3::c_ifdef_defines,
  'C Unit does not end with a final newline character' => \&UMDP3::c_final_newline,
                      );

my %dispatch_table_file_all = (
  'Line includes trailing whitespace character(s)' => \&UMDP3::line_trail_whitespace,
                      );

sub get_diff_dispatch_table_fortran {
  return %dispatch_table_diff_fortran;
}

sub get_file_dispatch_table_fortran {
  my $modified_file = shift;
  my %dispatch_table_file_fortran_custom = %dispatch_table_file_fortran;

  if ($modified_file =~/um_abort_mod.F90$/) {
    delete($dispatch_table_file_fortran_custom{'Never use STOP or CALL abort'});
  }

  return %dispatch_table_file_fortran_custom;
}

sub get_diff_dispatch_table_c {
  return %dispatch_table_diff_c;
}

sub get_file_dispatch_table_c {
  return %dispatch_table_file_c;
}

sub get_file_dispatch_table_all {
  return %dispatch_table_file_all;
}

1;
