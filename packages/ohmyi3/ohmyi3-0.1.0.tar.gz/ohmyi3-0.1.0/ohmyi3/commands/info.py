import uvicore
from ohmyi3.app import App
from uvicore.support.dumper import dump, dd
from uvicore.exceptions import SmartException
from uvicore.console import command, argument, option

@command()
async def cli():
    """Display this systems ohmyi3 configuration information"""

    # Get the application instance
    app = App();
    dd(app)
