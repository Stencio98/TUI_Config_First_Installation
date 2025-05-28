#!/bin/bash
echo "Welcome to Fedora Script Installation"
echo "First of all we need to update dnf packages..."
sleep 1

# First, clean the dnf cache
if ! dnf clean all; then
    echo "ERROR: dnf clean all"
    exit 1
fi

# Then, update the system
if ! dnf update -y; then
    echo "ERROR: dnf update"
    exit 1
fi

# Upgrade with refresh
if ! dnf upgrade --refresh -y; then
    echo "ERROR: dnf upgrade --refresh"
    exit 1
fi

# Remove unnecessary dependencies
if ! dnf autoremove -y; then
    echo "ERROR: dnf autoremove"
    exit 1
fi

echo -e "\e[1mdnf: System updated and cleaned successfully.\e[0m"

echo "Do you want to continue installation? y/n"
read -n1 keyboard_IN






##install dnf programs
#dnf install -y fastfetch &&

## make sure flatpak exist
#dnf install -y flatpak && flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo &&

##update flatpak packages
#sudo flatpak update -y &&
##install flatpak programs
##flatpak install -y flathub org.kde.kate &&
#flatpak install -y flathub com.discordapp.Discord &&
#flatpak install -y flathub org.chromium.Chromium &&
#flatpak install -y flathub com.jetbrains.IntelliJ-IDEA-Community &&
#flatpak install -y flathub com.google.AndroidStudio &&
#flatpak install -y flathub com.visualstudio.code &&
#flatpak install -y flathub com.github.IsmaelMartinez.teams_for_linux &&
#flatpak install -y flathub com.spotify.Client &&
#flatpak install -y flathub com.valvesoftware.Steam &&
#flatpak install -y flathub org.telegram.desktop &&
#flatpak install -y flathub com.play0ad.zeroad &&


## all good
#echo "installation finished"
