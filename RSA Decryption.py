from Crypto.Util.number import inverse, long_to_bytes
import sys
import time
import random

typing_speed = 64 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')




print("=============================")
print("=============HI==============")
print("=============================")
print("-----------------------------")
print("                             ")
slow_type("Made By Samurai # GitHub : iiSamurai")

print("                             ")
p = int(input("Input Your p Number! : "))
print("                             ")

q = int(input("Input Your q Number! : "))
print("                             ")

e = int(input("Input Your e (Encryption) Number! : "))
print("                             ")

ct = int(input("Input Your ct (Cypher Text) Number! : "))

n = p * q

phi = (p-1) * (q-1)

#d for Decryption
d = inverse (e, phi)

solved = pow(ct, d, n)
print("_________________________________________________")
print("                                                 ")
print("The Solution Is : " + str(long_to_bytes(solved)))
print("_________________________________________________")
print("                                                 ")
