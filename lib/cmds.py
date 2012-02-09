""" common utilities, meant to be used as build blocks by configs. 

Please, keep every block independent from the others. 
"""

#CONSTANTS
#http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=422427
apt_prefix = "export PATH=$PATH:/sbin:/usr/sbin:/usr/local/sbin;export TERM=linux;"
cmd = "command"


def changeCommands(cmds, old_value, new_value):
    list = cmds
    for i in range(len(list)):
        list[i] = list[i].replace(old_value, new_value)
    return list

upgrade_ubuntu = [apt_prefix + "sudo apt-get update -y",
                  apt_prefix + "sudo apt-get upgrade -y",
                  apt_prefix + "sudo apt-get check -y",
                  ]

kill_java_python = ["killall python -w -v",
                    "killall java -w -v",
                    ]

clean_home = ["rm -rf $HOME/*;ls $HOME"]

deploy_igniter = ["wget https://s3.amazonaws.com/bamboo-ec2-igniter/igniter.py",
                  "chmod a+x igniter.py;ls -la igniter.py"
                  ]

jdk = "jdk-6u27-linux-x64.bin"
java_dir = "jdk1.6.0_27"
install_jdk_16_27 = [
                     "wget https://s3.amazonaws.com/bamboo-ec2/%s" % jdk,
                     "chmod a+x %s" % jdk,
                     "echo |./%s >out_jdk 2>&1" % jdk,
                     "cat out_jdk",
                     "sudo mkdir -p /opt/java/sdk/",
                     "sudo mv %s /opt/java/sdk/" % java_dir,
                     "/opt/java/sdk/%s/bin/java -version" % java_dir
                     ]

increase_ubuntu_swap =[
                           "sudo dd if=/dev/zero of=/var/swapfile bs=1M count=2048",
                           "sudo chmod 600 /var/swapfile",
                           "sudo mkswap /var/swapfile",
                           "echo /var/swapfile none swap defaults 0 0 | sudo tee -a /etc/fstab",
                           "sudo swapon -a",
                           ]

install_puppet_ubuntu =[
                           apt_prefix + "sudo apt-get install puppet -y -f",
                           "puppet --version"
                           ]

install_git_ubuntu =[
                           apt_prefix + "sudo apt-get install git -y -f",
                           "git --version"
                           ]

def changeHostname(hostname):
    cmds = ["sudo hostname %s" % hostname,
                       "hostname",
                       ]
    return cmds

def exec_puppets_agent(src):
    return  [
             "cd %s && %s/run_puppet_ec2_ubuntu.sh" % (src, src)
             ]

def copy_puppet_cfg(src):
    return [
            "mkdir -p %s" % src,
            {cmd:"scp -o StrictHostKeyChecking=no -i %(key)s -r *.sh Rakefile manifests/ features/ modules/ %(user)s@%(dns)s:" 
             + "%s" % src  
             + " 2>&1 > %(out_tmp)s;let RET=$?;exit $RET"} 
            ]
    
fail_command = ["I want to fail as a command"]


