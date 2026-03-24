# Git VCS
---

**Git** is 
- a *distributed version control system (DVCS)* 
- every developer has a full copy of the repository and its history locally.

 **GitHub** is 
 - a *remote hosting platform* (cloud-based service) where we can 
 store Git repositories and collaborate with others.

 **Bitbucket** and **GitLab** are also remote hosting platforms like **GitHub** 
 that work with Git

---

## VCS - Version Control System
- a tool for tracking changes and collaborating on code
- allows us to take snapshots of a project
- a tool that tracks, manages, and records changes to code and files over time, allowing multiple people to collaborate, compare, and revert to previous 
versions

---


## Repository (Repo)
- a set of files in a program that Git is actively tracking
- A Git repository (or "repo") is a storage space that contains all the files 
for a project, along with their complete history of changes
- It is the central element in Git that enables version control, allowing 
developers to track modifications, revert to previous versions, and collaborate efficiently

### Types of Repositories
There are two primary types of Git repositories
- **Local Repository** - Stored on an individual developer's computer.
- **Remote Repository** - a version of our project that is hosted 
    on the Internet or 
    a local network, 
    rather than on our local machine

---

## Staging Area (Index) 
- An area where we prepare changes before committing them. 
- Using the git add command moves changes to the staging area.

---

## Working Directory
- The local directory on our computer where we edit files. 
- These changes are tracked by Git but not yet staged or committed.

---

## Commit 
- A snapshot of our project at a specific point in time. 
- Each commit has 
    1. a unique ID (SHA-1 hash), 
    1. a message describing the changes, and 
    1. author information

---

## Branch 
- An independent line of development within a repository. 
- It allows developers to work on new features or bug fixes in isolation from 
the main codebase

---

## Remote
- a link to another copy of our project that lives outside our local computer
- a remote is a reference (a named connection) to a repository that is hosted somewhere else—usually on the internet or a network.

- Remotes are used to
    * Push our changes --> send our code to the remote repo
    * Pull changes  --> bring updates from the remote repo to our local repo
    * Fetch --> download updates without merging

---

## Origin

- When we clone a repo from GitHub (or GitLab or Bitbucket), 
Git automatically creates a remote called: `origin`

This origin points to the online repository we cloned from.

---
