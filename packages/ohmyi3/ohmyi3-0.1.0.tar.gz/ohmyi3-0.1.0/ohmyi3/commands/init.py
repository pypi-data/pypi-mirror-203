import os
import shutil
import uvicore
from ohmyi3.app import App
from uvicore.support.dumper import dump, dd
from uvicore.exceptions import SmartException
from uvicore.console import command, argument, option

@command()
async def cli():
    """Initialize a stock ~/.config/ohmyi3/* configuration"""

    # Get the application instance
    app = App(must_exist=False);

    uvicore.log.header('Initializing ohmyi3')

    # Create ~/.config/ohmyi3/ and copy stubs
    if not os.path.exists(app.config_folder):
        uvicore.log.item(f"Creating {app.config_folder} folder")
        #os.mkdir(app.config_folder)
        uvicore.log.item(f"Copying base configs into {app.config_folder} folder")
        shutil.copytree(app.stubs_folder + '/', app.config_folder + '/')

    # Create ~/.config/i3
    if not os.path.exists(app.i3config_folder):
        uvicore.log.item(f"Creating {app.i3config_folder} folder")
        os.mkdir(app.i3config_folder)

    # Create ~/.config/i3status
    if not os.path.exists(app.i3status_folder):
        uvicore.log.item(f"Creating {app.i3status_folder} folder")
        os.mkdir(app.i3status_folder)

    uvicore.log.nl()
    uvicore.log('Done!  Now run: i3ctl generate')
