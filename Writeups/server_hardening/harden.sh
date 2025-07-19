#!/bin/bash

echo "[*] Updating system..."
sudo apt update && sudo apt upgrade -y

echo "[*] Enabling UFW Firewall..."
sudo ufw allow ssh
sudo ufw enable

echo "[*] Disabling root login over SSH..."
sudo sed -i 's/^#PermitRootLogin.*/PermitRootLogin no/' /etc/ssh/sshd_config
sudo systemctl restart sshd

echo "[*] Kernel hardening parameters applied (mock)..."
# In real use, you'd add kernel tweaks here

echo "[*] System hardened successfully!"
