#!/usr/bin/env bash
# Tien Nguyen

# This is a script for auto installing all the needed features for my Qtile system.
sudo pacman -S thunar qtile rofi firefox alacritty pipewire pipewire-pulse pipewire-alsa xorg xorg-xinit starship ttf-firacode-nerd feh udiskie network-manager-applet blueman python-psutil nvidia xf86-video-amdgpu scrot pamixer brightnessctl tldr zathura zathura-pdf-mupdf 

# Install yay
sudo pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

yay -S picom-simpleanims-git optimus-manager

systemctl start --user pipewire-pulse
