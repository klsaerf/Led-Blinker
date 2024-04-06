# ANIMATIONS:
# inside out    - 1
# outside in    - 2
# rapidly blink - 3
# upside down   - 4
# downside up   - 5
# random        - 6

import random


def write(s, file_name):
    file_name.write(s)


# top_row = [x + "0" for x in "23456"]
# top_left = ["1" + x for x in "12345"]
# top_right = ["7" + x for x in "12345"]
# middle_row = [x + "6" for x in "23456"]
# bot_left = ["1" + x for x in "789ab"]
# bot_right = ["7" + x for x in "789ab"]
# bot_row = [x + "c" for x in "23456"]
#
# numbers = {
#     1: [top_right, bot_right],
#     2: [top_row, top_right, middle_row, bot_left, bot_row],
#     3: [top_row, top_right, middle_row, bot_right, bot_row],
#     4: [top_left, top_right, middle_row, bot_right],
#     5: [top_row, top_left, middle_row, bot_right, bot_row],
#     6: [top_row, top_left, middle_row, bot_left, bot_right, bot_row]
# }
#
# animation = [
#     ["46"],
#     ["36", "56"],
#     ["26", "66"],
#     [],
#     ["15", "75", "17", "77"],
#     ["14", "74", "18", "78"],
#     ["13", "73", "40", "19", "79", "4c"],
#     ["12", "72", "30", "50", "1a", "7a", "3c", "5c"],
#     ["11", "71", "20", "60", "1b", "7b", "2c", "6c"],
# ]
#
# reverse_animation = animation[::-1]
#
# upside_animation = []
# for col in "0123456789abc":
#     r = []
#     for row in "1234567":
#         r.append(row + col)
#     upside_animation.append(r)
#
# downside_animation = upside_animation[::-1]
#
# brightness = "\n\"e3f"
# dimness = "e30"
# wait_short = "w0009"
# wait_long = "w0021"
# wait_inf = "wffff"
# select_all = "a"
# terminate = "x\""
#
# f1 = open("1.h", "w")
# write(brightness, f1)
# for part in animation:
#     for line in part:
#         for segment in numbers[1]:
#             for index in segment:
#                 if line == index:
#                     write("s" + index, f1)
#     write(wait_short, f1)
# write(wait_long, f1)
# write(terminate, f1)
#
# f2 = open("2.h", "w")
# write(brightness, f2)
# for part in reverse_animation:
#     for line in part:
#         for segment in numbers[2]:
#             for index in segment:
#                 if line == index:
#                     write("s" + index, f2)
#     write(wait_short, f2)
# write(wait_long, f2)
# write(terminate, f2)
#
# f3 = open("3.h", "w")
# write(brightness, f3)
# for segment in numbers[3]:
#     for index in segment:
#         write("s" + index, f3)
# write(wait_long, f3)
# write(dimness, f3)
# write(select_all, f3)
# write(wait_long, f3)
# write(terminate, f3)
#
# f4 = open("4.h", "w")
# write(brightness, f4)
# for part in upside_animation:
#     for line in part:
#         for segment in numbers[4]:
#             for index in segment:
#                 if line == index:
#                     write("s" + index, f4)
#     write(wait_short, f4)
# write(wait_long, f4)
# write(terminate, f4)
#
# f5 = open("5.h", "w")
# write(brightness, f5)
# for part in downside_animation:
#     for line in part:
#         for segment in numbers[5]:
#             for index in segment:
#                 if line == index:
#                     write("s" + index, f5)
#     write(wait_short, f5)
# write(wait_long, f5)
# write(terminate, f5)
#
# f6 = open("6.h", "w")
# index_of_6 = []
# for line in numbers[6]:
#     for index in line:
#         index_of_6.append(index)
#
# random.shuffle(index_of_6)
# counter = 0
# write(brightness, f6)
# for i in range(1, 31):
#     counter += 1
#     write("s" + index_of_6[i - 1], f6)
#     if counter == 10 or counter == 20:
#         write(wait_short, f6)
# write(wait_long, f6)
# write(terminate, f6)


counter = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0
}

hard_coded = {
    1: "\n\"e3fs75s77w0009s74s78w0009s73s79w0009s72s7aw0009s71s7bw0021x\"",
    2: "\n\"e3fs71s20s60s1bs2cs6cw0009s72s30s50s1as3cs5cw0009s73s40s19s4cw0009s74s18w0009s75s17w0012s26s66w0009s36s56w0009s46w0021x\"",
    3: "\n\"e3fs20s30s40s50s60s71s72s73s74s75s26s36s46s56s66s77s78s79s7as7bs2cs3cs4cs5cs6cw0021e30aw0021x\"",
    4: "\n\"e3fs11s71w0009s12s72w0009s13s73w0009s14s74w0009s15s75w0009s26s36s46s56s66w0009s77w0009s78w0009s79w0009s7aw0009s7bw0021x\"",
    5: "\n\"e3fs2cs3cs4cs5cs6cw0009s7bw0009s7aw0009s79w0009s78w0009s77w0009s26s36s46s56s66w0009s15w0009s14w0009s13w0009s12w0009s11w0009s20s30s40s50s60w0021x\"",
    6: "\n\"e3fs7bs15s1bs26s17s3cs56s6cs5cs46w0009s12s14s36s18s77s4cs30s11s60s78w0009s13s2cs50s79s7as66s1as19s40s20w0021x\""
}

file = open("project.h", "a")
for _ in range(0, 66):
    r = random.randint(1, 6)
    while counter[r] == 11:
        r = random.randint(1, 6)
    counter[r] += 1
    write(hard_coded[r], file)

for value in counter.values():
    print(" ", value)
