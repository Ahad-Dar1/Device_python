import os

def write_random_number(Device_name,data_to_write):
    Device_name1=Device_name+"_random"
    with open(Device_name1, 'w') as file:
        file.write(data_to_write)


def read_random_number(Device_name):
    Device_name1=Device_name+"_random"
    with open(Device_name1, 'r') as file:
        data = file.read()
    return data
    print(data)
'''
def check_random_number(Device_name):
    
 #   file_path = Device_name
  #  if os.path.exists(file_path):
        print(f"The file '{file_path}' exists.")
        read_random_number(Device_name)
        return 1
    else:
        return 0'''