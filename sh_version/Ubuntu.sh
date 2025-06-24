#!/bin/bash
#sudo bash Ubuntu.sh
bold='\e[1m'
err='\a\033[7m ERROR:'
reset='\033[0m'

printf "%b Welcome to Ubuntu Script Installation %b\n" "\$bold" "\$reset"
printf "%b Press [ENTER] to continue... %b" "\$bold" "\$reset"
read

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
exec_command apt install -y snapd

echo -e "${bold} Updating Snap packages ${reset}"
exec_command snap refresh

echo -e "\n${bold} APT & Snap are updated.\nDo you want to continue and install additional programs? [y/n] ${reset}"
read -n1 -s INPUT

if [[ "$INPUT" = "y" || "$INPUT" = "Y" ]]; then
    echo -e "${bold} Installing Snap and APT packages.. ${reset}"

    exec_command snap install code --classic
    exec_command snap install discord
    exec_command snap install chromium
    exec_command snap install intellij-idea-community --classic
    exec_command snap install android-studio --classic
    exec_command snap install telegram-desktop
    exec_command snap install spotify
    exec_command snap install steam
    exec_command snap install 0ad

    # Installazioni via APT
    exec_command apt install gedit
    exec_command apt install gedit-plugins
    exec_command apt install psensor
fi

echo -e "${bold} Installation complete. Consider rebooting your system. ${reset}"
echo -e "${bold} Have a nice Linux experience!! ${reset}"

