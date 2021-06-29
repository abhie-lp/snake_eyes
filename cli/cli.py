"""Main file to handle cli commands"""

from os import listdir, path
from typing import List, Optional
from click import command, MultiCommand, Context, Command

cmd_folder = path.join(path.dirname(__file__), "commands")
cmd_prefix = "cmd_"


class CLI(MultiCommand):
    """Go to the speicific command and run it"""

    def list_commands(self, ctx: Context) -> List[str]:
        """Return a sorted list of commands"""
        return sorted(
            [filename[len(cmd_prefix):-3] for filename in listdir(cmd_folder)
             if filename.endswith(".py") and filename.startswith(cmd_prefix)]
        )

    def get_command(self, ctx: Context, cmd_name: str) -> Optional[Command]:
        """Get specific command by looking up the module"""
        filename = path.join(cmd_folder, cmd_prefix + cmd_name + ".py")
        ns = {}

        with open(filename) as fr:
            code = compile(fr.read(), filename, "exec")
            eval(code, ns, ns)

        return ns["cli"]


@command(cls=CLI)
def cli():
    """Commands to help manage project"""
    pass
