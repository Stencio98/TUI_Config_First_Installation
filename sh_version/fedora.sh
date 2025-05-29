#!/usr/bin/env bash
#########!/bin/bash

#variables to make visible the error line
bold='\e[1m'
err='\a\033[7m ERROR:'
reset='\033[0m'

echo -e "${bold} Welcome to Fedora Script Installation ${reset}"
echo -n -e "${bold} Press [ENTER] to continue... ${reset}"
read
sleep 2

function exec_command(){
	sudo "$@"
	#sudo "$*" --> see difference between $@ e $*
	if [ "$?" -ne 0 ]; then
		echo -e "${err} $@ ${reset}"
		echo -e "\n${bold} Do you want to QUIT installation now? [y/n] ${reset}"
		read -n1 -s INPUT
		if [[ "$INPUT" = "y" || "$INPUT" = "Y" ]]; then
			exit 0;
		fi
		echo -e "${bold} Skiping command: $@ ${reset}"
	fi
}

#update dnf packages
echo -e "${bold} Updating dnf packages ${reset}"
exec_command dnf clean all
exec_command dnf update -y
exec_command dnf upgrade --refresh -y
exec_command dnf autoremove -y

echo -e "${bold} dnf: System updated and cleaned successfully. ${reset}"

echo -e "${bold} Prepare Flatpak ${reset}"
exec_command dnf install -y flatpak
exec_command flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

echo -e "${bold} Installation Flatpak Packages ${reset}"
exec_command flatpak update
exec_command flatpak install -y flathub org.kde.kate
exec_command flatpak install -y flathub com.discordapp.Discord
exec_command flatpak install -y flathub org.chromium.Chromium
exec_command flatpak install -y flathub com.jetbrains.IntelliJ-IDEA-Community
exec_command flatpak install -y flathub com.google.AndroidStudio
exec_command flatpak install -y flathub com.visualstudio.code
exec_command flatpak install -y flathub com.github.IsmaelMartinez.teams_for_linux
exec_command flatpak install -y flathub com.spotify.Client
exec_command flatpak install -y flathub com.valvesoftware.Steam
exec_command flatpak install -y flathub org.telegram.desktop
exec_command flatpak install -y flathub com.play0ad.zeroad

echo -e "${bold} Installation complete. Consider rebooting your system. ${reset}"

