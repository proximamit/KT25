# Generate and add SSH public key to GitHub

---

# Ubuntu (Linux)

1. Open terminal and generate ssh keys
    - `ssh-keygen -t ed25519 -C "youremail@gmail.com"`
1. Start SSH agent and set the environment variables
    - `eval "$(ssh-agent -s)"`
1. Load SSH private keys into running agent
    - `ssh-add ~/.ssh/id_ed25519`
    - Verify (list the fingerprints of all SSH keys currently loaded into your local SSH agent)
    - `ssh-add -l`
1. View and copy SSH public key
    - `cat ~/.ssh/id_ed25519.pub`
    - copy the SSH public key (to paste to GitHub)
1. Add the SSH public key to GitHub
    - Open github.com in web browser and login
    - Go to settings
    - In the panel on left side, navigate to *SSH & GPG Keys*
    - On the *SSH Keys* page, click *New SSH Key*
    - Give suitable title (for easy identification)
    - Leave the key type to default value (Authentication key)
    - Paste the SSH public keys
    - Click on *Add SSH Key*
1. From the terminal, verify github access via SSH
    - ssh -T git@github.com
    - If all is well, A message like You've successfully authenticated... is displayed
