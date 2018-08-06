import random as rn
import subprocess as sp

# text = ["Das hier", "ist ein", "langer", "Text"]

# text = input("Your text: ")
# text = text.split(" ")

def clear():
    sp.call('clear',shell=True)

def sand_func(text):
    if str(type(text)) == ("<class 'list'>" or "<class 'dict'>"):
        len_count = []
        i = 0
        for i in text:
            len_count.append(len(i))
        max_count = int(max(len_count))
        wrap = "=" * max_count
        text = "\n".join(text)
        return(wrap+"\n"+text+"\n"+wrap)
    elif str(type(text)) == ("<class 'str'>" or "<class 'int'>"):
        i = 0
        wrap = "=" * len(text)
        return(wrap+"\n"+text+"\n"+wrap)


def wrap_func(text):
    len_count = []
    i = 0
    for i in text:
        len_count.append(len(str(i)))
    max_count = int(max(len_count))
    tb = (max_count + 4) * "="

    def md(row, max_count):
        space = " " * (max_count - len(str(row)))
        return("| "+str(row)+space+" |")

    new_text = [tb]

    for word in text:
        new_text.append(md(word, max_count))

    new_text.append(tb)
    return(new_text)

def wrfl_all(list, old):
    if str("all") in list:
        w1 = int(rn.randint(1, 6))
        w2 = int(rn.randint(1, 6))
        w3 = int(rn.randint(1, 6))
        w4 = int(rn.randint(1, 6))
        w5 = int(rn.randint(1, 6))
        result = [w1, w2, w3, w4, w5]
    else:
        result = old
        if str(1) in list:
            w1 = int(rn.randint(1, 6))
            result[0] = w1
        if str(2) in list:
            w2 = int(rn.randint(1, 6))
            result[1] = w2
        if str(3) in list:
            w3 = int(rn.randint(1, 6))
            result[2] = w3
        if str(4) in list:
            w4 = int(rn.randint(1, 6))
            result[3] = w4
        if str(5) in list:
            w5 = int(rn.randint(1, 6))
            result[4] = w5
    return(result)

def player_names():
    i=int(1)
    names = []
    try:
        count = int(input("How many players: "))
    except:
        clear()
        print(sand_func(str("A number is needed!")))
        player_names()
    if count > 4:
        clear()
        print(sand_func("Max. 4 players supported"))
        player_names()
    elif count <= 1:
        clear()
        print(sand_func("At least 2 players needed"))
        player_names()
    else:
        while i <= count:
            name = str(input("Player "+str(i)+" name: "))
            if name in names:
                clear()
                print(sand_func(["No double names!", "Try again!"]))
                # print("Try again!")
                continue
            names.append(str(name))
            i += 1
        return(names)

def tcwrap(lc, rc):
    ## max. length top and bottom
    len_count_lc = []
    i = 0
    for i in lc:
        len_count_lc.append(len(i))
    max_count_lc = int(max(len_count_lc))

    len_count_rc = []
    i = 0
    for i in rc:
        len_count_rc.append(len(str(i)))
    max_count_rc = int(max(len_count_rc))

    max_count_ges = max_count_rc + max_count_lc
    tb = "=" * (max_count_ges + 7)

    def tcmd(row_lc, row_rc, max_count_lc, max_count_rc):
        minus_lc = "-" * (max_count_lc - len(row_lc))
        minus_rc = " " * (max_count_rc - len(str(row_rc)))
        return("| "+row_lc+minus_lc+" | "+str(row_rc)+minus_rc+" |")

    new_text = [tb]

    for (row_lc, row_rc) in zip(lc, rc):
        new_text.append(tcmd(row_lc, row_rc, max_count_lc, max_count_rc))

    new_text.append(tb)
    return(new_text)


def tcwrap_blank(lc, rc):
    ## max. length top and bottom
    len_count_lc = []
    i = 0
    for i in lc:
        len_count_lc.append(len(i))
    max_count_lc = int(max(len_count_lc))

    len_count_rc = []
    i = 0
    for i in rc:
        len_count_rc.append(len(str(i)))
    max_count_rc = int(max(len_count_rc))

    max_count_ges = max_count_rc + max_count_lc
    tb = "=" * (max_count_ges + 7)

    def tcmd(row_lc, row_rc, max_count_lc, max_count_rc):
        minus_lc = " " * (max_count_lc - len(row_lc))
        minus_rc = " " * (max_count_rc - len(str(row_rc)))
        return("| "+row_lc+minus_lc+" | "+str(row_rc)+minus_rc+" |")

    new_text = [tb]

    for (row_lc, row_rc) in zip(lc, rc):
        new_text.append(tcmd(row_lc, row_rc, max_count_lc, max_count_rc))

    new_text.append(tb)
    return(new_text)


