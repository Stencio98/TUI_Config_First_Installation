#!/usr/bin/env bash
##!/bin/sh

# Variables to make visible the error line
bold='\e[1m'
err='\a\033[7m ERROR:'
reset='\033[0m'

echo "${bold}Welcome to Linux Mint Script Installation${reset}\n"
echo "${bold}Press [ENTER] to continue...${reset}\n"
read INPUT

exec_command () {
    sudo "$@"
    if [ "$?" -ne 0 ]; then
        printf "${err} $@ ${reset}\n"
        printf "\n${bold}Do you want to CONTINUE installation now? [y/n]${reset}\n"
        read INPUT
        if  [ "$INPUT" = "y" ]; then
        	echo
        elif  [ "$INPUT" = "Y" ]; then
 			echo
        else
        	exit 0	
        fi
        	printf "${bold}Skipping command: $@${reset}\n\n"
        	sleep 1
        
    fi
}

# Update apt packages
printf "${bold}Updating apt packages...${reset}\n"
exec_command apt-get cleanf
exec_command apt-get update -y
exec_command apt-get dist-upgrade -y
exec_command apt-get autoremove -y

printf "${bold}System updated and cleaned successfully.${reset}\n"

# Prepare Flatpak
printf "${bold}Prepare Flatpak...${reset}\n"
exec_command apt-get install -y flatpak
exec_command flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

# Update Flatpak packages
printf "${bold}Updating Flatpak packages...${reset}\n"
exec_command flatpak update -y

# Install programs
printf "\n${bold}System updated.\nDo you want to install additional programs? [y/n]${reset}\n"
read -n1 -s INPUT

if [[ "$INPUT" = "y" || "$INPUT" = "Y" ]]; then
    printf "${bold}Installing Flatpak packages...${reset}\n"
    exec_command flatpak install -y flathub com.discordapp.Discord
    exec_command flatpak install -y flathub org.chromium.Chromium
    exec_command flatpak install -y flathub com.jetbrains.IntelliJ-IDEA-Community
    exec_command flatpak install -y flathub com.google.AndroidStudio
    exec_command flatpak install -y flathub com.github.IsmaelMartinez.teams_for_linux
    exec_command flatpak install -y flathub com.visualstudio.code
    exec_command flatpak install -y flathub com.spotify.Client
    exec_command flatpak install -y flathub com.valvesoftware.Steam
    exec_command flatpak install -y flathub org.telegram.desktop
    exec_command flatpak install -y flathub com.play0ad.zeroad
    exec_command flatpak install -y flathub me.timschneeberger.jdsp4linux
    exec_command flatpak install -y flathub org.gnome.gedit
fi

printf "${bold}Installation complete. Consider rebooting your system.${reset}\n"
printf "${bold}Have a nice Linux experience!${reset}\n"

