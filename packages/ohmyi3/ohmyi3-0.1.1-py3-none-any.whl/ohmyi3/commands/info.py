import uvicore
from ohmyi3.app import Application
from uvicore.support.dumper import dump, dd
from uvicore.exceptions import SmartException
from uvicore.console import command, argument, option

@command()
async def cli():
    """Display ohmyi3 configuration information"""

    # Get the application instance
    app = Application();

    uvicore.log.header("Ohmyi3 User Specific Configurator Instance")
    del app.configurator.app
    dump(app.configurator)

    uvicore.log.nl().nl()
    uvicore.log.header("Ohmyi3 Application Instance")
    del app.configurator
    dump(app)

