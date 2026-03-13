# Most Common Git commands


## Repository Setup

* `git init` - Initialize a new Git repository.
* `git clone <repo_url>` - Copy an existing repository to your machine.

Example:

```bash
git clone https://github.com/user/repo.git
```
---

## Checking Repository Status

* `git status` - To see the current state of the repository, including modified, staged, and untracked files

* `git log`  
and   
`git log --oneline` - To see commit history

---

## Adding and Committing Changes

* `git add <file>` - Stage a file.
* `git add .` - Stage all files in current directory and subdirectories
 but execution location matters
* `git add --all` - To stage all changes in the entire repository (entire 
working tree and execution location is irrelevant)
* `git commit -m "message"` - Commit staged changes.

Example:

```bash
git add .
git commit -m "Fix bug xyz"
```

---


## Remote Repositories

* `git remote -v` - Show remote repositories.
* `git push origin <branch>` - Push code to remote.
* `git pull` - Fetch + merge remote changes.
* `git fetch` - Download remote changes without merging.

Example:

```bash
git push origin main
git pull origin main
```

---

## Working with Branches

* `git branch` - List branches.
* `git branch <branch_name>` - Create a new branch.
* `git switch <branch_name>` - Switch branch.

---

## Stashing Work

* `git stash` - Save uncommitted changes temporarily.
* `git stash pop` - Restore stashed changes.

Example:

```bash
git stash
git stash pop
```
---
