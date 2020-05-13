import subprocess

interface = "wlp3s0"
new_mac="00:22:33:44:77:55"

print("[+] CHANGING MAC ADRESS FOR " + interface + " to " + new_mac)


subprocess.call("ifconfig "+interface + " down",shell=True)
subprocess.call("ifconfig "+interface +" hw ether "+ new_mac,shell=True)
subprocess.call("ifconfig "+interface +" up",shell=True)


