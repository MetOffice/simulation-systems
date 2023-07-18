#!/bin/bash

set -eu

github_url="https://github.com/MetOffice/simulation-systems.git"


echo "Git-scripts updater has started running"

rm -rf "${HOME}/Documents/um_scripts_git/pulled_repo_container" || echo "unable to remove current simulation-systems git directory"

git clone -b Lucy_testing_um_scripts --single-branch $github_url "${HOME}/Documents/um_scripts_git/pulled_repo_container" || echo "Unable to clone remote git repo into specified location. Check git branch, git url, destination path, permissions and git access"

echo "Github scripts updated"
