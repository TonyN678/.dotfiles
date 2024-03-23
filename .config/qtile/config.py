from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
# from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration
import os, subprocess
from libqtile.command import lazy

# Run the programs in autostart.sh once after start-up
@hook.subscribe.startup_once
def autostart_once():
	home = os.path.expanduser('~/.config/qtile/autostart.sh')
	subprocess.Popen([home])



mod = "mod4" # window key
alt_key = "mod1"

terminal = "alacritty"

# To know the key names, use "xev" and press any key, that key name will appear on the terminal, usually the name in string in bracket
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows

    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.

    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


    Key([mod], "n", lazy.layout.normalize()),
     
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod],"f", lazy.window.toggle_fullscreen(),desc="Toggle fullscreen on the focused window",),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # uncomment to use qtile own search menu
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("rofi -theme ~/.config/rofi/normaltheme.rasi -show drun")),
    
    Key([mod], "q", lazy.spawn("./.config/rofi/script/powermenu")),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    
    # Keys to increase/decrease screen brightness
    # Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -s set +5%")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("/home/tien/scripts/changebrightness up")),     
    # Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -s set 5%-")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("/home/tien/scripts/changebrightness down")),
    
 
    # Keys to increase/decrease audio volume
    # Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioMute", lazy.spawn("/home/tien/scripts/changevolume mute")),
    Key(["control", alt_key], "slash", lazy.spawn("/home/tien/scripts/changevolume mute")),
    # Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 1%-")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("/home/tien/scripts/changevolume down")),
    Key(["control", alt_key], "down", lazy.spawn("/home/tien/scripts/changevolume down")),
    # Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 1%+")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("/home/tien/scripts/changevolume up")),
    Key(["control", alt_key], "up", lazy.spawn("/home/tien/scripts/changevolume up")),
	
    Key([], "XF86AudioPause", lazy.spawn("/usr/bin/mocp -G")),
    Key([], "XF86AudioPlay", lazy.spawn("/usr/bin/mocp -G")),
    Key([], "XF86AudioNext", lazy.spawn("/usr/bin/mocp -f")),
    Key([], "XF86AudioPrev", lazy.spawn("/usr/bin/mocp -r")),
    
    # For taking screenshot with selected area with scrot
    Key([mod], "p", lazy.spawn("/usr/bin/scrot --select")),
    # For changing audio output device
    Key([mod], "a", lazy.spawn("/home/tien/scripts/audio-output")),

]

""""""""""""""""""
"""" GROUPS """""
""""""""""""""""""
# a list contains Group objects represent each workspaces in the groupbox widget 
groups = []

# Group's number
group_names = ["1", "2", "3", "4",]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ",]
#group_labels = ["", "", "", "", "", "",] 
group_labels = ["󰏃","󰏃","󰏃","󰏃"] 
#group_labels = ["Terminal", "CodeResources", "Web", "Music", "Files", "Documents", ]

group_layouts = [ "columns", "columns", "columns", "columns"]

# Create Group objects with attributes and paste to the list called groups
for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend(
        [
        #CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen()),
        # Key([mod], "Tab", lazy.screen.next_group()),
        # Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "control"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),

        ]
    )

# Add a ScratchPad Group With a terminal dropdown
groups.append(
    ScratchPad("scratchpad", [
        DropDown("term", terminal,x=0.25, y=0.15, width=0.45, height=0.6),
        DropDown("music", f"{terminal} -e mocp", y=0.13, x=0.23, width=0.5, height=0.7, on_focus_lost_hide=True),
        DropDown("protonvpn", f"{terminal} -e protonvpn-cli connect", y=0.13, x=0.23, width=0.5, height=0.7),
        DropDown("Visualiser", f"{terminal} -e cava", y=0.15, x=0.25, width=0.5, height=0.70, on_focus_lost_hide=False),
        ])
    )
