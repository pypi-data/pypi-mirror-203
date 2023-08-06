import os
import sys
import shutil
import uvicore
from glob import glob
from uvicore.typing import Dict
from ohmyi3.app import Application
from ohmyi3.util import path, now, template
from uvicore.support.dumper import dump, dd
from uvicore.exceptions import SmartException

from uvicore.console import command, argument, option

@command()
async def cli():
    """Dynamically Generate a new i3 config using Ohmyi3"""

    # Get the application instance
    app = Application()

    # Shortcut to user configurator
    configurator = app.configurator

    # Start the generation
    uvicore.log.header("Generating new i3 config using ohmyi3")

    # Fire off user defined before_generate_hook
    uvicore.log.item3("Firing user defined before_generate hook")
    await configurator.before_generate()

    # If i3 config exists, back it up
    i3config_file = f"{app.i3config_folder}/config"
    if os.path.exists(i3config_file):
        backup = path([app.i3config_folder, 'backup-' + now()])
        uvicore.log.item(f"Backing up {i3config_file} to {backup}")
        shutil.copy(i3config_file, backup)

    # Get all config.d/* files
    os.chdir(app.configd_folder)
    files = sorted(glob("*.conf"))

    # Append config.d/* and theme.d/theme to new i3 config
    with open(i3config_file, "w") as f:
        # Loop and merge each config and append to
        for file in files:
            uvicore.log.item2(f"Appending {file}")
            f.write(template(app.configd_folder, file, **configurator))
            f.write("\n\n\n")

        # Append the selected theme files
        theme_folder = f"{app.themes_folder}/{configurator.theme}"
        theme_file = path([theme_folder, 'theme.conf'])
        if os.path.exists(theme_file):
            uvicore.log.item(f"Appending THEME {configurator.theme}")
            f.write(template(theme_folder, 'theme.conf', **configurator))

    # Copy themed i3status or a default if no theme specific file exists
    i3status_folder = None
    if os.path.exists(f"{theme_folder}/i3status.conf"):
        # Use themed i3status.conf
        i3status_folder = f"{theme_folder}"
    elif os.path.exists(f"{app.themes_folder}/i3status.conf"):
        # Use default i3status.conf
        i3status_folder = f"{app.themes_folder}"
    if i3status_folder:
        uvicore.log.item(f"Copying {i3status_folder}/i3status.conf to {app.i3status_folder}/config")
        with open(f"{app.i3status_folder}/config", "w") as f:
            f.write(template(i3status_folder, 'i3status.conf', **configurator))

    # Fire off user defined afer_generate_hook
    uvicore.log.item3("Firing user defined after_generate hook")
    await configurator.after_generate()

    # Cleanup
    app._cleanup()

    # Done
    uvicore.log.nl()
    uvicore.log("Done!")
    uvicore.log(f"New {i3config_file} generated!")
    uvicore.log("Please reload i3!")
