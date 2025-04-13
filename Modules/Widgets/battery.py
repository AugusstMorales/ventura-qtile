from libqtile.widget import base

class CustomBattery(base.InLoopPollText):
    defaults = [
        ("update_interval", 5, "Seconds between updates"),
        ("low_percentage", 0.3, "Low battery threshold (30%)"),
        ("font", "SF Pro", "Font for the widget"),
    ]

    def __init__(self, **config):
        base.InLoopPollText.__init__(self, **config)
        self.add_defaults(CustomBattery.defaults)
        self.normal_color = "#00FF00"  # Verde para 30%-100%
        self.low_color = "#FFA500"    # Anaranjado para <30%
        self.charging_color = "#FFFF00"  # Amarillo para cargando

    def poll(self):
        try:
            # Leer porcentaje y estado (separados en líneas distintas)
            percent = int(open("/sys/class/power_supply/BAT0/capacity", "r").read().strip())
            status = open("/sys/class/power_supply/BAT0/status", "r").read().strip()

            # Seleccionar color según el estado y porcentaje
            if status == "Charging":
                self.foreground = self.charging_color  # Amarillo cuando carga
            else:
                self.foreground = self.low_color if percent < self.low_percentage * 100 else self.normal_color
            
            # Solo mostrar el círculo
            return "●"

        except FileNotFoundError:
            return "● Err"
        except Exception as e:
            return f"● Err: {str(e)}"