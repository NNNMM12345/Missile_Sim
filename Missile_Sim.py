import geocoder
import sys
import time
from time import sleep
import datetime

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
print("\nThe current time is: ", datetime.datetime.now())
g = geocoder.ip('me')
print(g.latlng)
print("\nSign in to launch missile")
key = str(input("\nEnter launch key :"))
if key == str(23484772):
    print("Welcome")
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
for i in range(10, 0, -1):
    time.sleep(3)
    print(i)
print("\nLaunched")
print("\nThe target will be hit with a desired amount of KT")
payload_1 = int(input("\nEnter a payload: "))
print("Traveling...")
for i in range(15, 0, -1):
    time.sleep(3)
    print(i)
if payload_1 == 25:
    print(city_1 - payload_1)

elif payload_1 == 50:
    print(city_2 - payload_1)

elif payload_1 == 75:
    print(city_3 - payload_1)

elif payload_1 == 100:
    print(city_4 - payload_1)

if payload_1 > 100:
    print("\nPlease select a desired payload and try again")
    raise SystemExit
if not new_target:
    target = target
    print("\nThe city of " + target + " has been hit")
if new_target:
    print("\nThe city of " + new_target + " Has been hit")
print("\nTo order another strike enter the correct keyword")
no = input()
if no == "yes":
    print("\nWould you like to order another strike")
    strike = input()
else:
    raise SystemExit
if strike == "yes":
    pass
else:
    raise SystemExit
target_2 = "Pythonabad"
print("\nThe next target to be hit is " + target_2)
key = str(input("\nEnter launch key again: "))
if key == str(23484772):
    print("\nLaunch Initiated!!!")
else:
    print("\nFAILURE!!!")
    raise SystemExit
new_target_2 = input("\nEnter new target if desired (leave blank for no change)")
if not new_target_2:
    target_2 = target_2
    print("\nThe missile will be positioned to hit " + target_2)
if new_target_2:
    print("\nThe missile will be positioned to hit " + new_target_2)
print("\nLaunching...")
for i in range(10, 0, -1):
    time.sleep(3)
    print(i)
print("\nLaunched")
print("\nThe target will be hit with a desired amount of KT")
payload_1 = int(input("\nEnter a payload: "))
print("Traveling...")
for i in range(15, 0, -1):
    time.sleep(3)
    print(i)
if payload_1 == 25:
    print(city_1 - payload_1)

elif payload_1 == 50:
    print(city_2 - payload_1)

elif payload_1 == 75:
    print(city_3 - payload_1)

elif payload_1 == 100:
    print(city_4 - payload_1)

if payload_1 > 100:
    print("\nPlease select a desired payload and try again")
    raise SystemExit
if not new_target_2:
    target_2 = target_2
    print("\nThe city of " + target_2 + " has been hit")
if new_target:
    print("\nThe city of " + new_target_2 + " Has been hit")
print("\nTo order another strike restart the program")
print("\nIf you would like to launch other types of missiles call +372 428-553-5758")
print("\nGoodbye")
raise SystemExit
