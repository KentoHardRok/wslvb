# PreReq for this is to add vbox commands to your path
# at this point you have to build the VM yourself with at least one IP address
# that the host can ssh to. Once thats been verified you can add this script to a
# new terminal in windows terminal.


import argparse
import subprocess
import os
import time

parser = argparse.ArgumentParser(description='A WSL without Hyper-V.')
parser.add_argument("-o", "--vm_os", help="The name of the VM OS to be started", default="Manjaro", type=str, )
parser.add_argument("-i", "--vm_ip", help="The host accessible IP of the VM", default="192.168.56.102")
parser.add_argument("-u", "--ssh_user", help="The account used to SSH to the VM", default="tomw", type=str)
args = parser.parse_args()

# First we set the os and IP
vm_os = args.vm_os
vm_ip = args.vm_ip
ssh_user = args.ssh_user
vm_status = subprocess.check_output('vboxmanage list runningvms', shell=True)

# just the connection function


def vm_connect():
    os.system('ssh ' + ssh_user + '@' + vm_ip)


# If the vm is already running go ahead and connect else start the vm in headless mode
# wait for it to finish starting (30s) then connect.
if vm_os in str(vm_status):
    vm_connect()
else:
    subprocess.call('vboxmanage startvm ' + vm_os + ' --type headless')
    time.sleep(30)
    vm_connect()
