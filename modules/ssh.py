import interfacer.base_module as base_module
import sys

def register():
    return SshModule()        

class ListCommand(base_module.SubCommand):
    ''' example_cli ssh list [--name] '''

    def name(self):
        return 'list'

    def description(self):
        return 'list the tribbles'

    def options(self):

        return [
           [ "-n", "--name", dict(dest="name", help="list tribles only with this name") ]
        ]

    def run(self, options, args):
        tribbles = [ 'xyork', 'slorg', 'rooster', 'blinky', 'poorboy', 'willy', ]
   
        found = False
        for x in tribbles:
            if options.name is not None:
                if options.name.lower() in x:
                    found = True
                    print x 
            else:
                print x    

        if not found and options.name is not None:
            # TODO: make this an exception subclass
            sys.stderr.write("error: tribble (%s) not found" % options['name'])
            return 1
        return 0
    
class SshModule(base_module.BaseModule):
    ''' example_cli tribbles [...] '''

    def name(self):
        return 'ssh'

    def description(self):
        return 'does things with ssh'

    def sub_commands(self):
        return [
            ListCommand(self)
        ]