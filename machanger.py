import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()

    parser.add_option("-i","--interface", dest="interface", help="interface to change its MAC address")
    parser.add_option("-m","--mac", dest="new_mac", help="new mac address")

    (options, arguments) = parser.parse_args()
    if not options.interface:
        #codigo para el error
        parser.error("[-] por fa pon la interfaz bien meco")
    elif not options.new_mac:
        #codigo para error
        parser.error("[-] por fa pon la mac address bien meco")
    return options
        
def  change_mac(interface, new_mac):
        print("[+] CHANGING MAC ADRESS FOR " + interface + " to " + new_mac)

        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
        subprocess.call(["ifconfig", interface, "up"])


#"wlp3s0"


#interface = options.interface
#new_mac = options.new_mac
options = get_arguments()
change_mac(options.interface, options.new_mac)

