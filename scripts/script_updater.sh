#!/bin/bash

github_url="https://github.com/MetOffice/simulation-systems.git"


echo "updater script has started running"

rm -rf $HOME/Documents/um_scripts_git/pulled_repo_container

git clone -b Lucy_testing_um_scripts --single-branch $github_url $HOME/Documents/um_scripts_git/pulled_repo_container


