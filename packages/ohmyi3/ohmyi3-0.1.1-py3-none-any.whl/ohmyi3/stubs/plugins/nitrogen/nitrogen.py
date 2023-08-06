import uvicore
from uvicore.support.dumper import dump, dd
from ohmyi3.util import path, exists, shell

class Nitrogen:
    """
    Nitrogen Wallpaper Plugin
    Copyright (c) 2023 Matthew Reschke License http://mreschke.com/license/mit
    """

    def __init__(self, configurator, test):
        # User Configurator Instance
        self.configurator = configurator


    def set_wallpaper(self):
        """Set nitrogen wallpaper based on selected theme"""

        # Shortcuts
        configurator = self.configurator
        app = configurator.app
        theme = configurator.theme
        themes = configurator.themes
        wallpaper_base = configurator.wallpaper_base

        # Get theme background file (jpg or png)
        background = None
        theme_folder = path([app.themes_folder, theme])
        jpg = path([theme_folder, 'background.jpg'])
        png = path([theme_folder, 'background.jpg'])
        if exists(jpg): background = jpg
        if exists(png): background = png

        # Check for background override
        override = themes.dotget(f"{theme}.wallpaper")
        if override: background = path(f"{wallpaper_base}/{override}")

        # If no theme background file or override found, don't set background
        if not background: return

        # If background found, set it using nitrogen
        if exists(background):
            cmd = f"nitrogen --save --set-zoom-fill {background} > /dev/null 2>&1"
            #cmd = f"nitrogen --save --set-scaled {background} > /dev/null 2>&1"
            uvicore.log.item4(f"Plugin Nitrogen: {cmd}")
            shell(cmd)
