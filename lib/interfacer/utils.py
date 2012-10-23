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
import glob
import imp

def find_module_path(name):
    ''' given the name of a library directory, look for it in all the likely places '''
    for x in [ name, "../%s" % name, "/usr/share/%s" % name ]:
        if os.path.exists(x):
            return x
    return None

def load_modules(dir, class_name='CliModule'):
    ''' given a selected library directory, return plugin instances '''
    modules = {}
    for path in glob.glob(os.path.join(dir, '*.py')): 
        (name, ext) = os.path.splitext(os.path.basename(path))
        if not name.startswith("_"):
            modules[name] = imp.load_source(name, path).register()
    return sorted(modules.values(), key=lambda m: m.name())
