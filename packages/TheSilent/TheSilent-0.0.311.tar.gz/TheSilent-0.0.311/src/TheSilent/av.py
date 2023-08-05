import os
from TheSilent.clear import clear

CYAN = "\033[1;36m"
RED = "\033[1;31m"


def av(my_dir):
    # av escape includes anti-debugging strings
    av_escape_strings = ["checkremotedebugger", "isdebuggerpresent",
                         "ntqueryinformationprocess", "ntsetinformationthread"]
    ransomware_strings = ["bitcoin", "createfilea", "docx", "fopen", "get", "http/1.1", "ip", "jpeg", "jpg",
                          "language", "movefilew", "pdf", "port", "post", "png", "readfile" "sprintf", "swprintf", "writefile"]

    malware_list = []

    clear()

    for path, directories, files in os.walk(my_dir):
        for file in files:
            scan = path + "/" + file

            av_escape_hits = 0
            ransomware_hits = 0
            skip = False

            try:
                if os.stat(scan).st_size > 0 and os.stat(scan).st_size < 1000000000:
                    print(CYAN + "checking: " + scan)
                    with open(scan, "rb") as f:
                        # scan for av escape strings
                        detected_strings = []
                        for i in f:
                            result = i.decode(errors="replace").lower()
                            for mal in av_escape_strings:
                                for detect in detected_strings:
                                    if detect == mal:
                                        skip = True

                                if mal in result and av_escape_hits < len(av_escape_strings) and not skip:
                                    av_escape_hits += 1
                                    detected_strings.append(mal)

                        # scan for ransomware strings
                        detected_strings = []
                        for i in f:
                            result = i.decode(errors="replace").lower()
                            for mal in ransomware_strings:
                                for detect in detected_strings:
                                    if detect == mal:
                                        skip = True

                                if mal in result and ransomware_hits < len(ransomware_strings) and not skip:
                                    ransomware_hits += 1
                                    detected_strings.append(mal)

                if av_escape_hits > 0:
                    chance = 100 * (av_escape_hits / len(av_escape_strings))
                    if chance > 0:
                        print(RED + f"{chance}% av escape: " + scan)
                        malware_list.append(f"{chance}% av escape: " + scan)

                if ransomware_hits > 0:
                    chance = 100 * (ransomware_hits / len(ransomware_strings))
                    if chance > 0:
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

    else:
        print(CYAN + "No threats detected!")
