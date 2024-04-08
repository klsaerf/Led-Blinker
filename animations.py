import random

top_row = [x + "0" for x in "23456"]
top_left = ["1" + x for x in "12345"]
top_right = ["7" + x for x in "12345"]
middle_row = [x + "6" for x in "23456"]
bot_left = ["1" + x for x in "789ab"]
bot_right = ["7" + x for x in "789ab"]
bot_row = [x + "c" for x in "23456"]

numbers = {
    1: [top_right, bot_right],
    2: [top_row, top_right, middle_row, bot_left, bot_row],
    3: [top_row, top_right, middle_row, bot_right, bot_row],
    4: [top_left, top_right, middle_row, bot_right],
    5: [top_row, top_left, middle_row, bot_right, bot_row],
    6: [top_row, top_left, middle_row, bot_left, bot_right, bot_row]
}

animation = [
    ["46"],
    ["36", "56"],
    ["26", "66"],
    [],
    ["15", "75", "17", "77"],
    ["14", "74", "18", "78"],
    ["13", "73", "40", "19", "79", "4c"],
    ["12", "72", "30", "50", "1a", "7a", "3c", "5c"],
    ["11", "71", "20", "60", "1b", "7b", "2c", "6c"],
]

reverse_animation = animation[::-1]

upside_animation = []
for col in "0123456789abc":
    r = []
    for row in "1234567":
        r.append(row + col)
    upside_animation.append(r)

downside_animation = upside_animation[::-1]

brightness = "\n\"e3f"
dimness = "e30"
wait_short = "w0009"
wait_long = "w0021"
select_all = "a"
terminate = "x\""


def animate_1():
    command = brightness
    for part in animation:
        flag = False
        for line in part:
            for segment in numbers[1]:
                for index in segment:
                    if line == index:
                        command += "s" + index
                        flag = True
        if flag:
            command += wait_short
    command = command[:-5]
    command += wait_long
    command += terminate
    return command


def animate_2():
    command = brightness
    for part in reverse_animation:
        flag = False
        for line in part:
            for segment in numbers[2]:
                for index in segment:
                    if line == index:
                        command += "s" + index
                        flag = True
        if flag:
            command += wait_short
    command = command[:-5]
    command += wait_long
    command += terminate
    return command


def animate_3():
    command = brightness
    for segment in numbers[3]:
        for index in segment:
            command += "s" + index
    command += wait_long
    command += dimness
    command += select_all
    command += wait_long
    command += terminate
    return command


def animate_4():
    command = brightness
    for part in upside_animation:
        flag = False
        for line in part:
            for segment in numbers[4]:
                for index in segment:
                    if line == index:
                        command += "s" + index
                        flag = True
        if flag:
            command += wait_short
    command = command[:-5]
    command += wait_long
    command += terminate
    return command



def animate_5():
    command = brightness
    for part in downside_animation:
        flag = False
        for line in part:
            for segment in numbers[5]:
                for index in segment:
                    if line == index:
                        command += "s" + index
                        flag = True
        if flag:
            command += wait_short
    command = command[:-5]
    command += wait_long
    command += terminate
    return command


def animate_6():
    index_of_6 = []
    for line in numbers[6]:
        for index in line:
            index_of_6.append(index)

    random.shuffle(index_of_6)
    counter = 0
    command = brightness
    for i in range(1, 31):
        counter += 1
        command += "s" + index_of_6[i - 1]
        if counter == 10 or counter == 20:
            command += wait_short
    command += wait_long
    command += terminate
    return command
