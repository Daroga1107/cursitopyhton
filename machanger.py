import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i","--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="new mac address")

    return  parser.parse_args()

def  change_mac(interface, new_mac):
        print("[+] CHANGING MAC ADRESS FOR " + interface + " to " + new_mac)

        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])


#"wlp3s0"


#interface = options.interface
#new_mac = options.new_mac
(options, arguments ) = get_arguments()
change_mac(options.interface, options.new_mac)

