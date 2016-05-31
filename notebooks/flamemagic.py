"""
==========
tutormagic
==========
Magics to Pyro4.utils.flame in the notebook.
PYRO_FLAME_ENABLED=true pyro4-flameserver -p 9999
Usage
=====
To enable the magics below, execute ``%load_ext tutormagic``.
``%%flame``
{flamemagic_DOC}
"""

from __future__ import print_function
import sys
import Pyro4.utils.flame

from IPython.core.magic import Magics, magics_class, cell_magic
from IPython.core.magic_arguments import (argument, magic_arguments, parse_argstring)
from IPython.display import Markdown, Pretty

@magics_class
class FlameMagics(Magics):
    """
    A magic function to run Pyro4.utils.flame from a code cell.
    """
    def __init__(self, shell):
        super(FlameMagics, self).__init__(shell)
        Pyro4.config.SERIALIZER = "pickle"  # flame requires pickle serializer
        self.flame = None

    @magic_arguments()
    @argument(
        '-h', '--host', action='store', nargs = 1,
        help="Flame server"
        )

    @argument(
        '-p', '--port', action='store', nargs=1,
        help="Port number"
        )

    @cell_magic
    def flame(self, line, cell):
        if line:
            args = parse_argstring(self.flame, line)

            if args.host:
                host = args.host[0]
            if args.port:
                port = int(args.port[0])
        else:
            host = 'localhost'
            port = 9999

        if self.flame is None:
            self.flame = Pyro4.utils.flame.connect("{}:{}".format(host, port))

        self.flame.execute(cell)
        try:
            out = self.flame.evaluate('out')
        except NameError:
            out = ''
        #print(out)
        #self.shell.write(out)
        #self.shell.run_code(out)
        #return dir(self.shell)
        #return Markdown(out)
        sys.stdout.write(out)
        sys.stdout.flush()

        """
        for cml in cell.split('\n'):
            print(cml)
            out = self.flame.evaluate(cml)
            out = self.flame.
            print(out)
            #self.shell.write(out)
        """


def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(FlameMagics)