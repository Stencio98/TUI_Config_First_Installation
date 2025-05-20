programs = {
    "♻️ ⚪  update debian packages": "apt-get clean && apt-get update && apt-get dist-upgrade -y && apt-get full-upgrade -y && apt-get autoremove -y",
    "♻️ 🔵  update flatpak packages ": "sudo flatpak update -y",
    "♻️ 🔴  update snap packages": "sudo snap refresh",
    "⚪  gedit and gedit's plugins": "apt install -y gedit && apt install -y gedit-plugins",
    "⚪  neofetch": "apt install neofetch",
    "⚪  flatpak with flathub ⚠️": "sudo apt install -y flatpak && flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo",
    "⚪  flatpak-plugin-gnome": "sudo apt install -y gnome-software-plugin-flatpak",
    "⚪  flatpak-plugin-KDE_Plasma": "sudo apt install -y plasma-discover-backend-flatpak",
    "⚪🔴  snapd and snap store gui ⚠️": "sudo apt install -y snapd && sudo snap install snapd && sudo snap install snap-store",
    "🔵  discord": "flatpak install -y flathub com.discordapp.Discord",
    "🔵  Intellij Community": "flatpak install -y com.jetbrains.IntelliJ-IDEA-Community",
    "🔵  Android Studio": "flatpak install -y com.google.AndroidStudio",
    "🔵  Visual Studio Code": "flatpak install -y com.visualstudio.code",
    "🔵  spotify": "flatpak install -y flathub com.spotify.Client",
    "🔵  steam": "flatpak install -y flathub com.valvesoftware.Steam",
    "🔵  telegram": "flatpak install -y flathub org.telegram.desktop",
    "🔵  0ad": "flatpak install -y com.play0ad.zeroad",
    "⚪  KVM \"Kernel Virtual Machine\" Desktop use 💻": "sudo apt install -y qemu-system libvirt-daemon-system",
    "⚪  KVM \"Kernel Virtual Machine\" Server use 💾": "sudo apt install -y --no-install-recommends qemu-system libvirt-clients libvirt-daemon-system"

}

