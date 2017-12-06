"""
skele

Usage:
  dash-admin startproject <projectname>
  dash-admin -h | --help
  dash-admin --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  dash-admin startproject myproject

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/gaw89/dash-admin
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import dash_admin.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(dash_admin.commands, k) and v:
            module = getattr(dash_admin.commands, k)
            dash_admin.commands = getmembers(module, isclass)
            command = [command[1] for command in dash_admin.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
