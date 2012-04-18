"""
Simple example of a configuration file for the provisioning command.
"""


#commands library from Bellatrix
#The source file can be found here:     https://bitbucket.org/adeccico/bellatrix/src/tip/bellatrix/lib/cmds.py
# and the documentation here: http://bellatrix.readthedocs.org/en/latest/source/ref/bellatrix.lib.html#module-bellatrix.lib.cmds
from bellatrix.lib import cmds
commands = cmds.apt_get_update()
commands += cmds.install_pip()
commands += cmds.pip_install("virtualenv")
commands += ['echo "Adding my own command :)" > test', 'cat test']
