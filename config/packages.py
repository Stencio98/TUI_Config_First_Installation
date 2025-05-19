programs = {
    "update debian packages (apt)": "apt-get clean && apt-get update && apt-get dist-upgrade && apt-get full-upgrade && apt-get autoremove",
    
    "update flatpak packages": "sudo flatpak update",
    
    "update snap packages": "sudo snap refresh",
    
    "install gedit and gedit's plugins (apt)": "apt install gedit && apt install gedit-plugins",
    
    "install flatpak with flathub": "sudo apt install -y flatpak && flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo",
    
    "install flatpak-plugin-gnome": "sudo apt install -y gnome-software-plugin-flatpak",
    
    "install flatpak-plugin-KDE_Plasma": "sudo apt install -y plasma-discover-backend-flatpak",
    
    "install discord (flatpak)": "flatpak install -y flathub com.discordapp.Discord",
    
    "install spotify (flatpak)": "flatpak install -y flathub com.spotify.Client",
    
    "install steam (flatpak)": "flatpak install -y flathub com.valvesoftware.Steam",
    
    "install telegram (flatpak)": "flatpak install -y flathub org.telegram.desktop",
    
    "install telegram (apt)": "apt install telegram-desktop",
    
    "install gedit and gedit's plugins": "apt install gedit && apt install gedit-plugins",
    
    "install virtualbox (debian.org)": (
    	"sudo apt install -y lsb-release && "
        "echo \"deb http://deb.debian.org/debian $(lsb_release -cs)-backports main contrib\" | sudo tee /etc/apt/sources.list.d/backports.list && "
        "sudo apt install -y fasttrack-archive-keyring && "
        "echo \"deb http://fasttrack.debian.net/debian-fasttrack/ $(lsb_release -cs)-fasttrack main contrib\" | sudo tee /etc/apt/sources.list.d/fasttrack.list && "
        "echo \"deb http://fasttrack.debian.net/debian-fasttrack/ $(lsb_release -cs)-backports-staging main contrib\" | sudo tee -a /etc/apt/sources.list.d/fasttrack.list && "
        "sudo apt update && "
        "sudo apt install -y virtualbox virtualbox-ext-pack && "
        "sudo apt install -y virtualbox-guest-x11 && "
        "sudo apt install -y virtualbox-guest-utils"
    
    "install snapd and snap store gui": "sudo apt install snapd && sudo snap install snapd && sudo snap install snap-store"
    
}