def poss(nums):
    def count_num(nums, num):
        count = 0
        for c in nums:
            if c == num:
                count += 1
        return count

    eins = count_num(nums, 1)
    zwei = count_num(nums, 2)
    drei = count_num(nums, 3)
    vier = count_num(nums, 4)
    funf = count_num(nums, 5)
    sechs = count_num(nums, 6)
    nums_count = [eins, zwei, drei, vier, funf, sechs]
    nums_pnkt = [1*eins, 2*zwei, 3*drei, 4*vier, 5*funf, 6*sechs]

    kstrasse = 0
    gstrasse = 0
    kniffel = 0
    chance = 0
    pasch3 = 0
    pasch4 = 0
    full_house = 0

    z = 0 in nums_count
    a = 1 in nums_count
    b = 2 in nums_count
    c = 3 in nums_count
    d = 4 in nums_count
    e = 5 in nums_count

    if b and c:
        full_house=25
        # print("full house")

    if e:
        kniffel=50
        # print("Kniffel")

    ######gstrasse
    if 1 in nums and 2 in nums and 3 in nums and 4 in nums and 5 in nums:
        gstrasse=40
        # print("große straße")

    if 2 in nums and 3 in nums and 4 in nums and 5 in nums and 6 in nums:
        gstrasse=40
        # print("große straße")

    #####kstrasse
    if 1 in nums and 2 in nums and 3 in nums and 4 in nums:
        kstrasse=30
        # print("kleine straße")
    if 2 in nums and 3 in nums and 4 in nums and 5 in nums:
        kstrasse=30
        # print("kleine straße")
    if 3 in nums and 4 in nums and 5 in nums and 6 in nums:
        kstrasse=30
        # print("kleine straße")

    #####Pasch
    pasch3 = 0
    if 3 in nums_count or 4 in nums_count or 5 in nums_count:
        for i in nums_pnkt:
            pasch3 = pasch3 + i
        # print("3er pasch")

    if 4 in nums_count or 5 in nums_count:
        for i in nums_pnkt:
            pasch4 = pasch4 + i
        # print("4er pasch")

    chance = 0
    for i in nums_pnkt:
        chance = chance + i

    poss = nums_pnkt + ["=", gstrasse, kstrasse, full_house, kniffel, pasch3, pasch4, chance]
    return(poss)

def display_poss(score, poss):
    result = []
    i = 1
    if score[0] == 0 and poss[0] != 0:
        result.append(str(i)+". "+str(poss[0])+"pkte auf die 1er")
        i = i + 1
    if score[1] == 0 and poss[1] != 0:
        result.append(str(i)+". "+str(poss[1])+"pkte auf die 2er")
        i = i + 1
    if score[2] == 0 and poss[2] != 0:
        result.append(str(i)+". "+str(poss[2])+"pkte auf die 3er")
        i = i + 1
    if score[3] == 0 and poss[3] != 0:
        result.append(str(i)+". "+str(poss[3])+"pkte auf die 4er")
        i = i + 1
    if score[4] == 0 and poss[4] != 0:
        result.append(str(i)+". "+str(poss[4])+"pkte auf die 5er")
        i = i + 1
    if score[5] == 0 and poss[5] != 0:
        result.append(str(i)+". "+str(poss[5])+"pkte auf die 6er")
        i = i + 1
    if score[7] == 0 and poss[7] != 0:
        result.append(str(i)+". "+str(poss[7])+"pkte für die große Straße")
        i = i + 1
    if score[8] == 0 and poss[8] != 0:
        result.append(str(i)+". "+str(poss[8])+"pkte für die kleine Straße")
        i = i + 1
    if score[9] == 0 and poss[9] != 0:
        result.append(str(i)+". "+str(poss[9])+"pkte für das Full House")
        i = i + 1
    if score[10] == 0 and poss[10] != 0:
        result.append(str(i)+". "+str(poss[10])+"pkte für den Kniffel")
        i = i + 1
    if score[11] == 0 and poss[11] != 0:
        result.append(str(i)+". "+str(poss[11])+"pkte für den 3er Pasch")
        i = i + 1
    if score[12] == 0 and poss[12] != 0:
        result.append(str(i)+". "+str(poss[12])+"pkte für den 4er Pasch")
        i = i + 1
    if score[13] == 0 and poss[13] != 0:
        result.append(str(i)+". "+str(poss[13])+"pkte auf die Chance")
        i = i + 1
    result.append(str("Zum nochmal würfeln n eingeben"))
    return(result)

def calc_poss(action, score, poss):
    i = 1
    if score[0] == 0 and poss[0] != 0:
        if action == i:
            result = [0, poss[0]]
        i = i + 1
    if score[1] == 0 and poss[1] != 0:
        if action == i:
            result = [1, poss[1]]
        i = i + 1
    if score[2] == 0 and poss[2] != 0:
        if action == i:
            result = [2, poss[2]]
        i = i + 1
    if score[3] == 0 and poss[3] != 0:
        if action == i:
            result = [3, poss[3]]
        i = i + 1
    if score[4] == 0 and poss[4] != 0:
        if action == i:
            result = [4, poss[4]]
        i = i + 1
    if score[5] == 0 and poss[5] != 0:
        if action == i:
            result = [5, poss[5]]
        i = i + 1
    if score[7] == 0 and poss[7] != 0:
        if action == i:
            result = [7, poss[7]]
        i = i + 1
    if score[8] == 0 and poss[8] != 0:
        if action == i:
            result = [8, poss[8]]
        i = i + 1
    if score[9] == 0 and poss[9] != 0:
        if action == i:
            result = [9, poss[9]]
        i = i + 1
    if score[10] == 0 and poss[10] != 0:
        if action == i:
            result = [10, poss[10]]
        i = i + 1
    if score[11] == 0 and poss[11] != 0:
        if action == i:
            result = [11, poss[11]]
        i = i + 1
    if score[12] == 0 and poss[12] != 0:
        if action == i:
            result = [12, poss[12]]
        i = i + 1
    if score[13] == 0 and poss[13] != 0:
        if action == i:
            result = [13, poss[13]]
        i = i + 1


    return(result)




