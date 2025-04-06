# /home/augusstmorales/.config/qtile/Configs/layouts.py
from libqtile import layout
from libqtile.config import Match

# Definición de layouts principales
layouts = [
    layout.Columns(
        border_focus_stack=["#000000", "#000000"],  # Sin bordes visibles
        border_width=0,                             # Minimalista
        margin=20                                   # Espacio limpio alrededor
    ),
    layout.Max(
        border_width=0,                            # Sin bordes
        margin=20                                  # Espacio consistente
    ),
]

# Configuración del layout flotante
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,  # Reglas por defecto de qtile
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ]
)