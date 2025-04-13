# ~/.config/qtile/config.py
# Main configuration file for the Qtile desktop environment.
# Defines the core widgets and their integration into the bar, following a clean and modular design.

from libqtile import bar, qtile, widget, hook
from libqtile.config import Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Import layouts and groups
from Configs.layouts import layouts, floating_layout
from Configs.groups_and_controls import init_groups_and_controls

# Custom widgets
from Modules.Widgets.app_name import AppName
from Modules.Widgets.battery import CustomBattery
from Modules.Widgets.custom_clock import CustomClock
from Modules.Widgets.check_wifi_status import check_wifi_status

# Import key bindings
from Modules.Utilities.keymaps import init_keymaps

import os
import subprocess

# Initialize wallpaper
def init_wallpaper():
    subprocess.Popen(["feh", "--bg-fill", "/home/augusstmorales/.config/qtile/Assets/Wallpapers/Ventura Graphic Dark.png"])

# Autostart terminal and Picom
def autostart():
    subprocess.Popen([terminal])
    subprocess.Popen(["bash", "/home/augusstmorales/.config/qtile/start_picom.sh"])

# Run autostart on startup
@hook.subscribe.startup_once
def run_on_startup():
    autostart()

# Apply wallpaper
init_wallpaper()

# Core settings
mod = "mod4"
terminal = guess_terminal()

# Initialize key bindings
keys = init_keymaps(mod, terminal)

# Initialize groups, additional keys, mouse, and widget defaults
groups, group_keys, mouse, widget_defaults, extension_defaults = init_groups_and_controls(mod)
keys.extend(group_keys)  # Merge group key bindings with main keys

# Screen and bar configuration
screens = [
    Screen(
        top=bar.Bar(
            [
                # Branding Section
                widget.Sep(linewidth=1, foreground="#02121F", background="#02121F", padding=5),
                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/system/ico-topbar.png",
                    scale=False,
                    background="#02121F",
                    margin=8,
                ),
                # App Name
                widget.Sep(linewidth=1, foreground="#02121F", background="#02121F"),
                AppName(font="SF Pro bold", foreground="FFFFFF", background="#02121F", fontsize=13, padding=2),
                # Workspace Section
                widget.GroupBox(
                    font="SF Pro",
                    fontsize=12,
                    margin_y=3,
                    margin_x=5,
                    padding_x=2,
                    borderwidth=1,
                    active="#FFFFFF",
                    inactive="#777777",
                    highlight_method="border",
                    this_current_screen_border="#FFFFFF",
                    background="#02121F",
                ),
                # Spacer
                widget.Spacer(background="#02121F"),
                # System Tray and Indicators
                widget.Systray(background="#02121F", padding=5),
                widget.Sep(linewidth=1, foreground="#02121F", background="#02121F", padding=5),
                # Wi-Fi Status
                widget.GenPollText(background="#02121F", func=check_wifi_status, update_interval=10, markup=True),
                widget.Sep(linewidth=1, foreground="#02121F", background="#02121F", padding=3),
                # Keymanager
                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/system/keymanager.png",
                    scale=False,
                    background="#02121F",
                    margin=7,
                ),
                widget.Sep(linewidth=1, foreground="#02121F", background="#02121F", padding=3),
                # Obsidian
                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/Apps/Obsidian.png",
                    scale=False,
                    background="#02121F",
                    margin=6,
                ),
                widget.Sep(linewidth=1, foreground="#02121F", background="#02121F", padding=3),
                # Telegram
                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/Apps/Telegram.png",
                    scale=False,
                    background="#02121F",
                    margin=8,
                ),
                widget.Sep(linewidth=1, foreground="#02121F", background="#02121F", padding=3),
                # Ranger
                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/Apps/RangerIcon.png",
                    scale=False,
                    background="#02121F",
                    margin=8,
                    mouse_callbacks={'Button1': lazy.spawn(f"{terminal} -e ranger")},
                ),
                widget.Sep(linewidth=1, foreground="#02121F", background="#02121F", padding=3),
                # Control Center
                widget.Image(
                    filename="/home/augusstmorales/.config/qtile/Assets/Icons/system/control-update-center.png",
                    scale=False,
                    background="#02121F",
                    margin=7,
                ),
                # Battery
                CustomBattery(font="SF Pro", fontsize=7),
                # Clock
                CustomClock(
                    format='%a %b %-d %-I:%M %p',
                    font="SF Pro bold",
                    fontsize=13,
                    foreground="#FFFFFF",
                    background="#02121F",
                    padding=8,
                ),
                widget.Sep(linewidth=1, foreground="#02121F", background="#02121F", padding=5),
            ],
            size=28,
            background="#02121F",
            opacity=0.8,
        ),
    ),
]

# General settings
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