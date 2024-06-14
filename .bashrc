alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME'
alias activate="source env/bin/activate"
alias cbonsai="cbonsai -i -l -b 1 -m Hello"
alias weather="curl wttr.in/"
alias vpn="protonvpn-cli c -f"
alias monitor="xrandr --output HDMI-A-0 --mode 1920x1080 --rate 60 --brightness 0.7"
alias offvpn="nmcli con down pvpn-ipv6leak-protection"
alias fetch="clear; echo ""; neofetch"

eval "$(starship init bash)"
