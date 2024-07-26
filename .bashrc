alias config='/usr/bin/git --git-dir=$HOME/.cfg/ --work-tree=$HOME'
alias activate="source env/bin/activate"
alias cbonsai="cbonsai -i -l -b 1 -m Hello"
alias weather="curl wttr.in/"
alias vpn="protonvpn-cli c -f"
alias monitor="xrandr --output HDMI-A-0 --mode 1920x1080 --rate 60 --brightness 0.7"
alias offvpn="nmcli con down pvpn-ipv6leak-protection"
alias fetch="clear; echo ""; neofetch"
alias eza="eza --long --git"
eval "$(starship init bash)"

export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
