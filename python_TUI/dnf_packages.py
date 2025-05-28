programs = {
        "📦 dnf(RPM) packages":{
                "🔄 update": "dnf clean all && dnf update -y && dnf upgrade --refresh -y && dnf autoremove -y",
		"fastfetch (similar to neofetch)": "dnf install -y fastfetch",
		"flatpak with flathub": "dnf install -y flatpak && flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo"
        }
}
