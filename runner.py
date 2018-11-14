from simple_device import SimpleDevice
import os

os.system("cls||clear")

print ("Let's create the device, its main state is 'LockedState'")
device = SimpleDevice()

print("\nNow we are changing its state to 'UnlockedState' entering the pin")
device.on_event('pin_entered')

print("\nAnd we finally to move the device back to 'LockedState'")
device.on_event('device_locked')


print("\nYou can always check device state to build more complex scenarios using device.state")
print (device.state)
