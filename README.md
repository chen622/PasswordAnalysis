# PasswordAnalysis
> This project is only used to study the principles of password guessing.

This is a project to analyze the password of CSDN and Yahoo. It use four analysis methods:
1. Pattern. It used to count the pattern of number, letter and symbol. Code is in `/PasswordPattern` folder.
2. Date. It used to count the date format. The code is in `/Data` folder.
3. Keyboard. It used to count the char which arranged in adjacent positions in the keyboard. Code is in `/KeyboardMap` folder.
4. Word&Pinyin. It used to count the word and Pinyin. The Code is in `/EnglishPinyinDetection` folder.

Based on the analysis, we design a password guesser `pcfg.py`, which will generate passwords with probability of occurrence.