"""This configuration holds the list of cmds that are going to be applied to a list of ami's. 
This is part of the normal Bellatrix process. The new configuration will be burned into a new ami."""

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


#list of cmds to execute
import lib.cmds

commands = cmds.upgrade_ubuntu \
            + cmds.install_puppet_ubuntu \
            + cmds.changeHostname(amis[0][1]) \
            + cmds.copy_puppet_cfg(puppet_src) \
            + cmds.exec_puppets_agent(puppet_src)

