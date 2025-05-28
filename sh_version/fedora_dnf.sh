#!/bin/bash

#variables to make visible the error line
bold='\e[1m'
err='\a\033[7m ERROR:'
reset='\033[0m'


echo -e "${bold}Welcome to Fedora Script Installation dnf packages${reset}"
sleep 2


dnf install -y fastfetch;
if [ "$?" -ne 0 ]; then
	echo -e "${err} fastfetch (dnf) ${reset}\nSkip.."
fi


dnf install -y gedit;
if [ "$?" -ne 0 ]; then
	echo -e "${err} gedit (dnf) ${reset}\nSkip.."
fi


dnf install -y tree;
if [ "$?" -ne 0 ]; then
	echo -e "${err} tree (dnf) ${reset}\nSkip.."
fi
