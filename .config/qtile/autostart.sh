#!/bin/sh

# preserve the wallpaper 
feh --bg-scale ~/Wallpapers/Aesthetic2.png &

# apply picom settings when the session starts
picom --fade-in-step=1 --fade-out-step=1 --fade-delta=0 -b -f &

# enable automounting disk
# udiskie & 

# enable the mouse in touchpad to function: tapping, drag, scroll
xinput set-prop "ELAN1203:00 04F3:307A Touchpad" "libinput Tapping Enabled" 1 &
xinput set-prop "ELAN1203:00 04F3:307A Touchpad" "libinput Tapping Drag Lock Enabled" 1 &
xinput set-prop "ELAN1203:00 04F3:307A Touchpad" "libinput Natural Scrolling Enabled" 1 &

# Set the screen refresh rate from 144hz to 60.00hz to increase battery duration
xrandr -r 60.00 & 

# protonvpn-cli fix - by installing gnome-keyring and network-manager-applet and start these commands as session begins
gnome-keyring-daemon --start &
nm-applet &

# Enable swipe and pinch gestures for touchpad
# libinput-gestures &
libinput-gestures-setup stop desktop autostart start

# lxsession for theme color config
# lxsession &
