# Amend a commit

---
## To amend a commit
1. Make the required changes
1. `git add .`
1. `git commit --amend --no-edit` # To keep the same commit message
1. `git push origin <branchname> --force-with-lease`

e.g. `git push origin main --force-with-lease`
---
