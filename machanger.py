import subprocess
#"wlp3s0"
interface = input("interface > ") 
new_mac = input("nueva mac > ")

print("[+] CHANGING MAC ADRESS FOR " + interface + " to " + new_mac)



subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
