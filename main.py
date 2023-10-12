import file_HIDD1
import http_client
import wifi_connect
import time

#Global variable in main
One_time_POST=False
Device_name="Ahad_a66"
ssid = "SiiconNexusStorm"
password = "embedded123S"

#Pass 0 if auth failed,1 if Connected and None if Network is Unreachable
test=wifi_connect.connect_to_wifi(ssid, password)
if test==1:
    print(f"Connected to {ssid}")
elif test==0:
    print(f"Authentication Failed to {ssid}")
else:
    print("Network Unreachable")
if test==1:
    file_HIDD1.check_or_generate_hash(Device_name)
while(1):
    while not One_time_POST:
        One_time_POST=True
        http_client.check_device_reg(Device_name)
    time.sleep(10)
    verified=http_client.verification_client(Device_name)
    if verified==0:
        One_time_POST=False
    elif verified==1:
        One_time_POST=True
        #This will halt the inner while() loop



