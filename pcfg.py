# MIT License
#
# Copyright (c) 2020 UCAS Web Security Course
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

from tqdm import tqdm
import itertools
import gc


class PCFG:
    def loading(self):
        with open('./EnglishPinyinDetection/top1000.txt', 'r') as file:
            letter = file.readlines()[:-1]
        with open('./KeyboardMap/result_big_csdn_char.dat', 'r') as file:
            tmp = file.readlines()[:1000]
            letter = letter + tmp
        letter = [line[:-1].split(' ') for line in letter]
        self.letter = {}
        for line in letter:
            if int(line[3]) not in self.letter:
                self.letter[int(line[3])] = []
            self.letter[int(line[3])].append([line[0], float(line[2])])
        with open('./KeyboardMap/result_big_csdn_number.dat', 'r') as file:
            number = file.readlines()[:1000]
        number = [line[:-1].split(' ') for line in number]
        self.number = {}
        for line in number:
            if int(line[3]) not in self.number:
                self.number[int(line[3])] = []
            self.number[int(line[3])].append([line[0], float(line[2])])
        with open('./result_small_csdn.txt', 'r') as file:
            rules = file.readlines()[:80]
        rules = [line.split(' ') for line in rules]
        self.rules = []
        for rule in rules:
            p = float(rule[2][:-2]) / 100
            rule = rule[0]
            single = []
            i = 0
            while i < len(rule):
                if rule[i] == "L" or rule[i] == "D" or rule[i] == "S":
                    length = 1
                    while i + length < len(rule) and (rule[i + length] != "L" and rule[i + length] != "D" and rule[i + length] != "S"):
                        length = length + 1
                    single.append(rule[i:i + length])
                    i = i + length
                else:
                    i = i + 1
            self.rules.append([single, p])
        self.char = '~`!@#$%^&*()_+-=[]{}|;:"\',./<>?'

    def merge(self):
        res = []
        for rule in tqdm(self.rules):
            try:
                ret = self.digui(rule[0])
            except:
                continue

            ret = [[line[0], line[1] * rule[1]] for line in ret]
            res = res + ret
            del ret
            gc.collect()
        res.sort(key=lambda x:x[1], reverse=True)
        return res[:1000]

    def digui(self, rule):
        if len(rule) > 1:
            string = self.digui(rule[1:])
            res = []
            key = rule[0][0]
            val = int(rule[0][1:])
            tmp = []
            if key == "L":
                tmp = self.letter[val]
            elif key == "D":
                tmp = self.number[val]
            elif key == "S":
                tmp = [[i, 1] for i in itertools.product(self.char, repeat=val)]
            for line_left in tmp:
                for line_right in string:
                    res.append([line_left[0] + line_right[0], line_left[1] * line_right[1]])
            return res
        else:
            key = rule[0][0]
            val = int(rule[0][1:])
            if key == "L":
                return self.letter[val]
            elif key == "D":
                return self.number[val]
            elif key == "S":
                return [[i, 1] for i in itertools.product(self.char, repeat=val)]
            else:
                return []


if __name__ == "__main__":
    app = PCFG()
    app.loading()
    res = app.merge()
    with open('./password_dict.txt', 'w') as file:
        for password in res:
            file.write(str(password[0]) + ' ' + str(password[1]) + '\n')


