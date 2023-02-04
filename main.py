
import os
import time
from elevate import elevate

# to be sure that the wifi_name is 'WiFi'
def get_info():
    interfaces = os.system("netsh interface show interface")
    print(interfaces)
    return interfaces


def main(wifi_name='WiFi'):
    # to run as Administrator
    elevate(show_console=False)
    # turn WiFi adapter off
    os.system(f"netsh interface set interface {wifi_name} disabled")
    # wait for 2 seconds
    time.sleep(2)
    # turn WiFi adapter on
    os.system(f"netsh interface set interface {wifi_name} enabled")


if __name__ == '__main__':
    main()