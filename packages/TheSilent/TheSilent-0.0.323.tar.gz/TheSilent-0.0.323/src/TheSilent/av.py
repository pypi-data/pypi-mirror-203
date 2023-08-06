import os
from TheSilent.clear import clear

CYAN = "\033[1;36m"
RED = "\033[1;31m"


def av(my_dir):
    # av escape includes anti-debugging strings
    anti_vm_hex = ["564d5868"]
    anti_debug_strings = ["checkremotedebugger", "isdebuggerpresent"]
    anti_vm_strings = ["vm", "virtual"]
    ransomware_strings = ["bitcoin", "btc", "encyrpt", "files", ".onion", "tor"]

    malware_list = []

    clear()

    for path, directories, files in os.walk(my_dir):
        for file in files:
            scan = path + "/" + file

            anti_debug_hits = 0
            anti_vm_hits = 0
            ransomware_hits = 0

            try:
                if os.stat(scan).st_size > 0 and os.stat(scan).st_size < 1000000000:
                    print(CYAN + "checking: " + scan)
                    with open(scan, "rb") as f:
                        # scan for anti-debug strings
                        detected_strings = []
                        skip = False
                        for i in f:
                            result = i.decode(errors="replace").lower()
                            for mal in anti_debug_strings:
                                for detect in detected_strings:
                                    if detect == mal:
                                        skip = True

                                if mal in result and anti_debug_hits < len(anti_debug_strings) and not skip:
                                    anti_debug_hits += 1
                                    detected_strings.append(mal)

                        # scan for anti-vm strings
                        detected_strings = []
                        skip = False
                        for i in f:
                            result = i.decode(errors="replace").lower()
                            for mal in anti_vm_strings:
                                for detect in detected_strings:
                                    if detect == mal:
                                        skip = True

                                if mal in result and anti_vm_hits < len(anti_vm_strings) and not skip:
                                    anti_vm_hits += 1
                                    detected_strings.append(mal)

                        # scan for anti-vm hex
                        detected_strings = []
                        skip = False
                        for i in f:
                            result = i.lower()
                            for mal in anti_vm_hex:
                                for detect in detected_strings:
                                    if detect == mal:
                                        skip = True

                                if mal in result and anti_vm_hits < len(anti_vm_strings) and not skip:
                                    anti_vm_hits += 1
                                    detected_strings.append(mal)
                                    
                        # scan for ransomware strings
                        detected_strings = []
                        skip = False
                        for i in f:
                            result = i.decode(errors="replace").lower()
                            for mal in ransomware_strings:
                                for detect in detected_strings:
                                    if detect == mal:
                                        skip = True
                                        
                                if mal in result and ransomware_hits < len(ransomware_strings) and not skip:
                                    ransomware_hits += 1
                                    detected_strings.append(mal)

                if anti_debug_hits > 0:
                    chance = 100 * (anti_debug_hits / len(anti_debug_strings))
                    if chance > 0:
                        print(RED + f"{chance}% anti-debug: " + scan)
                        malware_list.append(f"{chance}% anti-debug: " + scan)

                if anti_vm_hits > 0:
                    chance = 100 * (anti_vm_hits / int(len(anti_vm_strings) + len(anti_vm_hex)))
                    if chance > 0:
                        print(RED + f"{chance}% anti-vm: " + scan)
                        malware_list.append(f"{chance}% anti-vm: " + scan)

                if ransomware_hits > 0:
                    chance = 100 * (ransomware_hits / len(ransomware_strings))
                    if chance > 50:
                        print(RED + f"{chance}% ransomware: " + scan)
                        malware_list.append(f"{chance}% ransomware: " + scan)

            except PermissionError:
                print(RED + "ERROR! Permission error!")
                continue

            except:
                continue

    clear()

    malware_list = list(set(malware_list))
    malware_list.sort()

    if len(malware_list) > 0:
        for malware in malware_list:
            print(RED + malware)

        print(RED + f"\n{len(malware_list)} possible threats detected!")

    else:
        print(CYAN + "No threats detected!")
