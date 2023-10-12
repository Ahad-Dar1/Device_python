import requests
import file_HIDD1
import random_key
import endpoints
import time
import json

def initiate_random(Device_name):
    random_data = {
        "DeviceName": Device_name,
        "DeviceId": file_HIDD1.Device_key_HIDD1
    }
    url=endpoints.SERVER_URL_Rand
    random_string=json.dumps(random_data)
    random_response = requests.post(url, data=random_string, headers={'Content-Type': 'application/json'})
    if random_response.status_code==200:
        random_response_parse=random_response.json()
        # Access and work with the JSON data
        random_number_gen =random_response_parse['randomNum']
        random_key.write_random_number(Device_name,str(random_number_gen))
        return 1
    else:
        return 0
      
def check_device_reg(Device_name):
    #  Define the string you want to send
    registration_data = {
        "DeviceName": Device_name,
        "DeviceId": file_HIDD1.Device_key_HIDD1
    }
    reg_JSON_string=json.dumps(registration_data)
    print("HIDD1 is in this scope as",file_HIDD1.Device_key_HIDD1)
    url=endpoints.SERVER_URL_Reg
    # Send a POST request with the JSON string
    registration_response = requests.post(url, data=reg_JSON_string, headers={'Content-Type': 'application/json'})
    reg_response_parse=registration_response.json()
        # Access and work with the JSON data
    reg_FOUND =reg_response_parse['Found']    # Check the response status code
    print(reg_FOUND)
    if reg_FOUND == '0':
    #Initiate the registration process
        print("Device Not Found")
        for i in range(0,3):
            time.sleep(1)
            checker=initiate_random(Device_name)
            if checker == 1:
                break
            else:
                print("Random Number not received")
    elif reg_FOUND=='1':
        print("Device Found")
        
    else:
        print("Unknown Error")


def verification_client(Device_name):
    KD3=random_key.read_random_number(Device_name)
    verification_data = {
        "DeviceName": Device_name,
        "KD3": KD3
    }
    url=endpoints.SERVER_URL_Verification
    verification_string=json.dumps(verification_data)
    print(verification_string)
    verification_response = requests.post(url, data=verification_string, headers={'Content-Type': 'application/json'})
    print(verification_response.status_code)
    if verification_response.status_code==200:
        print("Device_verified")
        return 1
    else:
        print("Intruder Kicking in or server is down")
        return 0
