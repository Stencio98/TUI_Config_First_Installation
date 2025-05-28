#!/bin/bash

#variables to make visible the error line
bold='\e[1m'
err='\a\033[7m ERROR:'
reset='\033[0m'

echo -e "${bold}Welcome to Fedora Script Installation flatpak packages${reset}"
sleep 2


dnf install -y flatpak 
if [ "$?" -ne 0 ]; then
	echo -e "${err} flatpak (dnf) installation${reset}"
	exit 1 
fi


flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo
if [ "$?" -ne 0 ]; then
	echo -e "${err} flatpak remote-add (dnf) flathub${reset}"
	exit 1
fi

install_flatpak_app() {
    app=$1
    flatpak install -y flathub "$app"
    if [ "$?" -ne 0 ]; then
        echo -e "${err} failed to install $app${reset}"
    fi
}

install_flatpak_app com.discordapp.Discord
install_flatpak_app org.chromium.Chromium
install_flatpak_app com.jetbrains.IntelliJ-IDEA-Community
install_flatpak_app com.google.AndroidStudio
install_flatpak_app com.visualstudio.code
install_flatpak_app com.github.IsmaelMartinez.teams_for_linux
install_flatpak_app com.spotify.Client
install_flatpak_app com.valvesoftware.Steam
install_flatpak_app org.telegram.desktop
install_flatpak_app com.play0ad.zeroad
install_flatpak_app org.kde.kate

echo -e "${bold}Flatpak installation script completed.${reset}"

