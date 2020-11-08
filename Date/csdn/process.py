# -*- coding: utf-8 -*-
import time
import regex
import json


"""
save result
"""
def save_to_file():
    f_save=open("./result/eight_digit_data.txt",'w')
    f_save.write(json.dumps(eight_digit_data))
    f_save.close()

    f_save=open("./result/six_digit_data.txt",'w')
    f_save.write(json.dumps(six_digit_data))
    f_save.close()

    f_save=open("./result/eight_digit_2_segemetation_data.txt",'w')
    f_save.write(json.dumps(eight_digit_2_segmentation_data))
    f_save.close()

    f_save=open("./result/six_digit_2_segemetation_data.txt",'w')
    f_save.write(json.dumps(six_digit_2_segmentation_data))
    f_save.close()


def get_pw(string):
    return (string.split(" "))[2]

def parse(pw):
    # 匹配顺序8数字、6数字、8数字带2分隔符、6数字带2分隔符
    if eight_digit(pw):
        return
    if six_digit(pw):
        return
    if eight_digit_2_segmentation(pw):
        return
    if six_digit_2_segmentation(pw):
        return
    
def eight_digit(pw):
    valid_pw_num=0
    pattern=r"\d{8}"
    tmp_list=regex.findall(pattern,pw,overlapped=True)
    for i in tmp_list:
        try:
            if time.strptime(i,"%Y%m%d"):
                eight_digit_data.append(i)
                valid_pw_num=valid_pw_num+1
        except:
            continue
    return valid_pw_num

def six_digit(pw):
    valid_pw_num=0
    pattern=r"\d{6}"
    tmp_list=regex.findall(pattern,pw,overlapped=True)
    for i in tmp_list:
        month=int(i[2:4])
        day=int(i[4:6])
        if(month>0 and month<=12 and day>0 and day<=31):
            six_digit_data.append(i)
            valid_pw_num=valid_pw_num+1
    return valid_pw_num
            
def eight_digit_2_segmentation(pw):
    valid_pw_num=0
    pattern=r"\d{4}[\W_]\d{2}[\W_]\d{2}"
    tmp_list=regex.findall(pattern,pw,overlapped=True)
    for i in tmp_list:
        data=""
        data=data+i[0:4]+i[5:7]+i[8:10]
        try:
            if time.strptime(data,"%Y%m%d"):
                eight_digit_2_segmentation_data.append(i)
                valid_pw_num=valid_pw_num+1
        except:
            continue
    return valid_pw_num

def six_digit_2_segmentation(pw):
    valid_pw_num=0
    pattern=r"\d{2}[\W_]\d{2}[\W_]\d{2}"
    tmp_list=regex.findall(pattern,pw,overlapped=True)
    for i in tmp_list:
        # year=i[0:2]
        month=int(i[3:5])
        day=int(i[6:8])
        if(day>0 and day<=31 and month>0 and month<=12):
            six_digit_2_segmentation_data.append(i)
            valid_pw_num=valid_pw_num+1
    return valid_pw_num



# 获取密码的个数
file_name="../data/www.csdn.net.sql"
f=open(file_name)
tmp=f.readlines()
line_total=len(tmp)
print("total line:",line_total)
f.close()

# process
f=open(file_name)
# 存放8位数字密码
eight_digit_data=[]
# 存放6位数字密码
six_digit_data=[]
# 存放8位数字带分割符的密码
eight_digit_2_segmentation_data=[]
# 存放6位数字带分割符的密码
six_digit_2_segmentation_data=[]

line_current=0
while 1:
    line=f.readline()
    if not line:
        print("break")
        break
    password=get_pw(line)
    parse(password)

    # 显示进度
    if line_current % 10000 == 0:
        print("进度:",line_current/line_total)
    line_current+=1
f.close()
save_to_file()