# Add ScratchPad toogle key
keys.extend([
    Key([mod, "shift"], "Return", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key([mod], "m", lazy.group['scratchpad'].dropdown_toggle('music')),
    Key([mod], "v", lazy.group['scratchpad'].dropdown_toggle('protonvpn')),
    #lazy.spawn("st gnome-keyring-daemon --start"), lazy.spawn("st nm-applet"),  
    # Key([mod], "b", lazy.group['scratchpad'].dropdown_toggle('weather')),
])

#------------ FLOATING WINDOW ----------------- #

# reize foating windows with keybinds
@lazy.window.function 
def resize_floating_window(window, width: int = 0, height: int = 0): 
    window.cmd_set_size_floating(window.width + width, window.height + height)

# Move floating window with keybinds
@lazy.window.function 
def move_floating_window(window, x: int = 0, y: int = 0):
    new_x = window.float_x + x
    new_y = window.float_y + y
    window.cmd_set_position_floating(new_x, new_y)

# turn a window to floating state, move to middle and resize
@lazy.window.function 
def zoom_in_window(window):
    lazy.window.toggle_floating()
    window.cmd_center()
    window.cmd_set_size_floating(790, 600)

keys.extend([
Key([mod, "control" ], "h", resize_floating_window(width=10), desc='increase width by 10'), 
Key([mod, "control" ], "l", resize_floating_window(width=-10), desc='decrease width by 10'), 
Key([mod, "control" ], "k", resize_floating_window(height=10), desc='increase height by 10'), 
Key([mod, "control" ], "j", resize_floating_window(height=-10), desc='decrease height by 10'),

Key([mod, 'shift'], "h", move_floating_window(x=10), desc='move 10 left'),
Key([mod, 'shift'], 'l', move_floating_window(x=-10), desc='move 10 right'),
Key([mod, 'shift'], 'k', move_floating_window(y=10), desc='move 10 up'),
Key([mod, 'shift'], 'j', move_floating_window(y=-10), desc='move 10 down'),

Key([mod, 'shift'], 't', zoom_in_window(), desc='immidiately turn a window to floating, move to middle of the screen and resize'),
Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

])


""""""""""""""""""
"""" LAYOUTS """""
""""""""""""""""""

def init_layout_theme():
	return {
		"border_focus": '#b3b1f6',
		 "border_normal": '#00000000',
		}

layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(**layout_theme, allign=0, border_width=0, change_size=10, margin=10, single_margin=0, single_border_width=0),
    layout.Columns(**layout_theme, border_on_single=True, border_width=2, margin=8, margin_on_single=10),
    # layout.Spiral(**layout_theme),
    layout.Max(),
]

""""""""""""""""""
"""" WIDGETS """""
""""""""""""""""""


def init_colors():
    return [
        ["#434c5e", "#293e39"],  # 0 background
        ["#d8dee9", "#d8dee9"],  # 1 foreground
        ["#3b4252", "#3b4252"],  # 2 background lighter
        ["#bf616a", "#bf616a"],  # 3 red
        ["#a3be8c", "#a3be8c"],  # 4 green
        ["#ebcb8b", "#ebcb8b"],  # 5 yellow
        ["#81a1c1", "#81a1c1"],  # 6 blue
        ["#b48ead", "#b48ead"],  # 7 magenta
        ["#88c0d0", "#88c0d0"],  # 8 cyan
        ["#d8dee9", "#d8dee9"],  # 9 white
        ["#4c566a", "#4c566a"],  # 10 grey
        ["#bae1ff", "#bae1ff"],  # 11 orange
        ["#43e8d8", "#43e8d8"],  # 12 super cyan
        ["#5e81ac", "#5e81ac"],  # 13 super blue
        ["#242831", "#242831"],  # 14 super dark background
        ["#00000000", "00000000"], #15 transparent black
        ["#a265e5", "#a265e5"],  #16  purple
        ["#ecb4e2", "#ecb4e2"], #17 pink bubblegum
        ["#afeeff", "#afeeff"], #18 light cyan
	["#6f7787", "#6f7787"], #19 light grey
        ["#CAA9E0", "#CAA9E0"], #20 purple-pink"
    ]

