---
tags:
  - software
---

tags:
  - software

Do git bash here.

git status

git add . (adds all)

git status

git commit -m ""

git push

## Notes

https://www.youtube.com/watch?v=xnR0dlOqNVE

[Git Fork vs. Git Clone](https://www.youtube.com/watch?v=6YQxkxw8nhE)

[[How to do git commit messages properly]]

## Examples


# Git: Common Issues and Fixes

Git can be frustrating, especially when things go wrong. This guide provides practical solutions to common Git mistakes, explained in simple terms.

https://ohshitgit.com/

### how to remove something from a git history, if i forgot to add it to the gitignore, but now have

2. Remove the file from the Git index
This tells Git to stop tracking the file.

git rm --cached path/to/file
For a folder:
git rm -r --cached path/to/folder

3. Commit this change
This saves the removal from the index.

bash
Copy code
git commit -m "Stop tracking path/to/file and add to .gitignore"


## 🔄 Undoing Mistakes

### I messed up badly! Can I go back in time?

Yes! Use Git’s reflog to find a previous state:

```bash
git reflog
# Find the index of the state before things broke
git reset HEAD@{index}
```

_This is useful for recovering deleted commits, undoing bad merges, or rolling back to a working state._

## 🚀 Commit Fixes

### I committed but forgot a small change!

```bash
# Make the change
git add .
git commit --amend --no-edit
```

⚠ Warning: Never amend a commit that has already been pushed!

### I need to change the last commit message!

```bash
git commit --amend
```

This will open an editor where you can modify the commit message.



## 🔀 Branching Issues

### I committed to `master` but wanted a new branch!

```bash
# Create a new branch from the current state
git branch new-branch
# Remove the commit from master
git reset HEAD~ --hard
git checkout new-branch
```

⚠ Warning: If you’ve already pushed the commit, additional steps are needed.

### I committed to the wrong branch!

```bash
# Undo the last commit but keep the changes
git reset HEAD~ --soft
git stash
git checkout correct-branch
git stash pop
git add .
git commit -m "Moved commit to correct branch"
```

Alternative:

```bash
git checkout correct-branch
git cherry-pick master  # Moves last commit to correct branch
git checkout master
git reset HEAD~ --hard  # Removes the commit from master
```



## 🔍 Diff and Reset

### I ran `git diff`, but it showed nothing!

If your changes are staged, use:

```bash
git diff --staged
```

This shows differences between the last commit and staged files.

### I need to undo a commit from 5 commits ago!

```bash
git log  # Find the commit hash
git revert [commit-hash]
```

This creates a new commit that undoes the changes.



## 🗑️ Undoing Changes

### I need to undo changes to a file!

```bash
git log  # Find a commit before the changes
git checkout [commit-hash] -- path/to/file
git commit -m "Reverted file to previous version"
```

### I want to reset my repo to match the remote!

⚠ _Destructive action—this cannot be undone!_

```bash
git fetch origin
git checkout master
git reset --hard origin/master
git clean -d --force  # Removes untracked files
```



## 🤯 Last Resort

If everything is completely broken, nuke the repo and reclone:

```bash
cd ..
sudo rm -r repo-folder
git clone https://github.com/user/repo.git
cd repo-folder
```

