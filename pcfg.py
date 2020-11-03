from tqdm import tqdm
import itertools
import gc


class PCFG:
    def loading(self):
        with open('./EnglishPinyinDetection/top1000.txt', 'r') as file:
            letter = file.readlines()[:-1]
        with open('./KeyboardMap/result_big_csdn_char.dat', 'r') as file:
            tmp = file.readlines()[:5000]
            letter = letter + tmp
        letter = [line[:-1].split(' ') for line in letter]
        self.letter = {}
        self.letter[1] = [chr(i) for i in range(97, 123)]
        for line in letter:
            if int(line[3]) not in self.letter:
                self.letter[int(line[3])] = []
            self.letter[int(line[3])].append(line[0])
        with open('./KeyboardMap/result_big_csdn_number.dat', 'r') as file:
            number = file.readlines()[:5000]
        number = [line[:-1].split(' ') for line in number]
        self.number = {}
        self.number[1] = [str(i) for i in range(10)]
        self.number[2] = [str(i) for i in range(10, 100)]
        for line in number:
            if int(line[3]) not in self.number:
                self.number[int(line[3])] = []
            self.number[int(line[3])].append(line[0])
        with open('./result_small_csdn.txt', 'r') as file:
            rules = file.readlines()[:80]
        rules = [line.split(' ')[0] for line in rules]
        self.rules = []
        for rule in rules:
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
            self.rules.append(single)
        self.char = '~`!@#$%^&*()_+-=[]{}|;:"\',./<>?'

    def merge(self):
        for rule in tqdm(self.rules):
            try:
                ret = self.digui(rule)
            except:
                continue
            with open('./password_dict.txt', 'a') as file:
                for password in ret:
                    file.write(password + '\n')
            del ret
            gc.collect()

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
                tmp = [i for i in itertools.product(self.char, repeat=val)]
            for line_left in tmp:
                for line_right in string:
                    res.append(line_left + line_right)
            return res
        else:
            key = rule[0][0]
            val = int(rule[0][1:])
            if key == "L":
                return self.letter[val]
            elif key == "D":
                return self.number[val]
            elif key == "S":
                return [i for i in itertools.product(self.char, repeat=val)]
            else:
                return []


if __name__ == "__main__":
    app = PCFG()
    app.loading()
    app.merge()


