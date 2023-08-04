#!/bin/bash

# *****************************COPYRIGHT*******************************
# (C) Crown copyright Met Office. All rights reserved.
# For further details please refer to the file COPYRIGHT.txt
# which you should have received as part of this distribution.
# *****************************COPYRIGHT*******************************

#set -eu

github_url="https://github.com/MetOffice/simulation-systems.git"


echo "Git-scripts updater has started running"

rm -rf "${CYLC_SUITE_SHARE_DIR}/imported_github_scripts"
if [[ $? != 0 ]]; then
    echo "Couldn't remove specified folder. Try checking permissions"
    exit 1
  else
    echo "Successfully removed old simulation-systems git directory"
fi

git clone -b Lucy_testing_um_scripts --single-branch $github_url "${CYLC_SUITE_SHARE_DIR}/imported_github_scripts" 2>&1
if [[ $? != 0 ]]; then
    echo "Unable to clone remote git repo into specified location. Check git branch, git url, destination path, permissions and git access"
    exit 1
  else
    echo "Git repo successfully cloned"
fi

echo "Github scripts updated"
