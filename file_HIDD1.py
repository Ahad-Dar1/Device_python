import hashlib
import os
import random
import uuid 

Device_key_HIDD1=""

def write_HIDD1(Device_name,data_to_write):
    with open(Device_name, 'w') as file:
        file.write(data_to_write)
    global Device_key_HIDD1
    Device_key_HIDD1=data_to_write

def read_HIDD1(Device_name):
    with open(Device_name, 'r') as file:
        data = file.read()
    global Device_key_HIDD1
    Device_key_HIDD1 = data
    #print(data)

def check_or_generate_hash(Device_name):

    file_path = Device_name
    if os.path.exists(file_path):
        print(f"The file '{file_path}' exists.")
        read_HIDD1(Device_name)
    else:
        print(f"The file '{file_path}' does not exist.")
        mac=':'.join(['{:02x}'.format((uuid.getnode()>>elements) & 0xff) for elements in range(2,8,2)])
        randomdata=random.uniform(10000,100000)
        mac_random=str(randomdata)+mac
        print(mac_random)
        mac_random_encoded=mac_random.encode('utf-8')

        # Create a SHA-256 hash object
        sha256_hash = hashlib.sha256()

        # Update the hash object with the data
        sha256_hash.update(mac_random_encoded)

        # Get the hexadecimal representation of the hash
        hashed_data = sha256_hash.hexdigest()

        write_HIDD1(Device_name,hashed_data)
        print("Global var stored :",Device_key_HIDD1)


