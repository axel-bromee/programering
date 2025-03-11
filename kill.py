import os
import time

print("is your target alive")

x=input()

if x == "yes":
    os.system("start \"\" https://rentahitman.com/")
    print("misson failed will get them next time")


elif  x == "no":
    print("misson complete")
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("self destruct")
    time.sleep(0.5)
    print("booooooom")
    os.system('boom.png')
