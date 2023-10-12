import pywifi
import time
from pywifi import const
def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]

    iface.scan()
    time.sleep(2)
    scan_results = iface.scan_results()
    
    for result in scan_results:
        if result.ssid == ssid:
            profile = pywifi.Profile()
            profile.ssid = ssid
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = password

            iface.remove_all_network_profiles()
            tmp_profile = iface.add_network_profile(profile)
            iface.connect(tmp_profile)

            time.sleep(5)
            if iface.status() == const.IFACE_CONNECTED:
             #   print(f"Connected to {ssid}")
                return 1
            else:
              #  print(f"Failed to connect to {ssid}")
                return 0