colors = init_colors()


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length = 20
                    ),

               # widget.TextBox(
               #      font = "FiraCode Nerd Font Propo",
               #      text = "󰣇",
               #      foreground = colors[11],
               #      fontsize = 30,
               #      # mouse_callbacks = ,
               #      decorations = [
               #          RectDecoration(colour=colors[0], radius =15, filled=True, padding_y=6)
               #          ]
               #     ),

                # This widget is replacement and reference for the TextBox object above
                #widget.Image(
                #        filename='~/.config/qtile/assets/icons/arch.png',
                #        margin = 0.1,
                #        scale = True,
                #        mouse_callbacks={'Button1': lazy.spawn('alacritty')},
                #        decorations=[
                #            RectDecoration(colour=colors[0], radius=10, filled=True, padding_y=0)
                #        ]
                #        ),

                widget.GroupBox( 
                    font="FireCode Nerd Font Propo",
                    active = colors[12],
                    this_current_screen_border = colors[7],
                    inactive = colors[19],
                    foreground = colors[1],
                    highlight_method = "text",
                    borderwidth = 0,
                    center_aligned = False,
                    disable_drag = False,
                    fontsize = 16,
                    spacing=5,
		    margin = 10,
		    urgent_alert_method="line",
		    urgent_border=colors[15],
                    decorations = [RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6)]
                    ),

                widget.Spacer(
                    length = 10,
                        ),

               widget.Clock(
                        font='FiraCode Nerd Font Propo',
                        format="  %d/%m/%y | 󱎫 %H:%M ",
                        foreground=colors[20],
                        padding=0,
                        fontsize=16,
			mouse_callbacks = {'Button1': lazy.group['scratchpad'].dropdown_toggle('Calendar') },
                        decorations=[
                            RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6)
                        ]

                ), 
		 
                widget.Spacer(
                    length = 2 
                    ),

                widget.TextBox(
                    font='FiraCode Nerd Font Propo', 
                    text = " 󱂵 ",
                    foreground = colors[20],
                    fontsize = 27,
                    mouse_callbacks = {'Button1': lazy.spawn('thunar')},
                    decorations=[
                        RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6, padding_x=9)]
                    ),
                widget.Spacer(
                    length = 2
                    ),

#		widget.CurrentLayoutIcon(
#			foreground=colors[20],
#			scale= 0.45,
#			fmt = " {} ",
#			padding= 15,
#			decorations = [RectDecoration(colour=colors[0], extra_width=20,radius=13, filled=True, padding_y=6)]
#			
#		   ),

                widget.Spacer(
                    length = 750,
                        ),



	#	widget.TextBox(
 	#		text="  󰂯 ",
	#		foreground = colors[20],
	#		mouse_callbacks = {'Button1': lazy.spawn('./.config/rofi/script/bluetooth')},
 
        #                decorations =[
        #                    RectDecoration(colour=colors[0], group=True,  radius=13, filled=True, padding_y=6)
	#		    ]
	#		),
        #        widget.TextBox(
 	#		text="󰖩  ",
	#		foreground = colors[20],
	#		mouse_callbacks = {'Button1': lazy.spawn('./.config/rofi/script/wifimenu')},
        #                decorations =[
        #                    RectDecoration(colour=colors[0], group=True,  radius=13, filled=True, padding_y=6)
        #                    ]
        #                ),

