from typing import List
from converter import toCPP
from camera import record
import time
import os

def read_file_return_ints(inputfile):
    with open(inputfile) as f:
        numbers = f.read()
        number_list = numbers.split(" ")
        number_list: List[int] = [int(i) for i in number_list]
        return number_list

def binary_convert(n):
    temp = []

    while (n > 0):
        val = n / 2

        check = val - int(val)

        if (check > 0):
            temp.append("1")
            n = val - 0.5
        else:
            temp.append("0")
            n = val

    while (len(temp) < 6):
        temp.append("0")

    temp = temp[::-1]

    binary = ''.join(temp)

    return binary

def boolean_convert(list):
    bool_list = []
    for i in bin_list:
        temp = []
        for char in i:
            if char == "1":
                temp.append(True)
            else:
                temp.append(False)
        bool_list.append(temp)
    return bool_list


num_list = read_file_return_ints("input.txt")
bin_list = []

for i in num_list:
    i = i % (2 ** 6)
    binary = binary_convert(i)
    if len(binary) != 6:
        diff = abs(6 - len(binary))
        binary = (diff * "0") + binary
    bin_list.append(binary)



times = boolean_convert(bin_list)
print("Converted input numbers to binary!")
print(times)
print("Now generating C++ for Arduino!")
print("Sending C++ code to Arduino!")
toCPP(times)
print("Starting Recording!")
record()
time.sleep(2)
print("Uploading recording to GitHub as output!")
os.system("./uploader.sh")