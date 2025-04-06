# /home/augusstmorales/.config/qtile/config.py
# Main configuration file for the Qtile desktop environment.
# Defines the core widgets and their integration into the bar, following a clean and modular design.

from libqtile import bar, qtile, widget, hook  # Core components for building a seamless desktop experience
from libqtile.config import Click, Drag, Group, Key, Screen  # Essential tools for configuring user interactions
from libqtile.lazy import lazy  # Enables effortless, on-demand command execution
from libqtile.utils import guess_terminal  # Intelligently detects the default terminal

# Import layouts from the new module
from Configs.layouts import layouts, floating_layout

# Widgets personalizados
from Modules.Widgets.app_name import AppName          # Displays the active application name with a minimalist style
from Modules.Widgets.battery import CustomBattery     # Shows battery status in a simple, glanceable format
from Modules.Widgets.custom_clock import CustomClock  # Provides a sleek, custom time display
from Modules.Widgets.check_wifi_status import check_wifi_status  # Delivers a color-coded Wi-Fi status indicator

import os  # Provides access to system-level features and file management
import subprocess  # Allows execution of external commands and scripts
import time

# Import key bindings from a dedicated utility module
from Modules.Utilities.keymaps import init_keymaps

# Sets up the desktop wallpaper with a clean, scaled appearance
def init_wallpaper():
    subprocess.Popen(["feh", "--bg-fill", "/home/augusstmorales/.config/qtile/Assets/Wallpapers/default3.jpg"])

# Launches the default terminal and Picom at startup
def autostart():
    subprocess.Popen([terminal])
    subprocess.Popen(["bash", "/home/augusstmorales/.config/qtile/start_picom.sh"])

# Triggers the autostart function once when Qtile initializes, ensuring a smooth setup
@hook.subscribe.startup_once
def run_on_startup():
    autostart()

# Applies the wallpaper immediately upon loading the configuration
init_wallpaper()

mod = "mod4"  # Defines the primary modifier key for intuitive keyboard shortcuts
terminal = guess_terminal()  # Automatically selects the preferred terminal app

# Initialize key bindings with mod and terminal variables
keys = init_keymaps(mod, terminal)

screens = [
    Screen(
        top=bar.Bar(
            [
                # Application branding and identity with a rich starting hue
                widget.Sep(
                    linewidth=1,
                    foreground="#800100",
                    background="#800100",
                ),
                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/ico-topbar.png",
                    scale=False,
                    background="#800100",
                    margin=5,
                ),
                widget.Sep(
                    linewidth=1,
                    foreground="#800100",
                    background="#800100",
                ),
                AppName(
                    font="SF Pro bold",
                    foreground="#f0edec",
                    background="#800100",
                    fontsize=12,
                    padding=3,
                ),
                widget.Sep(
                    linewidth=1,
                    foreground="#800100",
                    background="#800100",
                ),

                # Workspace navigation with a grounded tone
                widget.Sep(
                    linewidth=1,
                    foreground="#ededed",
                    background="#800100",
                ),
                widget.Sep(
                    linewidth=1,
                    foreground="#800100",
                    background="#800100",
                ),
                widget.GroupBox(
                    font="SF Pro",
                    fontsize=12,
                    margin_y=3,
                    margin_x=0,
                    padding_x=5,
                    borderwidth=2,
                    active="#f0edec",
                    inactive="#777777",
                    highlight_method="border",
                    this_current_screen_border="#ffaa00",
                    background="#800100",
                ),

                # Command prompt with a subtle shift in tone
                widget.Sep(
                    linewidth=1,
                    foreground="#800100",
                    background="#800100",
                ),
                widget.Prompt(
                    font="SF Pro",
                    fontsize=12,
                    foreground="#ffaa00",
                    background="#800100",
                ),

                # Flexible spacing to balance the layout elegantly
                widget.Spacer(
                    background="#800100",
                ),

                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/figma.png",
                    scale=False,
                    background="#800100",
                    margin=5,
                ),

                # System tray and status indicators with a forest-like hue
                widget.Systray(
                    background="#800100",
                    padding=5,
                ),

                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/telegram.png",
                    scale=False,
                    background="#800100",
                    margin=5,
                ),
                widget.Sep(
                    linewidth=1,
                    foreground="#800100",
                    background="#800100",
                ),

                widget.GenPollText(
                    background="#800100",
                    func=check_wifi_status,
                    update_interval=10,
                    markup=True
                ),
                widget.Sep(
                    linewidth=1,
                    foreground="#800100",
                    background="#800100",
                ),
                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/octocat.png",
                    scale=False,
                    background="#800100",
                    margin=5,
                ),
                # Additional status icons with a twilight tone
                widget.Sep(
                    linewidth=1,
                    foreground="#800100",
                    background="#800100",
                ),
                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/glow.png",
                    scale=False,
                    background="#800100",
                    margin=5,
                ),

                CustomBattery(font="SF Pro", fontsize=11),

                # Time and system controls with a final dark elegance
                widget.Sep(
                    linewidth=1,
                    foreground="#800100",
                    background="#800100",
                ),
                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/search.png",
                    scale=False,
                    background="#800100",
                    margin=5,
                ),
                widget.Sep(
                    linewidth=1,
                    foreground="#800100",
                    background="#800100",
                ),
                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/control-update-center.png",
                    scale=False,
                    background="#800100",
                    margin=5,
                ),
                widget.Sep(
                    linewidth=1,
                    foreground="#800100",
                    background="#800100",
                ),
                CustomClock(
                    format='%a  %b  %-d  %-I:%M  %p',
                    foreground="#f0edec",
                    background="#800100",
                    fontsize=12,
                    font="SF Pro Semibold",
                ),
                widget.Sep(
                    linewidth=1,
                    foreground="#800100",
                    background="#800100",
                ),
            ],
            25,
            background="#800100",
            opacity=9.0,
        ),
    ),
]

for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

groups = [Group(i) for i in "12"]

for i in groups:
    keys.extend(
        [
            Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Switch to & move focused window to group {i.name}"),
        ]
    )

widget_defaults = dict(font="sans", fontsize=12, padding=3)
extension_defaults = widget_defaults.copy()

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24
wmname = "LG3D"