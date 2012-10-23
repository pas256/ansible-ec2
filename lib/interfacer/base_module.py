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

import os
import optparse
import sys
import exceptions

class SubCommand(object):
    ''' base class to a subcommand.  You will be extending this. '''
  
    def __init__(self, base_instance):
        ''' constructor, shouldn't be any need to override this '''
        self.base = base_instance

    def options(self):
        ''' what options does this command take?  Default to no options. '''
        return []

    def run(self, options, args):
        ''' implement this to traverse the options and decide how to run the command '''
        raise exceptions.NotImplementedError

    def name(self):
        ''' what is the name of the subcommand as triggered on the commmand line? '''
        return 'generic_subcommand_you_should_override_this'

    def description(self):
        ''' what description string to show when listing the subcommands '''
        return 'generic description, you should override this'

    def dispatch(self, cargs):
        ''' core function around kicking off the subcommand.  Don't override this. '''
        usage = "%s %s %s [options]" % (os.path.basename(cargs[0]), self.base.name(), self.name())
        parser = optparse.OptionParser(usage=usage)
        for option in self.options():
            (short, long, kw) = option
            parser.add_option(short, long, **kw)
        (options, args) = parser.parse_args(cargs)
        return self.run(options, args) 

class BaseModule(object):
    ''' base class for a command category that contains subcommands '''

    def __init__(self):
        ''' constructor, no need to override this. '''
        pass

    def name(self):
        ''' what is the name of the category? '''
        raise exceptions.NotImplementedError

    def description(self):
        '''
        explain what this command does in the help
        '''
        raise exceptions.NotImplementedError

    def sub_commands(self):
        '''
        return a dictionary of valid subcommands by name
        '''
        raise exceptions.NotImplementedError

    def run(self, args):
        ''' 
        defer to subcommands.  If you don't want subcommands, override this method!
        '''

        subs = self.sub_commands()
  
        if len(args) == 2 or args[2] in [ '-h', '--help']:
            self.list_subcommands(args)
            return 1        

        matched = [ x for x in subs if x.name() == args[2]]

        if len(matched) == 1:
            print ""
            rc = matched[0].dispatch(args)
            print ""
            return rc

        elif len(matched) > 1:
            sys.stderr.write("error: multiple commands respond to (%s)\n\n" % (args[2]))
        else:
            sys.stderr.write("error: subcommand (%s) not found\n\n" % (args[2]))

        sys.stderr.write("error: multiple subcommand modules found with this name")
        return 1

    def list_subcommands(self, args):
        ''' prints out the subcommands attached to this module.  Don't override this. '''

        print ""
        print "usage: %s %s <subcommand> [--options]" % (args[0], self.name())
        print ""
        print "  choose a subcommand:"
        print ""

        subs = self.sub_commands()
        for mod in subs:
             print "%20s - %s" % (mod.name(), mod.description())
        
        print ""       

def register():
    ''' each module plugin must define a register function at top level that returns a module instance '''
    return BaseModule()


