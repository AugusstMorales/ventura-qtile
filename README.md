
### Why Modular?

Apple's software excels at simplicity and maintainability. This configuration adopts the same philosophy by separating concerns:

- **Single Responsibility**: Each file handles a specific aspect (e.g., `layouts.py` for window arrangements, `keymaps.py` for shortcuts). This makes debugging and enhancements easier.
- **Scalability**: Adding new widgets, layouts, or keybindings requires minimal changes, as components are independent.
- **Clarity**: Logical organization reduces complexity, letting you focus on customization rather than navigating a monolithic file.
- **Reusability**: Widgets and utilities are designed as standalone modules, enabling reuse across different setups.

## Configuration Details

### Main Configuration (`config.py`)

The heart of the setup, `config.py` orchestrates all components into a cohesive experience. It:

- Defines the top bar with custom widgets (e.g., `AppName`, `CustomBattery`, `CustomClock`).
- Initializes keybindings via `keymaps.py`.
- Sets up groups, mouse controls, and defaults through `groups_and_controls.py`.
- Applies a Ventura-inspired wallpaper and launches the terminal and Picom at startup.

Key settings include:
- **Modifier Key**: `mod4` (Super) for intuitive shortcuts.
- **Terminal**: Automatically detected using `guess_terminal()`.
- **Bar Styling**: SF Pro font, dark background (`#02121F`), and 80% opacity for a sleek, translucent effect.

### Layouts (`Configs/layouts.py`)

Defines window arrangements (e.g., tiled, floating) and rules for floating windows. Separating layouts ensures you can tweak window behavior without touching the main configuration.

### Groups and Controls (`Configs/groups_and_controls.py`)

Manages:
- Workspace groups (e.g., "1", "2").
- Virtual terminal bindings for Wayland (`Ctrl + Alt + F1` to `F7`).
- Mouse controls for dragging and resizing floating windows.
- Default widget settings (font, size, padding).

This separation keeps `config.py` lean and makes group-related changes intuitive.

### Keybindings (`Modules/Utilities/keymaps.py`)

Centralizes keyboard shortcuts for launching apps, switching workspaces, and controlling windows. Using a dedicated file simplifies adding or modifying shortcuts.

### Custom Widgets (`Modules/Widgets/`)

Each widget is a standalone module for maximum flexibility:
- `app_name.py`: Shows the active application’s name, styled like macOS’s menu bar.
- `battery.py`: Displays battery status with a compact, glanceable design.
- `check_wifi_status.py`: Provides a color-coded Wi-Fi indicator.
- `custom_clock.py`: Renders the date and time in a clean, modern format.

### Assets

Icons and wallpapers are organized by purpose:
- **Icons**: Split into `Apps/` (e.g., Obsidian, Telegram) and `system/` (e.g., control center) for clarity.
- **Wallpapers**: Currently includes a Ventura-inspired dark background, with room for light/dark theme support.

### Startup Script (`start_picom.sh`)

Initializes Picom for compositing effects like transparency and shadows, enhancing the visual polish.

## Getting Started

1. **Install Qtile**: Ensure Qtile is installed (`pip install qtile` or via your package manager).
2. **Copy Configuration**: Place this directory in `~/.config/qtile/`.
3. **Install Dependencies**:
   - `feh` for wallpaper management.
   - `picom` for compositing.
   - SF Pro font (or a similar sans-serif font) for consistent styling.
4. **Restart Qtile**: Use `mod + control + r` to reload the configuration.
5. **Customize**: Adjust widgets, keybindings, or layouts to suit your workflow.

## Customization Tips

- **Add Widgets**: Create new files in `Modules/Widgets/` and import them in `config.py`.
- **Change Themes**: Add light/dark wallpapers in `Assets/Wallpapers/` and update `init_wallpaper()`.
- **Extend Keybindings**: Modify `keymaps.py` to include your favorite shortcuts.
- **Dynamic Theming**: Implement a script to toggle light/dark modes based on time, mimicking macOS’s auto-switching.

## Philosophy

This configuration embodies Apple’s design principles:
- **Simplicity**: A clean interface with only essential elements.
- **Cohesion**: Consistent fonts, colors, and layouts for a unified look.
- **Intuitiveness**: Easy-to-understand structure for quick tweaks.
- **Elegance**: Subtle transparency and modern typography for a polished feel.

Enjoy a desktop that’s as functional as it is beautiful.

---
*Last updated: April 12, 2025*