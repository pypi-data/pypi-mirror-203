import os
import platform
from datetime import datetime
from uvicore.support.module import load
from jinja2 import Environment as JinjaEnv
from uvicore.support.dumper import dump, dd
from jinja2 import FileSystemLoader as JinjaLoader

def plugin(module, **kwargs):
    return load('plugins.' + module).object


def path(location, must_exist=False, notfound_message=None):
    """Path helper with realpath and expanduser capabilities"""
    if type(location) == list:
        # If location is a list, join together with /
        location = "/".join(location)

    # Get real expanded path
    real = os.path.realpath(os.path.expanduser(location))

    # If must_exist, ensure it exists or display a message and exit
    if must_exist:
        if not os.path.exists(real):
            print(f"{real} not found")
            if notfound_message: print(notfound_message)
            exit(1)

    # Return real expanded path
    return real

def exists(location):
    """Check if path exists, using path() helper for realpath and expanduser"""
    return os.path.exists(path(location))


def now(dateformat='%Y-%m-%d_%H-%M-%S'):
    """Get now() date time in specified format (defaults 2021-01-24_19-24-58)"""
    return datetime.now().strftime(dateformat)


def shell(cmd):
    return os.system(cmd)


def template(path, file, **kwargs):
    """Render a file through the Jinja2 templating system"""
    loader = JinjaLoader(searchpath=path)
    env = JinjaEnv(loader=loader)
    template = env.get_template(file)
    rendered = template.render(kwargs)
    return rendered

def loggedinuser():
    return os.getlogin();

def hostname():
    return platform.node()
