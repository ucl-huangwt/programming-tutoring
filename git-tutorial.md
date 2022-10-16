# Git Tutorial

## Git
Git is a software development and IT operation tool used for **source code management**. It is a free and open-source **version control system** used to handle small to very large projects efficiently. Git is used to tracking changes in the source code, enabling multiple developers to work together on **non-linear development**.

## Initializing a new Project
Assume you have my-project directory in your machine. You can place it under Git revision control as follows.
```shell
$ cd my-project
$ git init
```
Git will reply
```
Initialized empty Git repository in .git/
```
You’ve now initialized the working directory—​you may notice a new directory created, named ".git".\
Next, tell Git to take a snapshot of the contents of all files under the current directory (note the .), with `git add`
```shell
$ git add
```
This snapshot is now stored in a temporary staging area which Git calls the "index". You can permanently store the contents of the index in the repository with `git commit`
```shell
$ git commit -m "Initialize my project"
```

## Making Changes
Assume you add several source code files - index.html, index.js, main.py. You can get a brief state of the working directory and the staging area with `git status`
```shell
$ git status
On branch master
No commits yet
Untracked files:
  (use "git add <file>..." to include in what will be committed)
    index.html
	index.js
    main.py
```
The `git add` command adds a change in the working directory to the staging area. It tells Git that you want to include updates to a particular file in the next commit. \
However, `git add` doesn't really affect the repository in any significant way—changes are not actually recorded until you run `git commit`
```shell
$ git add index.html
```
You can remove index.html from the staging area by:
```shell
$ git -rm --cached index.html
```
If you want to add all changes, try:
```
$ git add .
```
```
$ git status
On branch master
No commits yet
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   index.html
	new file:   index.js
	new file:   main.py
```
The `git commit` command captures a snapshot of the project's currently staged changes. \
Committed snapshots can be thought of as “safe” versions of a project - Git will never change them unless you explicitly ask it to do so.
```shell
$ git commit -m "add source code files"
```
```
$ git status
On branch master
nothing to commit, working tree clean
```

## Viewing Project History
At any point you can view the history of your changes using
```
$ git log
```
If you also want to see complete diffs at each step, use
```
$ git log -p
```
Often the overview of the change is useful to get a feel of each step
```
$ git log --stat --summary
```

## GitHub
**GitHub** is a **Git** repository hosting service that provides a web-based **graphical interface**. Programmers can find source codes in many different languages and use the command-line interface, **Git**, to make and keep track of any changes. **GitHub** helps every team member work together on a project from any location while facilitating **collaboration**. You can also review previous versions created at an earlier point in time.

## Using Git for Collaboration
After creating a corresponding respository in GitHub, you can initialize the remote repository by
```shell
$ git remote add origin https://github.com/[GitHub username]/[remote repository name]
$ git branch -M main
$ git push -u origin main
```
The `git push` command is used to push the local repository content to a remote repository. \
After a local repository has been modified, a push is executed to share the modifications with remote team members. Pushing is the way commits are transferred from the local repository to the remote repository. \
Assume you insert an empty main function to main.py
```shell
$ git add main.py
$ git commit -m "add main function to main.py"
$ git push
```
The `git pull` command is used to fetch and merge code changes from the remote repository to the local repository.
```
$ git pull
```

## Managing Branches:
A single Git repository can maintain multiple branches of development.
```
$ git branch  # list branches in local repository
$ git branch -r  # list branches in remote repository
$ git branch -a  # list all branches
$ git branch feature-a  # create new branch named feature-a
$ git switch feature-a  # switch to the feature-a branch
```
To merge the changes made in feature-a into master, run
```
$ git merge feature-a
```
If the changes don’t conflict, you’re done. If there are conflicts, markers will be left in the problematic files showing the conflict;
```
$ git diff
```
will show this. Once you’ve edited the files to resolve the conflicts,
```
$ git commit -a
```
will commit the result of the merge.
At this point you could delete the experimental branch with
```
$ git branch -d feature-a
```

## Other Command Lines
You can explore many other commands, helping you manage your project and collabrate with other teammates.
