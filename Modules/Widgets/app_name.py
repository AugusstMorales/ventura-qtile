# app_name.py
from libqtile import widget
from libqtile.log_utils import logger

class AppName(widget.base.InLoopPollText):
    """Un widget que muestra solo el nombre de la aplicación activa con nombres estilo macOS."""
    defaults = [
        ("font", "sans", "Nombre de la fuente"),
        ("fontsize", None, "Tamaño de la fuente"),
        ("foreground", "#ffffff", "Color del texto"),
        ("background", None, "Color de fondo"),
        ("padding", 3, "Relleno"),
        ("update_interval", 0.5, "Intervalo de actualización en segundos"),
        ("default_text", "No App", "Texto por defecto cuando no hay ventana activa"),
    ]

    # Diccionario de nombres 
    app_names = {
        "code": "Visual Studio Code",
        "firefox": "Firefox",
        "gnome-terminal": "Terminal",
        "nautilus": "Files",
        "google-chrome": "Google Chrome",
        "gnome-calendar": "Calendar",
        "nvim": "Neovim",
        "telegram-desktop": "Messages",
        "bruno": "Bruno",
        "skype": "Skype",
    }

    def __init__(self, **config):
        widget.base.InLoopPollText.__init__(self, **config)
        self.add_defaults(AppName.defaults)
        # Cacheamos el texto por defecto desde la configuración
        self.default_text = self.default_text

    def poll(self):
        """Obtiene el nombre de la aplicación activa."""
        try:
            window = self.qtile.current_window
            if not window:
                return self.default_text

            # Obtener wm_class de la ventana
            wm_class = window.window.get_wm_class()
            if not wm_class:
                return window.name or self.default_text

            # Usar el segundo elemento de wm_class (class) si existe, o el primero (instance)
            app_key = (wm_class[1] if len(wm_class) > 1 else wm_class[0]).lower()
            # Devolver el nombre personalizado o el wm_class si no está en el diccionario
            return self.app_names.get(app_key, app_key)

        except Exception as e:
            logger.error(f"Error en AppName widget: {e}")
            return "Error"