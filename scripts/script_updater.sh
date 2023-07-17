#!/bin/bash

github_url="https://github.com/MetOffice/simulation-systems.git"


# pulled_repo="simulation-systems"

# tmp_dir=$(mktemp -d)

echo "updater script has started running"

rm -rf $HOME/Documents/um_scripts_git/pulled_repo_container

git clone -b Lucy_testing_um_scripts --single-branch $github_url $HOME/Documents/um_scripts_git/pulled_repo_container

# git clone $github_url $HOME/Documents/um_scripts_git/pulled_repo_container--branch UMDIR-Scripts --single-branch

# git clone $github_url $tmp_dir

# mv $tmp_dir/$pulled_repo $HOME/Documents/um_scripts_git/pulled_repo_container

#echo "updater script finished running"

#chmod +x $HOME/Documents/um_scripts_git/test.sh

#chmod +x $HOME/Documents/um_scripts_git/pulled_repo_container/scripts/script_umdp3_checker/bin/umdp3_check.pl

#./test.sh

#./pulled_repo_container/scripts/script_umdp3_checker/bin/umdp3_check.pl

# rm -rf $tmp_dir


