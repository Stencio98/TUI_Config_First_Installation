#!/bin/bash

#variables to make visible the error line
bold='\e[1m'
err='\a\033[7m ERROR:'
reset='\033[0m'

echo -e "${bold}Welcome to Fedora Script Installation\nFirst of all we need to update dnf packages...${reset}"
sleep 2

# First, clean the dnf cache
dnf clean all
if [ "$?" -ne 0 ]; then
	echo -e "${err} dnf clean all ${reset}"
	exit 1
fi

# Then, update the system
dnf update -y
if [ "$?" -ne 0 ]; then
	echo -e "${err} dnf update ${reset}"
	exit 1
fi

# Upgrade with refresh
dnf upgrade --refresh -y
if [ "$?" -ne 0 ]; then
	echo -e "${err} dnf upgrade --refresh ${reset}"
	exit 1
fi

# Remove unnecessary dependencies
dnf autoremove -y
if [ "$?" -ne 0 ]; then
	echo -e "${err} dnf autoremove ${reset}"
	exit 1
fi
echo -e "${bold} \ndnf: System updated and cleaned successfully. ${reset}"

echo "\nDo you want to continue installation? y/n"
read -n1 INPUT
if [ "$INPUT" = "y" || "$INPUT" = "Y" ]; then
	echo "\nDo you want to install dnf packages? y/n"
	read -n1 INPUT
	if [ "$INPUT" = "y" || "$INPUT" = "Y" ]; then
		echo "\n"
		#apre script dnf
	fi	


fi




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
