from libqtile.widget import base

class CustomBattery(base.InLoopPollText):
    defaults = [
        ("update_interval", 5, "Seconds between updates"),
        ("low_percentage", 0.2, "Low battery threshold"),
        ("font", "SF Pro", "Font for the widget"),
    ]

    def __init__(self, **config):
        base.InLoopPollText.__init__(self, **config)
        self.add_defaults(CustomBattery.defaults)
        self.foreground = "#ffffff"  # Texto siempre blanco
        self.low_foreground = "#ff5555"  # Rojo para batería baja

    def poll(self):
        try:
            # Leer porcentaje y estado (ajusta BAT0 si es necesario)
            percent = int(open("/sys/class/power_supply/BAT0/capacity", "r").read().strip())
            status = open("/sys/class/power_supply/BAT0/status", "r").read().strip()

            # Calcular el nivel de llenado (5 segmentos en lugar de 10)
            filled = int(percent / 20)  # Divide entre 20 para 5 segmentos
            empty = 5 - filled
            battery_bar = "█" * filled + "░" * empty
            battery_icon = f"[{battery_bar}]"

            # Indicador de carga
            charge_icon = "⚡" if status == "Charging" else ""

            # Color según el nivel de batería
            current_foreground = self.low_foreground if percent < self.low_percentage * 100 else self.foreground

            # Formato final
            return f"{percent}% {battery_icon}{charge_icon}"

        except FileNotFoundError:
            return "Err [□□□□□]"
        except Exception as e:
            return f"Err: {str(e)}"