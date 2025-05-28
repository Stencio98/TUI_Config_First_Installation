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
echo -e "${bold} dnf: System updated and cleaned successfully. ${reset}"

echo -e "\nDo you want to continue installation? y/n"
read -n1 -s INPUT
if [[ "$INPUT" = "y" || "$INPUT" = "Y" ]]; then
	echo -e "Do you want to install dnf packages? y/n"
	read -n1 -s INPUT
	if [[ "$INPUT" = "y" || "$INPUT" = "Y" ]]; then
		#open script dnf
		sh fedora_dnf.sh
	fi
	
	echo -e "\nDo you want to install flatpak packages? y/n"
	read -n1 -s INPUT
	if [[ "$INPUT" = "y" || "$INPUT" = "Y" ]]; then
		#open script flatpak
		sh fedora_flatpak.sh
	fi	
fi

echo -e "${bold}Have a nice Linux experience!!"
exit 0

