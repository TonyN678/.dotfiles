#!/bin/sh
xrandr --output HDMI-A-0 --mode 1920x1080 --rate 60 --brightness 0.7 &

# preserve the wallpaper 
feh --bg-scale ~/Assets/wallpapers/SunsetDreamy.png &

# apply picom settings when the session starts
picom --fade-in-step=1 --fade-out-step=1 --fade-delta=0 -b -f &
# picom &

# enable automounting disk
udiskie & 

# enable the mouse in touchpad to function: tapping, drag, scroll
xinput set-prop "ELAN1203:00 04F3:307A Touchpad" "libinput Tapping Enabled" 1 &
xinput set-prop "ELAN1203:00 04F3:307A Touchpad" "libinput Tapping Drag Lock Enabled" 1 &
xinput set-prop "ELAN1203:00 04F3:307A Touchpad" "libinput Natural Scrolling Enabled" 1 &

# Set the screen refresh rate from 144hz to 60.00hz to increase battery duration
xrandr -r 60.00 & 

# protonvpn-cli fix - by installing gnome-keyring and network-manager-applet and start these commands as session begins
# in gnome-keyring
gnome-keyring-daemon --start &
# in network-manager-applet
nm-applet &
# in blueman
blueman-applet &

# lxsession for theme color config
# lxsession &

# Enable Vietnamese input method
#fcitx5 &

# Disable the screen timeout and display power management
xset s off -dpms &

# Enable swipe and pinch gestures for touchpad
libinput-gestures-setup stop desktop autostart start 
