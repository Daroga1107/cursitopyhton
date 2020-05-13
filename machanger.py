import subprocess

subprocess.call("ifconfig wlp3s0 down",shell=True)
subprocess.call("ifconfig wlp3s0 hw ether 00:11:22:33:44:57",shell=True)
subprocess.call("ifconfig wlp3s0 up",shell=True)
