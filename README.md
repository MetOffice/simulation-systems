Documentation is published by building the source from `main` and copying it to
this branch. This is done as follows:

# build documentation from main 
cd /path/to/simulation-systems/main
make clean html

# checkout the gh-pages branch in a separate worktree (allows parallel checkouts)
# and create a branch of a branch for making your changes in
git worktree add ../publish_wps
cd ../publish_wps
git checkout upstream/gh-pages
git checkout -b "<branch name>"

# copy documentation from main to this branch
cp -r ../simulation-systems/build/html .

# test the documentation
firefox index.html

# push
git commit -am "sensible message"
git push

# create a pull request from your branch to the gh-pages branch.