import os
import uvicore
from ohmyi3 import util
from ohmyi3.util import path, plugin
from uvicore.typing import Dict
from ohmyi3.app import Application
from uvicore.support.dumper import dump, dd
from ohmyi3.configurator import Configurator

# Welcome to ohmyi3! A better way to dynamically control i3 configs and themes!
# See https://github.com/ohmyi3/ohmyi3

# This is the main control and configuratoin script for ohmyi3!
# All self.* variables are accessible as jinja2 variables to dynamically control
# your custom config.d/* i3 config files and themes.  Themes and plugins
# are provided by the Community (that means you!).  Plugins can be run from
# the even hooks (after_generate) to configure and tweak any part of your system
# like setting dmenu, archey, conky, nitrogen....all from the selected theme!
# Enjoy, and please contribute!

class Ohmyi3(Configurator):
    def __init__(self, app: Application):

        # Application instance
        self.app = app

        # Hostname and user from system
        self.hostname = util.hostname()
        self.user = util.loggedinuser()

        # Has battery (is laptop)
        self.has_battery = True
        self.byhost('has_battery', {
            'sunjaro': False,
            'p53': True,
            'p15': True,
            'p14s': True,
        })

        # Desktop Environment (kde, xfce, i3, cinnamon, mate, gnome)
        # I like to run i3 inside kde and xfce etc...  If runing under these DE's
        # I need to tweak the configs (no screen lock, different autostarts etc...)
        self.desktop = 'i3'
        self.byhost('desktop', {
            'sunjaro': 'kde',
            'p53': 'i3',
            'p15': 'i3',
            'p14s': 'cinnamon',
        })

        # Theme (amber, archlinux, manjaro, pink)
        self.theme = 'manjaro'
        self.byhost('theme', {
            'sunjaro': 'manjaro',
            'p53': 'manjaro',
            'p15': 'manjaro',
            'p14s': 'pink',
        })

        # Custom wallpaper base folder
        self.wallpaper_base = '~/Wallpaper'
        self.byhost('wallpaper_base', {
            'sunjaro': '~/Pictures/Wallpaper',
            'p53': '~/Pictures/Wallpaper',
        })

        # Other details for each theme
        # Wallpaper is an OVERRIDE, else defaults to the themes folder/background.[jpg|png]
        self.themes = Dict({
            'amber': {
                #'wallpaper': 'Abstract/cracked_orange.jpg',
                #'wallpaper': 'Manjaro/antelope-canyon-984055.jpg',
                #'wallpaper': 'Scenes/digital_sunset.jpg',
                #'wallpaper': 'LinuxMint/linuxmint-vera/mpiwnicki_red_dusk.jpg',
                #'wallpaper': 'LinuxMint/linuxmint-vanessa/navi_india.jpg',
                'wallpaper': 'LinuxMint/linuxmint-una/nwatson_eclipse.jpg',
                #'wallpaper': 'LinuxMint/linuxmint-vera/navi_india.jpg',
                #'wallpaper': 'LinuxMint/linuxmint-ulyssa/tangerine_nanpu.jpg',
                #'wallpaper': 'Manjaro/sky-3189347.jpg',
                'archey3': 'yellow',
            },
            'archlinux': {
                #'wallpaper': 'Archlinux/349880.jpg',
                'archey3': 'blue',
            },
            'manjaro': {
                #'wallpaper': 'Manjaro/illyria-default-lockscreen-nobrand.jpg',
                #'wallpaper': 'Manjaro/wpM_orbit2_textured.jpg'
                'archey3': 'green',
            },
            'pink': {
                #'wallpaper': 'Abstract/artistic_colors2.jpg',
                #'wallpaper': 'Landscape/backlit-chiemsee-dawn-1363876.jpg',
                #`'wallpaper': 'Manjaro/DigitalMilkyway.png',
                #'wallpaper': 'LinuxMint/linuxmint-una/eeselioglu_istanbul.jpg',
                #'wallpaper': 'Abstract/neon_huawei.jpg',
                'archey3': 'cyan',
            },
        })
        self.byhost({
            'p15': {'themes.manjaro.wallpaper': 'Manjaro/wpM_orbit2_textured.jpg'}
        })
        # self.byhost('themes.amber.wallpaper', {
        #     'p15': None,
        # })

        # Default font for window titles (not bar.font)
        self.font = 'xft:URWGothic-Book 9'

        # i3bar configs
        # All themes may obey these global bar configs, or they may set their own
        self.bar = Dict({
            #'cmd': 'i3bar',
            'cmd': 'i3bar --transparency',
            'status_cmd': 'i3status',
            'position': 'bottom',
            'font': 'xft:URWGothic-Book 8',

            # Hide or show the bar
            'mode': 'dock', # dock|hide|invisible
            'hidden_state': 'show', # hide|show

            # Modifier makes the hidden bar show up while key is pressed
            'modifier': 'none',
            #'modifier': 'Ctrl+$alt',
        })
        # If not using pure i3 (i3 in kde or xfce... hide the bar)
        if self.desktop != 'i3':
            self.bar.mode = 'hide'
            self.bar.hidden_state = 'hide'
        # self.byhost('bar.position', {
        #     'p15': 'top'
        # })
        # self.byhost({
        #     'p15': {
        #         'bar.cmd': 'xxx',
        #         'bar.position': 'yyy'
        #     }
        # })

        # Preferred applications, could change depending on DE installed
        self.terminal = 'konsole'
        self.calculator = 'kcalc'
        self.screenshot = 'spectacle' # i3-scrot
        self.dmenu = path('~/.files/scripts/dmenu-run-blue')
        self.volumectrl = 'pavucontrol' # konsole -e 'alsamixer'
        if self.theme == 'manjaro':
            self.dmenu = path('~/.files/scripts/dmenu-run-green')
        # self.byhost({
        #     'p15': {
        #         'terminal': 'xfce4-terminal',
        #         'calculator': 'gcalc'
        #     }
        # })

        # Dynamically Load and Instantiate Plugins
        self.plugins = Dict({
            'nitrogen': plugin('nitrogen.Nitrogen')(self, 'tt'),
            'archey3': plugin('archey3.Archey3')(self)
        })


    async def before_generate(self):
        """This hook fires before the new i3 config is generated"""


    async def after_generate(self):
        """This hook fires after the new i3 config is generated"""

        # Set themed wallpaper
        self.plugins.nitrogen.set_wallpaper()

        # Set themed archey in my .zshrc and or .bashrc
        self.plugins.archey3.set_archey()

