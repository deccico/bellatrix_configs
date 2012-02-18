"""This configuration holds the list of cmds that are going to be applied to a list of ami's. 
This is part of the normal Bellatrix process. The new configuration will be burned into a new ami."""

import os

#list of ami's to process with the below cmds
amis = [
       ["ami-fd589594",  "ubuntu1104-ff36-mysql51-x64"],
       ]

#common variables
burn_ami_at_the_end=True    #decide whether or not burning the images at the end
skip_me = False             #decide whether to skip or not this configuration
user = "ubuntu"             #user of the ami's 

#this values will be applied to the instance that is going to be configured with bellatrix bewitch_ami
#once you have your ami configured, then you can launch it with a different configuration 
key_name = "elasticbamboo"          #Name of the key-pair name that will be applied to your instance. 
security_groups = "elasticbamboo"   #comma separated list (with no spaces) of the security groups that will be applied to the new instance. It can be only one. Usually is. e.g. mysecurity_group
instance_type = "t1.micro"          #type of instance that will be used for applying the configuration. Usually t1.micro should be enough. List of codes here: http://aws.amazon.com/ec2/instance-types for more


#------------------------------------------------------------------------------------------------
from bellatrix_configs.lib import cmds

env = "django_app"
project_name = "app"
django_app_dir = "/home/ubuntu/django_app"

def configureNginx():
    #prepare directories
    commands = ["sudo mkdir -p /opt/django/logs/nginx/"]
    #Create directories and softlinks for static content and templates
    commands.append("mkdir $HOME/django_app/static")
    commands.append("mkdir $HOME/django_app/templates")
    commands.append("sudo ln -s $HOME/django_app/static /opt/django")
    #download and set up Nginx configuration. Basically it will listen in port 80 and forward to port 8000 dynamic content
    commands.append("sudo mv /etc/nginx/sites-available/default /etc/nginx/sites-available/default.backup")
    commands += cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/tip/server/etc/nginx/sites-available/default")
    commands.append("sudo cp default /etc/nginx/sites-available/default")
    return commands


#list of cmds to execute
commands = cmds.install_pip 
commands += cmds.pip_install("virtualenv") 
commands += cmds.install_nginx 
commands += cmds.createVirtualEnv(env) 
commands += cmds.installPackageInVirtualEnv(env, package="django", verification_command="django-admin.py --version")
commands += cmds.installPackageInVirtualEnv(env, package="gunicorn")
commands += cmds.executeInVirtualEnv(env, cmds.create_django_project(project_name, dir_name=env + os.path.sep))
commands += configureNginx()

#setting up Django app
commands += cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/tip/django_app/settings.py", "/home/ubuntu/django_app/app/settings.py")
commands += cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/tip/django_app/urls.py", 
                      django_app_dir + "/app/urls.py")
commands += cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/1587f68db41e/templates/test_static.html",
                      django_app_dir + "/templates/test_static.html")
commands += cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/tip/static/django.png",
                      django_app_dir + "/static")


#setting up Upstart to automatically launch Django application 
commands += cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/tip/run.sh",
                      "/home/ubuntu/django_app/run.sh")
commands += cmds.chmod("a+x", django_app_dir + "/run.sh")
commands += cmds.sudo(cmds.wget("https://bitbucket.org/deccico/django_gunicorn/raw/tip/server/etc/init/django_app.conf",
                      "/etc/init/django_app.conf"))
