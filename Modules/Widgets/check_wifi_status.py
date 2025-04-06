# Wi-Fi status checker for the Qtile desktop environment.
# Provides a sleek, color-coded indicator of network connectivity.

import subprocess  # Allows execution of external commands for enhanced functionality.

def check_wifi_status():
    # Returns a formatted string showing Wi-Fi connection status with a colored indicator.
    try:
        result = subprocess.run(
            ['nmcli', '-t', '-f', 'STATE', 'general'],
            capture_output=True,
            text=True,
            timeout=2  # Adds a timeout to prevent hanging.
        )
        is_connected = "connected" in result.stdout.lower()
        status = "connect" if is_connected else "no connect"
        color = "#00ff2a" if is_connected else "#ff0000"  # Green for connected, red for disconnected.
        return f"<span foreground='{color}'>◉</span> <span foreground='#ffffff'>{status}</span>"
    except (subprocess.SubprocessError, Exception):
        # Handles errors gracefully with a clear disconnected state.
        return "<span foreground='#ff0000'>◉</span> <span foreground='#ffffff'>no connect</span>"