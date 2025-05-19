programs = {
    "[1]  🔄 update debian packages    [🛠️ apt]": "apt-get clean && apt-get update && apt-get dist-upgrade -y && apt-get full-upgrade -y && apt-get autoremove -y",
    "[2]  🔄 update flatpak packages    [⚠️ you need flatpak installed [5] ⚠️ -- 🛠️ flatpak]": "sudo flatpak update -y",
    "[3]  🔄 update snap packages    [⚠️ you need snapd installed [16] ⚠️ -- 🛠️ snap]": "sudo snap refresh",
    "[4]  ⚙️ install gedit and gedit's plugins    [🛠️ apt]": "apt install -y gedit && apt install -y gedit-plugins",
    "[5]  ⚙️ install flatpak with flathub    [🛠️ apt]": "sudo apt install -y flatpak && flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo",
    "[6]  ⚙️ install flatpak-plugin-gnome    [🛠️ apt]": "sudo apt install -y gnome-software-plugin-flatpak",
    "[7]  ⚙️ install flatpak-plugin-KDE_Plasma    [🛠️ apt]": "sudo apt install -y plasma-discover-backend-flatpak",
    "[8]  ⚙️ install discord    [🛠️ flatpak]": "flatpak install -y flathub com.discordapp.Discord",
    "[9]  ⚙️ install spotify    [🛠️ flatpak]": "flatpak install -y flathub com.spotify.Client",
    "[10] ⚙️ install steam    [🛠️ flatpak]": "flatpak install -y flathub com.valvesoftware.Steam",
    "[11] ⚙️ install telegram                                                          [🛠️ flatpak]": "flatpak install -y flathub org.telegram.desktop",
    "[12] ⚙️ install telegram    [🛠️ apt]": "apt install telegram-desktop",
    "[13] ⚙️ install 0ad    [🛠️ flatpak]": "flatpak install -y com.play0ad.zeroad",
    "[14] ⚙️ install KVM \"Kernel Virtual Machine\"    [🛠️ apt]": "sudo apt install -y qemu-system libvirt-daemon-system",
    "[15] ⚙️ install KVM \"Kernel Virtual Machine\" when installing on a server    [🛠️ apt]": "sudo apt install -y --no-install-recommends qemu-system libvirt-clients libvirt-daemon-system",
    "[16] ⚙️ install snapd and snap store gui    [🛠️ apt and snapd]": "sudo apt install -y snapd && sudo snap install snapd && sudo snap install snap-store"
    
}


#"install virtualbox (debian.org)": (
#    	"sudo apt install -y lsb-release && "
#        "echo \"deb http://deb.debian.org/debian $(lsb_release -cs)-backports main contrib\" | sudo tee /etc/apt/sources.list.d/backports.list && "
#        "sudo apt install -y fasttrack-archive-keyring && "
#        "echo \"deb http://fasttrack.debian.net/debian-fasttrack/ $(lsb_release -cs)-fasttrack main contrib\" | sudo tee /etc/apt/sources.list.d/fasttrack.list && "
#        "echo \"deb http://fasttrack.debian.net/debian-fasttrack/ $(lsb_release -cs)-backports-staging main contrib\" | sudo tee -a /etc/apt/sources.list.d/fasttrack.list && "
#        "sudo apt update && "
#        "sudo apt install -y virtualbox virtualbox-ext-pack && "
#        "sudo apt install -y virtualbox-guest-x11 && "
#        "sudo apt install -y virtualbox-guest-utils"
#    ),

