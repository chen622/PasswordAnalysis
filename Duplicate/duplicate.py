#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import time

if __name__ == "__main__":
    with open('../www.csdn.net.sql', 'r+', encoding='utf-8', errors='ignore') as data_file:
        dataset = {}
        line = data_file.readline()
        i = 0
        while line:
            str_s = line.split(' # ')
            if len(str_s) == 3:
                if str_s[1] in dataset.keys():
                    dataset[str_s[1]] += 1
                else:
                    dataset[str_s[1]] = 1
            else:
                print(f'error data: {line}')
            i += 1
            if i % 1000000 == 0:
                print(f'Load {len(dataset)} lines!')
                # break
            line = data_file.readline()
        print(f'Load file({len(dataset)} lines) complete!')
    result_list = dataset.items()
    order_list = sorted(result_list, key=lambda item: item[1], reverse=True)
    with open('result_duplicate.dat', 'w', encoding='utf-8',
              errors='ignore') as out_file:
        j = 0
        for item in order_list:
            if item[0].isdigit():
                out_file.write(f'{item[0]} {item[1]} {(item[1] / i):.6f} {len(item[0])}\n')
                j += 1
                if j % 1000:
                    out_file.flush()
