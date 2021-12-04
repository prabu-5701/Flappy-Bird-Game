import os
import sys
from distutils.core import setup

import py2exe

orig_system_dll = py2exe.build_exe.isSystemDLL
def system_dll(pathname):
    dlls = ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll")
    if os.path.basename(pathname).lower() in dlls:
        return 0
    return orig_system_dll(pathname)
py2exe.build_exe.isSystemDLL = system_dll

sys.argv.append('py2exe')

setup(
    name =    'Flappy Bird',
    version = '1.0',
    author =  'VVD Team',
    options = {
        'py2exe': {
            'bundle_files': 1, 
            'compressed': True,
        }
    },

    windows = [{
        'script': "flappy.py",
        'icon_resources': [
            (1, 'flappy.ico')
        ]
    }],

    zipfile=None,
)
