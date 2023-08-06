#!/usr/bin/env python3

import os, sys

def usage():
    print(f""" usage: {sys.argv[0]}
             update   - update system
             apply    - apply config file to system
             config   - open system config in vim
             mail     - open mail config in vim
             rollback - rollback to previous config
             bcrypt   - create a password hash for mail""")

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "update":
            os.system("nixos-rebuild --upgrade switch")
        if sys.argv[1] == "apply":
            os.system("sudo nixos-rebuild switch")
        if sys.argv[1] == "config":
            os.system("sudo vim /etc/nixos/configuration.nix")
        if sys.argv[1] == "mail":
            os.system("sudo vim /etc/nixos/mail.nix")
        if sys.argv[1] == "rollback":
            os.system("nixos-rebuild --rollback switch")
        if sys.argv[1] == "bcrypt":
            os.system("nix-shell -p mkpasswd --run 'mkpasswd -sm bcrypt'")
    else: usage()

if __name__ == "__main__": main()
