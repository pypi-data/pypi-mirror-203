import os
import sys
import shutil
import uvicore
from uvicore.typing import Dict
from uvicore.support.dumper import dump, dd

class App(Dict):

    def __init__(self, must_exist = True):
        # Ohmyi3 main folder (~/.config/ohmyi3)
        # Override with env OHMYI3_CONFIG_PATH
        self.config_folder = self.path(uvicore.config('ohmyi3.config_path'), must_exist,
            message="Perhpas you havent run 'i3ctl init' yet??")

        # config.d folder (~/.config/ohmyi3/config.d)
        self.configd_folder = self.path(self.config_folder + '/config.d', must_exist)

        # themes.d folder (~/.config/ohmyi3/themes.d)
        self.theme_folder = self.path(self.config_folder + '/themes.d')

        # i3 config path (~/.config/i3) and file
        # Override with env OHMYI3_I3CONFIG_PATH
        self.i3config_folder = self.path(uvicore.config('ohmyi3.i3config_path'))

        # i3status path (~/.config/i3status/config)
        self.i3status_folder = self.path(uvicore.config('ohmyi3.i3status_path'))

        # Stubs folder
        self.app_folder = self.path(uvicore.app.package(main=True).path, True)
        self.stubs_folder = self.path(self.app_folder + '/stubs', True)

        # Import user settings (~/.config/ohmyi3/settings.py)
        if must_exist:
            self.settings = self._import_settings();

    def path(self, location, must_exist=False, message=None):
        real = os.path.realpath(os.path.expanduser(location))
        if must_exist:
            if not os.path.exists(real):
                print(f"{real} not found")
                if message: print(message)
                exit(1)
        return real


    def _cleanup(self):
        pycache = self.path(self.config_folder + '/__pycache__')
        if os.path.exists(pycache):
            shutil.rmtree(pycache)


    def _import_settings(self):
        sys.path.append(os.path.realpath(self.config_folder))
        from settings import Settings
        return Settings(self)


