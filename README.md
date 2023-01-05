# DeepLearning

This repo stores all projects worked on during my independent study for spring of 2023.

# Bash commands:

touch file.name: creates a file.

cat file.name: opens a file.

# Git commands:

git log: goes over all commits, pressing q is how to exit

git init: initializes repo

git status: status of repo, shows un added/commited changes.

git add file.name: adds the file to staging area, file is ready to be commited. This means commit's messages are attached to only the things that are currently being staged. ($ git add . puts everything in staging)

git commmit -m "Message": commits all things in staging area with message attached. 

git push: Pushes all commits to the repo

git restore --staged file.name: removes file from staging.

git branch branch-name: creates a new branch, basically letting you clone the repo and do seperate stuff. 

git checkout branch-name: switch to branch-name

git checkout -b branch-name: goes to and makes a new branch

git merge branch-name: merges targeted branch with the current branch

# General tips that I have learned:

When in doubt, git status. The status will tell you what you should do next to make a commit. 