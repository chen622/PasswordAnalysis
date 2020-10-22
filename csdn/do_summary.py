# -*- coding: utf-8 -*-
import json

f=open("./result/eight_digit_data.txt","r")
eight_digit_data=json.loads(f.read())
f.close()

f=open("./result/six_digit_data.txt","r")
six_digit_data=json.loads(f.read())
f.close()

f=open("./result/eight_digit_2_segemetation_data.txt","r")
eight_digit_2_segemetation_data=json.loads(f.read())
f.close()

f=open("./result/six_digit_2_segemetation_data.txt","r")
six_digit_2_segemetation_data=json.loads(f.read())
f.close()

print("8个数字:",len(eight_digit_data))
print("8个数字2个分隔符:",len(eight_digit_2_segemetation_data))
print("6个数字:",len(six_digit_data))
print("6个数字2个分隔符:",len(six_digit_2_segemetation_data))
