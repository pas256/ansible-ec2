#
# Copyright (c) rPath, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


# Michael DeHaan

import sys
import os

class Interfacer(object):
    ''' Interfacer is a multi-level command line framework '''

    def __init__(self, name, modules_list):
        ''' 
        Create a CLI around this list of module instances.  
        Use functions from interfacer.utils to load from a directory
        '''

        self.name    = name
        self.modules = modules_list
        self.app     = sys.argv[0]

    def run(self, args):
        '''
        Run command line interface
        '''

        self.app = args[0]

        if len(args) == 1 or args[1] in [ '--help', '-h', 'help' ]:
            return self.list_modules()

        for x in self.modules:
            if x.name() == args[1].lower():
                return x.run(args)

        return self.module_not_found(args[1])

    def list_modules(self):
        '''
        Print out what modules are available
        '''

        print ""
        print "usage: %s <category> [subcommand] [--options]" % self.app
        print ""

        if len(self.modules) == 0:
            sys.stderr.write("error: no modules loaded\n")
            return 1

        print "  choose a category for information about available commands:"

        for module in self.modules:
            self._print_module_line(module)
        print ""
        return 1

    def _print_module_line(self, module):
        ''' print the name of a module + description '''

        print "%20s - %s" % (module.name(), module.description())

    def module_not_found(self, name):
        '''
        I'm sorry, I can't do that, Dave.
        '''

        sys.stderr.write("error: category (%s) not found\n" % name)
        return 1

