# 🛡️ Server Hardening Script

A lightweight Python and Bash-based project to automate basic Linux server hardening.

## 🔧 Features

- Enables UFW firewall and allows SSH
- Disables root SSH login
- Applies system updates
- Basic kernel parameter placeholder

##  Structure
server-hardening/
├── harden.py
├── requirements.txt
├── README.md
└── scripts/
└── harden.sh

##  Usage

1. Open terminal in this directory.
2. Make the script executable:
   ```bash
   chmod +x scripts/harden.sh
Run the Python script:
python3 harden.py
You may need sudo permissions for some commands.

 Note
This project is designed for Debian-based Linux environments. Always review security scripts before running on production servers.
