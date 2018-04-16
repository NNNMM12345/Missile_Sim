import geocoder
import sys
import time
from time import sleep

for i in range(101):
    sys.stdout.write('\r')
    sys.stdout.write("[%-10s] %d%%" % ('='*i, 1*i))
    sys.stdout.flush()
    sleep(0.02)

city_1 = 50
city_2 = 100
city_3 = 200
city_4 = 400
target = "FayCliffNewton"
print("\nThe current time is: ", time.asctime())
g = geocoder.ip('me')
print(g.latlng)
print("\nSign in to launch nuke")
key = str(input("\nEnter launch key :"))
if key == str(23484772):
    print("\nLaunch Initiated!!!")
else:
    print("\nFAILURE!!!")
    raise SystemExit
print("\nThe current target is " + target)
new_target = input("\nEnter new target if desired (leave blank for no change)")
if not new_target:
    target = target
    print("\nThe missile will be positioned to hit " + target)
if new_target:
    print("\nThe missile will be positioned to hit " + new_target)
print("\nLaunching")
time.sleep(5)
print(3)
time.sleep(5)
print(2)
time.sleep(5)
print(1)
print("\nLaunched")
print("\nThe target will be hit with a desired amount of KT")
payload_1 = int(input("\nEnter a payload: "))
if payload_1 == 25:
    print(city_1 - payload_1)

elif payload_1 == 50:
    print(city_2 - payload_1)

elif payload_1 == 75:
    print(city_3 - payload_1)

elif payload_1 == 100:
    print(city_4 - payload_1)

else:
    print("\nPlease select a desired payload")
if not new_target:
    target = target
    print("\nThe city of " + target + " has been hit")
if new_target:
    print("\nThe city of " + new_target + " Has been hit")
print("\nTo order another strike restart the program")
print("\nGoodbye :(")
raise SystemExit 

