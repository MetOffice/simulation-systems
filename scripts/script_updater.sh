#!/bin/bash

#set -eu

github_url="https://github.com/MetOffice/simulation-systems.git"


echo "Git-scripts updater has started running"

rm -rf "${HOME}/Documents/um_scripts_git/pulled_repo_container"
if [[ $? != 0 ]]; then
    echo "Couldn't remove specified folder. Try checking permissions"
    exit 1
  else
    echo "Successfully removed old simulation-systems git directory"
fi

git clone -b Lucy_testing_um_scripts --single-branch $github_url "${HOME}/Documents/um_scripts_git/pulled_repo_container"
if [[ $? != 0 ]]; then
    echo "Unable to clone remote git repo into specified location. Check git branch, git url, destination path, permissions and git access"
    exit 1
  else
    echo "Git repo successfully cloned"
fi

echo "Github scripts updated"
