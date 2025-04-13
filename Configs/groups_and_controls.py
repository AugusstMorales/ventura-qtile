# ~/.config/qtile/Configs/groups_and_controls.py
# Configuration for groups, virtual terminals, mouse controls, and widget defaults.
# Designed for modularity and ease of maintenance.

from libqtile import qtile  # Import qtile to resolve undefined variable error
from libqtile.config import Group, Key, Drag, Click
from libqtile.lazy import lazy

def init_groups_and_controls(mod):
    """
    Initialize groups, virtual terminal bindings, mouse controls, and widget defaults.
    Args:
        mod: Modifier key (e.g., 'mod4').
    Returns:
        tuple: (groups, keys, mouse, widget_defaults, extension_defaults)
    """
    # Virtual terminal bindings (Wayland-specific)
    keys = []
    for vt in range(1, 8):
        keys.append(
            Key(
                ["control", "mod1"],
                f"f{vt}",
                lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
                desc=f"Switch to VT{vt}",
            )
        )

    # Workspace groups
    groups = [Group(i) for i in "12"]

    # Group key bindings
    for i in groups:
        keys.extend(
            [
                Key([mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),
                Key(
                    [mod, "shift"],
                    i.name,
                    lazy.window.togroup(i.name, switch_group=True),
                    desc=f"Switch to & move focused window to group {i.name}",
                ),
            ]
        )

    # Mouse controls for floating windows
    mouse = [
        Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
        Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
        Click([mod], "Button2", lazy.window.bring_to_front()),
    ]

    # Default widget and extension settings
    widget_defaults = dict(font="sans", fontsize=12, padding=3)
    extension_defaults = widget_defaults.copy()

    return groups, keys, mouse, widget_defaults, extension_defaults