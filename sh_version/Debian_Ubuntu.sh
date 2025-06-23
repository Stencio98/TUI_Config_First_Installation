#!/usr/bin/env bash

bold='\e[1m'
err='\a\033[7m ERROR:'
reset='\033[0m'

echo -e "${bold} Welcome to Ubuntu Script Installation ${reset}"
echo -n -e "${bold} Press [ENTER] to continue... ${reset}"
read
sleep 2

function exec_command(){
    sudo "$@"
    if [ "$?" -ne 0 ]; then
        echo -e "${err} $@ ${reset}"
        echo -e "\n${bold} Do you want to QUIT installation now? [y/n] ${reset}"
        read -n1 -s INPUT
        if [[ "$INPUT" = "y" || "$INPUT" = "Y" ]]; then
            exit 0
        fi
        echo -e "${bold} Skipping command: $@ ${reset}"
    fi
}

echo -e "${bold} Updating APT packages ${reset}"
exec_command apt update
exec_command apt upgrade -y
exec_command apt autoremove -y
exec_command apt autoclean -y

echo -e "${bold} APT: System updated and cleaned successfully. ${reset}"

echo -e "${bold} Checking Snap installation ${reset}"
if ! command -v snap &> /dev/null; then
    echo -e "${bold} Installing snapd ${reset}"
    exec_command apt install -y snapd
else
    echo -e "${bold} Snap is already installed. ${reset}"
fi

# Aggiornamento Snap
echo -e "${bold} Updating Snap packages ${reset}"
exec_command snap refresh

# Conferma installazione extra
echo -e "\n${bold} APT & Snap are updated.\nDo you want to continue and install additional programs? [y/n] ${reset}"
read -n1 -s INPUT

if [[ "$INPUT" = "y" || "$INPUT" = "Y" ]]; then
    echo -e "${bold} Installing Snap and APT packages.. ${reset}"

    # Installazioni via Snap
    exec_command snap install code --classic
    exec_command snap install discord
    exec_command snap install chromium
    exec_command snap install intellij-idea-community --classic
    exec_command snap install android-studio --classic
    exec_command snap install telegram-desktop
    exec_command snap install spotify
    exec_command snap install steam
    exec_command snap install gedit
    exec_command snap install 0ad

    # Installazioni via APT
fi

echo -e "${bold} Installation complete. Consider rebooting your system. ${reset}"
echo -e "${bold} Have a nice Linux experience!! ${reset}"

