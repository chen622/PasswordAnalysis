# coding=utf-8
import time
import pandas as pd

def LDS_map(dataset_param):
    result = {}
    j = 0
    time_start = time.time()

    for data in dataset_param:  # 遍历全部密码
        res_str = ''
        last_index = ''
        char_num = 0
        for char in data:  # 遍历密码字符串
            if char >= '0' and char <= '9':
                char_index = 'D'
            elif (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
                char_index  = 'L'
            else:
                char_index = 'S'
            if char_index != last_index:
                if char_num != 0:
                    res_str = res_str + last_index + str(char_num)
                last_index = char_index
                char_num = 1
            else:
                char_num += 1
        res_str = res_str + last_index + str(char_num)

        if res_str in result:
            result[res_str] += 1
        else:
            result[res_str] = 1
        j += 1
        if j % 100000 == 0:
            time_end = time.time()
            percent = j / len(dataset_param) * 100
            print(f'Analyze 10W lines within {(time_end - time_start):.1f} seconds! {percent:.2f}%')
            time_start = time_end
    return result
if __name__ == "__main__":
    # with open('www.csdn.net.sql', 'r+', encoding='utf-8', errors='ignore') as data_file:
    with open('plaintxt_yahoo.txt', 'r+', encoding='utf-8', errors='ignore') as data_file:
        dataset = []
        line = data_file.readline()
        i = 0
        while line:
            # str_s = line.split(' # ')
            str_s = line.split(':', 2)
            if len(str_s) == 3:
                # dataset.append(str_s[1])
                dataset.append(str_s[2])
            else:
                print(f'error data: {line}')
            i += 1
            if i % 1000000 == 0:
                print(f'Load {len(dataset)} lines!')
                # break
            line = data_file.readline()
        print(f'Load file({len(dataset)} lines) complete!')
    result_map = LDS_map(dataset)

    result_list = result_map.items()
    order_list = sorted(result_list, key=lambda item: item[1], reverse=True)
    with open(('result_small_yahoo.txt' ), 'w', encoding='utf-8',
              errors='ignore') as out_file:
        i = 0
        for item in order_list:
            percent = item[1] / len(dataset) * 100
            out_file.write(f'{item[0]} {item[1]} {percent:.4f}%\n')
            i += 1
            if i % 1000:
                out_file.flush()