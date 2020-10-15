# coding=utf-8

key_map = [
    # line 1
    [['`', '~'], ['-1'], ['1', '!'], ['-1'], ['2', '@'], ['-1'], ['3', '#'], ['-1'], ['4', '$'], ['-1'], ['5', '%'],
     ['-1'], ['6', '^'], ['-1'], ['7', '&'], ['-1'], ['8', '*'], ['-1'],
     ['9', '('], ['-1'], ['0', ')'], ['-1'], ['-', '_'], ['-1'], ['=', '+'], ['-1']],
    # line 2
    [['-1'], ['-1'], ['-1'], ['q'], ['-1'], ['w'], ['-1'], ['e'], ['-1'], ['r'], ['-1'], ['t'], ['-1'], ['y'],
     ['-1'], ['u'], ['-1'], ['i'], ['-1'], ['o'], ['-1'], ['p'], ['-1'], ['[', '{'], ['-1'], [']', '}'], ['-1'],
     ['\\', '|'], ['-1'], ],
    # line 3
    [['-1'], ['-1'], ['-1'], ['-1'], ['a'], ['-1'], ['s'], ['-1'], ['d'], ['-1'], ['f'], ['-1'], ['g'], ['-1'],
     ['h'], ['-1'], ['j'], ['-1'], ['k'], ['-1'], ['l'], ['-1'], [';', ':'], ['-1'], ['\'', '"'], ['-1'], ],
    # line 4
    [['-1'], ['-1'], ['-1'], ['-1'], ['-1'], ['z'], ['-1'], ['x'], ['-1'], ['c'], ['-1'], ['v'], ['-1'], ['b'],
     ['-1'], ['n'], ['-1'], ['m'], ['-1'], [',', '<'], ['-1'], ['.', '>'], ['-1'], ['/', '?'], ['-1'], ]
]


def keyboard_map(dataset):
    print_map()
    result = {}
    i = 0
    for data in dataset:
        aim_str = ''
        last_index = (-2, -2)
        for char in data:
            x, y = find_index(char)
            if (x, y) != (-2, -2):
                distance_x = 0.5 * (x - last_index[0])
                distance_y = y - last_index[1]
                distance = distance_x * distance_x + distance_y * distance_y
                if distance < 2:
                    aim_str += char
                else:
                    if len(aim_str) >= 3:
                        if aim_str in result:
                            result[aim_str] += 1
                        else:
                            result[aim_str] = 1
                    aim_str = char
            last_index = (x, y)
        if len(aim_str) >= 3:
            if aim_str in result:
                result[aim_str] += 1
            else:
                result[aim_str] = 1
        i += 1
        if i % 100000 == 0:
            print(f'Analyze data {i}/{len(dataset)}')
    return result


def find_index(char):
    for y in range(len(key_map)):
        for x in range(len(key_map[y])):
            for symbol in key_map[y][x]:
                if symbol == char:
                    return x, y
    return -2, -2


def print_map():
    print('The key map which I used is like this:')
    for y in range(len(key_map)):
        for x in range(len(key_map[y])):
            if key_map[y][x][0] == '-1':
                print(' ', end='')
            else:
                print(key_map[y][x][0], end='')
        print()


if __name__ == "__main__":
    data_file = open('../www.csdn.net.sql', 'r+', encoding='utf-8', errors='ignore')
    dataset = []
    line = data_file.readline()
    i = 0
    while line:
        str_s = line.split(' # ')
        if len(str_s) == 3:
            dataset.append(str_s[1])
        else:
            print(f'error data: {line}')
        i += 1
        if i % 100000 == 0:
            print(f'Load file({len(dataset)} lines)!')
            break
        line = data_file.readline()
    print(f'Load file({len(dataset)} lines) complete!')
    print(keyboard_map(dataset))
