import os
import sys
import shutil
import uvicore
from uvicore.typing import Dict
from uvicore.support.dumper import dump, dd
from ohmyi3.util import path

class Application(Dict):

    def __init__(self, must_exist = True):

        # Ohmyi3 main folder (~/.config/ohmyi3)
        self.config_folder = path(uvicore.config('ohmyi3.config_path'), must_exist,
            notfound_message="Perhpas you havent run 'i3ctl init' yet??")

        # Ohmyi3 i3 configs folder (~/.config/ohmyi3/configs)
        self.configd_folder = path([self.config_folder, 'config.d'], must_exist)

        # Ohmyi3 i3 themes folder (~/.config/ohmyi3/themes)
        self.themes_folder = path([self.config_folder, 'themes'])

        # i3 config folder (~/.config/i3)
        self.i3config_folder = path(uvicore.config('ohmyi3.i3config_path'))

        # i3status path (~/.config/i3status)
        self.i3status_folder = path(uvicore.config('ohmyi3.i3status_path'))

        # Stubs folder
        self.app_folder = path(uvicore.app.package(main=True).path, True)
        self.stubs_folder = path([self.app_folder, 'stubs'], True)

        # Import user settings (~/.config/ohmyi3/settings.py)
        if must_exist:
            self.configurator = self._import_configurator();


    def _cleanup(self):
        pycache = path([self.config_folder, '__pycache__'])
        if os.path.exists(pycache):
            shutil.rmtree(pycache)


    def _import_configurator(self):
        """Dynamically import the users ~/.config/ohmyi3/configurator.py"""
        sys.path.append(os.path.realpath(self.config_folder))
        from configurator import Ohmyi3
        return Ohmyi3(self)


