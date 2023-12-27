
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration
mod = "mod1"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows

    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.

    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # press mod+z to enter resizing mode, press Esc to escape from resizing mode    
    KeyChord([mod], "z", [
        Key([], "h", lazy.layout.grow()),
        Key([], "l", lazy.layout.shrink()),
        # set window in 50:50 ratio
        Key([], "n", lazy.layout.normalize()),
        # set currently focused window to max
        Key([], "m", lazy.layout.maximize())],
        mode=True,
        name="Resizable"
        ),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),

    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod],"f", lazy.window.toggle_fullscreen(),desc="Toggle fullscreen on the focused window",),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # uncomment to use qtile own search menu
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "r", lazy.spawn("rofi -show drun")),
    
    # Keys to increase/decrease screen brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -s set +5%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -s set 5%-")),

    # Keys to increase/decrease audio volume
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer sset Master 1%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer sset Master 1%+")),

]

""""""""""""""""""
"""" GROUPS """""
""""""""""""""""""
# a list contains Group objects represent each workspaces in the groupbox widget 
groups = []

# Group's number
group_names = ["1", "2", "3", "4", "5", "6"]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ",]
group_labels = ["", "", "", "", "", "",] 
#group_labels = ["Terminal", "CodeResources", "Web", "Music", "Files", "Documents", ]

group_layouts = ["monadtall", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall",]

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
        Key([mod], "Tab", lazy.screen.next_group()),
        Key([mod, "shift" ], "Tab", lazy.screen.prev_group()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "control"], i.name, lazy.window.togroup(i.name) , lazy.group[i.name].toscreen()),

        ]
    )


""""""""""""""""""
"""" LAYOUTS """""
""""""""""""""""""

layouts = [
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=0),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(allign=0, border_focus='#66b2b2', border_normal='#004c4c', border_width=2, change_size=10, margin=10, single_margin=1),
    layout.Max()
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    
]

""""""""""""""""""
"""" WIDGETS """""
""""""""""""""""""


def init_colors():
    return [
        ["#2e3440", "#2e3440"],  # 0 background
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
    ]

colors = init_colors()

widget_defaults = dict(
    font="sans",
    fontsize=14,
    padding=6,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length = 0
                    ),

                widget.TextBox(
                     font = "FiraCode Nerd Font Propo",
                     text = "󰣇",
                     foreground = colors[11],
                     fontsize = 30,
                     # mouse_callbacks = ,
                     decorations = [
                         RectDecoration(colour=colors[0], radius =15, filled=True, padding_y=6)
                         ]
                    ),
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

                widget.Spacer(
                    length = 10
                    ),
               widget.Clock(
                        font='FiraCode Nerd Font Propo',
                        format="  %d/%m/%y | 󱎫 %H:%M ",
                        foreground="#5e5ef6",
                        padding=0,
                        fontsize=16,
                        decorations=[
                            RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6)
                        ]

                ), 
                
               # widget.Spacer(
               #     length = 10
               #     ),

               # widget.TextBox(
               #     font='FiraCode Nerd Font Propo', 
               #     text = " 󱂵 ",
               #     foreground = colors[13],
               #     fontsize = 30,
               #     mouse_callbacks = {'Button1': lazy.spawn('thunar')},
               #     decorations=[
               #         RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6, padding_x=9)]
               #     ),

                
                widget.Spacer(
                    length = 370,
                        ),

                widget.GroupBox( 
                    font="FireCode Nerd Font Propo",
                    active = "#006666",
                    inactive = colors[10],
                    # background = colors[0],
                    foreground = colors[1],
                    highlight_method = "text",
                    this_current_screen_border = colors[12],
                    borderwidth = 2,
                    center_aligned = False,
                    disable_drag = False,
                    fontsize = 16,
                    margin = 9,
                    decorations = [RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6)]

                    ),

                widget.Spacer(
                    length = 200,
                    ),

                widget.Battery(
                    font="FiraCode Nerd Font Propo",
                    foreground=colors[4],
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
                    foreground=colors[5],
                    padding=0,
                    format='  {MemUsed: .1f}{mm}/{MemTotal: .1f}{mm}  ',
                    fontsize=16,
                    measure_mem='G',
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
                    foreground=colors[16],
                    foreground_alert=colors[3],
                    metric=True,    
                    padding=0,
                    # tag_sensor="CPU",
                    threshold=60,
                    format = '  {temp:.1f}{unit} ',
                    # mouse_callbacks={"Button1": openHtop},
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
                    foreground=colors[17],
                    backlight_name='amdgpu_bl2',
                    decorations=[
                        RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6)
                        ]
                ),

                widget.Spacer(
                        length = 10,
                        ),

                widget.Volume(
                        font="FiraCode Nerd Font Propo",
                        foreground=colors[18],
                        padding=0,
                        emoji=True,
                        emoji_list=['󰖁','','','󰕾'],
                        fmt='  {} ',
                        fontsize=16,
                        scroll=True,
                         decorations=[
                            RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6,group=True)
                        ]

                ),                
                widget.Volume(
                        font="FiraCode Nerd Font Propo",
                        foreground=colors[8],
                        padding=0,
                        fmt='{}  ',
                        fontsize=16,
                        scroll=True,
                         decorations=[
                            RectDecoration(colour=colors[0], radius=13, filled=True, padding_y=6,group=True)
                        ]
                ),

                widget.Spacer(
                        length = 10,
                        ),

                widget.Systray(),


            ],
            45,
            # opacity=1.0,
            background="#00000000",
            margin = [1,0,1,25],
            # border_width=[2, 4, 2, 4],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        )
        
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
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
    ]
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
