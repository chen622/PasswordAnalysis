import pymysql
import re
from tqdm import tqdm
import pickle


class TreeNode:
    def __init__(self):
        # 26叉树，字典树
        self.nodes = dict()

    def insert(self, word: str):
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TreeNode()
            curr = curr.nodes[char]

    def search(self, word: str):
        curr = self
        for char in range(len(word)):
            if word[char] not in curr.nodes:
                if char >= 3 and len(word) - char >= 3:
                    return self.search(word[char:])
                return False
            curr = curr.nodes[word[char]]
        return True


class PasswordGuess:
    def __init__(self):
        self.usr_list = []
        self.word_list = []
        self.word_tree = TreeNode()
        with open('./pinyin.txt', 'r') as file:
            self.spell = file.read().split('\n')
        self.spell = sorted(self.spell, key=lambda i: len(i), reverse=True)

    def word_in(self):
        # 导入英文单词数据库
        db = pymysql.connect("localhost", "root", "19971128", "english_words")
        cursor = db.cursor()
        sql = 'select * from english_words;'
        cursor.execute(sql)
        datas = cursor.fetchall()
        for word in datas:
            word = word[1]
            self.word_list.append(word)
            self.word_tree.insert(word)
        db.close()

    def type_classify(self, word):
        word = list(filter(str.isalpha, word))
        if len(word) <= 2:
            return None
        word = "".join(word)
        word_backup = word
        word.lower()
        word_len = len(word) + 1
        while len(word) < word_len:
            word_len = len(word)
            for pinyin in self.spell:
                if len(pinyin) >= 2:
                    if re.match(pinyin, word):
                        word = word[len(pinyin):]
                        break
            if len(word) == 0:
                return "Pinyin"
        word = word_backup
        if self.word_tree.search(word):
            return "English"
        elif word[0] == 'i' and self.word_tree.search(word[1:]):
            return "English"
        return None

    def usr_in(self):
        # 导入csdn密码数据
        with open('./www.csdn.net.sql', 'r', encoding='iso8859-1') as string:
            uft_str = string.readlines()
        for usr in tqdm(uft_str, total=len(uft_str), desc="计算中："):
            usr = usr[:-1]
            usr = usr.split(' # ')
            usr_mes = {
                "name": usr[0],
                "password": usr[1],
                "email": usr[2],
                "type": self.type_classify(usr[1])
            }
            self.usr_list.append(usr_mes)


if __name__ == "__main__":
    app = PasswordGuess()
    app.word_in()
    app.usr_in()
    with open('./letter_analyze.txt', 'w') as file:
        file.write(str(app.usr_list))
    # print(app.usr_list)
    # print(app.type_classify("shuziluoji"))


