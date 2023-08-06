import os
import platform
from uvicore.typing import Dict

# ohmyi3 configuration python class
# Configs as python gives unlimited flexibility and programability
# All of these self.* variables are accessible as jinja2 variables
# to dynamically control your config.d/* i3 files

class Settings(Dict):
    def __init__(self):

        # Desktop Environment (kde, xfce, i3, cinnamon, mate, gnome)
        self.de = 'kde'

        # Theme
        self.theme = 'manjaro'

        # Hostname
        self.hostname = platform.node()

        # Logged in User
        self.user = os.getlogin()
