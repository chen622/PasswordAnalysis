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


"""
格式：
类别 频数 频率 位数
"""

csdn_passwd_sum=6428632
yahoo_passwd_sum=453493

print("8个数字:",len(eight_digit_data))
print("8个数字2个分隔符:",len(eight_digit_2_segemetation_data))
print("6个数字:",len(six_digit_data))
print("6个数字2个分隔符:",len(six_digit_2_segemetation_data))

f=open("./result/summary.txt","w")
f.writelines("8个数字"+" "+str(len(eight_digit_data))+" "+str(len(eight_digit_data)/csdn_passwd_sum)+"\n")
f.writelines("8个数字和2个分隔符"+" "+str(len(eight_digit_2_segemetation_data))+" "+str(len(eight_digit_2_segemetation_data)/csdn_passwd_sum)+"\n")
f.writelines("6个数字"+" "+str(len(six_digit_data))+" "+str(len(six_digit_data)/csdn_passwd_sum)+"\n")
f.writelines("6个数字和2个分隔符"+" "+str(len(six_digit_2_segemetation_data))+" "+str(len(six_digit_2_segemetation_data)/csdn_passwd_sum)+"\n")
f.close()
