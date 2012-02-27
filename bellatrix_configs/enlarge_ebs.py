'''
Set of commands to enlarge an EC2 EBS image
'''

#list of ami's to process with the below cmds
amis = [
       ["ami-fd589594",  "ubuntu1104-ff36-mysql51-x64"],
       ]

#this values will be applied to the instance that is going to be configured with bellatrix bewitch_ami
#once you have your ami configured, then you can launch it with a different configuration 
key_name = "key"          #Name of the key-pair name that will be applied to your instance. 
security_groups = "default"   #comma separated list (with no spaces) of the security groups that will be applied to the new instance. It can be only one. Usually is. e.g. mysecurity_group
instance_type = "t1.micro"          #type of instance that will be used for applying the configuration. Usually t1.micro should be enough. List of codes here: http://aws.amazon.com/ec2/instance-types for more

#------------------------------------------------------------------------------------------------
from bellatrix_configs.lib import cmds


commands = cmds.resize_image()