#		widget.Wttr(
#			font = "FiraCode Nerd Font",
#			fontsize = 16,
#			foreground = colors[20],
#			padding = 15,
#			location = {},
#			# Add %l for location, 
#			format = "%c%t | %w",
#			units = 'm',
#			update_interval = 10,
#			user_agent = 'Qtile',
#			mouse_callbacks = {'Button1': lazy.group['scratchpad'].dropdown_toggle('weather') },
#                        decorations =[
#                            RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6)
#                            ]
#			
#			),
		
                widget.Spacer(
                        length = 10,
                        ),

                widget.Battery(
                    font="FiraCode Nerd Font Propo",
                    foreground=colors[20],
                    low_foreground=colors[7],
                    low_percentage=0.3,
                    # notification_timeout= ,
                    # notify_below= 0.3,
                    padding=0,
                    show_short_text=False,
                    full_char='󰁹',
                    charge_char='󰂋',
                    discharge_char='󰁿',
                    empty_char='󰂃',
                    format='  {char} {percent:2.0%} | 󱧦 {hour:d}:{min:02d} ',
                    fontsize=16,
                    update_interval=1,
                    # mouse_callbacks= ,
                        decorations=[
                        RectDecoration(colour=colors[0], radius=13, filled=True,extra_width=0, padding_y=6)
                    ]
                ),
                
                widget.Spacer(
                        length = 10,
                        ),

                widget.Memory(
                    font="FiraCode Nerd Font Propo",
                    foreground=colors[20],
                    padding=0,
                    format='  {MemUsed: .1f}{mm} /{MemTotal: .0f}{mm}  ',
                    fontsize=16,
                    measure_mem='G',
 		    mouse_callbacks = {'Button1': lazy.group['scratchpad'].dropdown_toggle('htop')},
                    decorations=[
                        RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6)
                        ]
                ),

                widget.Spacer(
                        length = 10,
                        ),
                
                widget.ThermalSensor(
                    font="FiraCode Nerd Font Propo",
                    fontsize=16,
                    foreground=colors[20],
                    foreground_alert=colors[3],
                    metric=True,    
                    padding=0,
                    # tag_sensor="CPU",
                    threshold=60,
                    format = '  {temp:.0f}{unit} ',
                    decorations=[
                        RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6)
                        ]
 
                 ),
                widget.Spacer(
                        length = 10,
                        ),

                widget.Backlight(
                    font="FiraCode Nerd Font Propo",
                    fontsize=16,
                    format = ' 󱩒 {percent:2.0%} ',
                    foreground=colors[20],
		   
   	            # if the widget stop working someday, check the name again at /sys/class/backlight/

                    backlight_name='amdgpu_bl0',
                    #backlight_name='amdgpu_bl1',
                    decorations=[
                        RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6)
                        ]
                ),

                widget.Spacer(
                        length = 10,
                        ),

                widget.Volume(
                        font="FiraCode Nerd Font Propo",
                        foreground=colors[20],
                        padding=0,
                        emoji=True,
                        emoji_list=['󰖁','','','󰕾'],
                        fmt='  {} ',
                        fontsize=16,
                        scroll=True,
			mouse_callbacks={'Button1': lazy.spawn("pavucontrol"), 'Button3': lazy.group['scratchpad'].dropdown_toggle('Visualiser') },
                         decorations=[
                            RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6,group=True)
                        ]

                ),                
                widget.Volume(
                        font="FiraCode Nerd Font Propo",
                        foreground=colors[20],
                        padding=0,
                        fmt='{}  ',
                        fontsize=16,
                        scroll=True,
			mouse_callbacks={'Button1': lazy.spawn("pavucontrol"), 'Button3': lazy.group['scratchpad'].dropdown_toggle('Visualiser') },
                         decorations=[
                            RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6,group=True)
                        ]
                ),


               widget.Spacer(
		length = 5,	
		),
 
		widget.Systray(
			icon_size = 25,
			padding = 2,
		),


            ],
            45,
            # opacity=1.0,
            # background=["#50586d", "#50586d"],
            background=["#00000000"],
           # north east south west
	    #  margin = [5,12,0,12],
	     margin = [3,0,-5,0],
            # border_width=[3,13,3,13],  # Draw top and bottom borders
            # border_color=["f0f0ef", "bae1ff", "f0f0ef", "bae1ff"]  # Borders are magenta
        )
        
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.toggle_floating()),
]

# dgroup list is for setting which application goes to which group
dgroups_key_binder = None
dgroups_app_rules = [
	#Rule(Match(wm_class=['qutebrowser']), group="2"),
]  
follow_mouse_focus = True
bring_front_click = True
floats_kept_above = True
cursor_warp = False

# The flaoting window will remember its palce once being moved first time
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="Pavucontrol"), 
        Match(wm_class="Blueman-manager"),  
        Match(wm_class="Gestures"),  
        Match(wm_class="Nvidia-settings"),  
        Match(wm_class="Font-manager"),  
        Match(wm_class="Thunar"),  
        Match(wm_class="Lxappearance"),  
        Match(wm_class="Nm-connection-editor"), 
        Match(wm_class="Grub-customizer"), 
        Match(title="htop"), 
        Match(title="cava"), 
    ],
	border_width=2,
	border_focus="#ffffff",
	border_normal="#00000000",
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