score_p1 = [0, 0, 0, 0, 0, 0, "=", 0, 0, 0, 0, 0, 0, 0]
score_p2 = [0, 0, 0, 0, 0, 0, "=", 0, 0, 0, 0, 0, 0, 0]
score_p3 = [0, 0, 0, 0, 0, 0, "=", 0, 0, 0, 0, 0, 0, 0]
score_p4 = [0, 0, 0, 0, 0, 0, "=", 0, 0, 0, 0, 0, 0, 0]

points = [0, 0, 0, 0]

score_temp = [
"1er",
"2er",
"3er",
"4er",
"5er",
"6er",
"=============",
"Kleine Straße",
"Große Straße",
"Full House",
"Kniffel",
"3er-Pasch",
"4er-Pasch",
"Chance"
]

def name_point(np, points):
    list = tcwrap_blank(np, points)
    return(list)

def join_two_lists(left, right, free):
    result = []
    len_left = len(left)
    len_right = len(right)
    free = " " * free
    if len_right > len_left:
        free_left = " " * len(left[0])
        len_add = len_right - len_left
        for a, b in zip(left, right):
            result.append(a + free + str(b))
        for i in range(len_left, len_right):
            result.append(free_left + free + str(right[i]))
    if len_right == len_left:
        for a, b in zip(left, right):
            result.append(a + free + str(b))
    if len_left > len_right:
        free_right = " " * len(right[0])
        len_add = len_left - len_right
        for a, b in zip(left, right):
            result.append(a + free + str(b))
        for i in range(len_right, len_left):
            result.append(left[i] + free + free_right)

    return(result)

a = True

clear()
np = player_names()
player = -1
wrf = ["all"]
count_try = 1
while True:
    end = 0
    a = True
    if player < (len(np) - 1):
        player = player + 1
    else:
        player = 0

    while a:
        clear()
        player_name = np[player]
        print("Playing: "+player_name)
        print("Übersicht:                Möglichkeiten:                   Spieler:")
        if player == 0:
            player_score = score_p1
        if player == 1:
            player_score = score_p2
        if player == 2:
            player_score = score_p3
        if player == 3:
            player_score = score_p4
        score_list = player_score
        if str("all") in wrf:
            old = []
            wrf_list = ["all"]
            nums_list = wrfl_all(wrf_list, old)
        else:
            old = nums_list
            wrf_list = wrf.split(" ")
            nums_list = wrfl_all(wrf_list, old)
        poss_list = poss(nums_list)
        left_display = tcwrap(score_temp, score_list)
        bar = display_poss(score_list, poss_list)
        display_poss_list = wrap_func(bar)
        player_data_list = tcwrap_blank(np, points)
        final1 = join_two_lists(left_display, display_poss_list, 5)
        final2 = join_two_lists(final1, player_data_list, 5)
        dices = ["                            Your dices:", "                            =====================", "                            | "+str(nums_list[0])+" | "+str(nums_list[1])+" | "+str(nums_list[2])+" | "+str(nums_list[3])+" | "+str(nums_list[4])+" |", "                            ====================="]
        for i in final2:
            print(i)
        for i in dices:
            print(i)

        while True:
            poss_count = len(bar)
            foo = []
            for i in range(1, poss_count+1):
                foo.append(str(i))
            choice = input("Aktion: ")
            if str(choice) in foo:
                set_points = calc_poss(int(choice), score_list, poss_list)
                score_list[int(set_points[player])] = int(set_points[1])

                gesamt = 0
                for i in score_list:
                    if i == "=":
                        continue
                    else:
                        gesamt = gesamt + int(i)
                points[player] = int(gesamt)
                end = 1
                break

            elif str(choice) == "n":
                if count_try < 3:
                    count_try = count_try + 1
                    print("Nochmal würfeln:")
                    player = player - 1
                    print("Zum abbrechen \"abbruch\" eingeben")
                    wrf = input("Welche Würfel neu würfeln (1 2 3 4 5): ")
                    if len(wrf) == 0:
                        wrf = str("all")
                    if wrf == "abbruch":
                        continue
                    break
                else:
                    print("Alle Versuche aufgebraucht")
                    continue

            else:
                print("Eingabe ungültig")
                continue



        a = False

    if end == 1:
        print("nächster player")
        count_try = 1
