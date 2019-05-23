#!/bin/python3
import random
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*'
length=int(input('Enter password length?'))
num_pass=int(input('Enter numbers of passwords to be generated:'))
for p in range(num_pass):
  password=''
  for t in range(length):
    password+=random.choice(chars)
  print(password)