import sys


# 1. the form " Please convert *** "
def form1(converse_words):
    A_to_R_single = {"0": "", "1": "I", "2": "II", "3": "III", "4": "IV", "5": "V", "6": "VI", "7": "VII", "8": "VIII",
                     "9": "IX"}
    A_to_R_tens = {"0": "", "1": "X", "2": "XX", "3": "XXX", "4": "XL", "5": "L", "6": "LX", "7": "LXX", "8": "LXXX",
                   "9": "XC"}
    A_to_R_hundred = {"0": "", "1": "C", "2": "CC", "3": "CCC", "4": "CD", "5": "D", "6": "DC", "7": "DCC", "8": "DCCC",
                      "9": "CM"}
    A_to_R_thousand = {"1": "M", "2": "MM", "3": "MMM"}
    arabic = converse_words
    if arabic.isdigit():
        charge = int(arabic)
        if charge > 3999 or arabic[0] == "0":
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()

        result_A_to_R = ""
        if len(arabic) == 4:
            result_A_to_R = result_A_to_R + A_to_R_thousand[arabic[0]] + A_to_R_hundred[arabic[1]] \
                            + A_to_R_tens[arabic[2]] + A_to_R_single[arabic[3]]
        elif len(arabic) == 3:
            result_A_to_R = result_A_to_R + A_to_R_hundred[arabic[0]] + A_to_R_tens[arabic[1]] \
                            + A_to_R_single[arabic[2]]
        elif len(arabic) == 2:
            result_A_to_R = result_A_to_R + A_to_R_tens[arabic[0]] + A_to_R_single[arabic[1]]
        elif len(arabic) == 1:
            result_A_to_R = result_A_to_R + A_to_R_single[arabic[0]]

        return result_A_to_R

    else:
        roman = converse_words

        R_to_A = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        check = ["I", "V", "X", "L", "C", "D", "M"]

        for a in roman:
            if a not in check:
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()

        if roman.count("I") > 3 or roman.count("X") > 3 or roman.count("C") > 3 or roman.count("M") > 3 \
                or roman.count("V") > 1 or roman.count("L") > 1 or roman.count("D") > 1:
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()

        i = 0
        while i < len(roman) - 1:
            if roman[i] == "I":
                if "IXI" in roman or "IVI" in roman:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
                elif R_to_A[roman[i]] < R_to_A[roman[i + 1]] and roman[i + 1] != "V" and roman[i + 1] != "X":
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
                elif R_to_A[roman[i]] < R_to_A[roman[i + 1]] and R_to_A[roman[i]] == R_to_A[roman[i - 1]]:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()

            elif roman[i] == "X":
                if "XLX" in roman or "XCX" in roman:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
                elif R_to_A[roman[i]] < R_to_A[roman[i + 1]] and roman[i + 1] != "L" and roman[i + 1] != "C":
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
                elif R_to_A[roman[i]] < R_to_A[roman[i + 1]] and R_to_A[roman[i]] == R_to_A[roman[i - 1]]:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()

            elif roman[i] == "C":
                if "CMC" in roman or "CDC" in roman:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
                if R_to_A[roman[i]] < R_to_A[roman[i + 1]] and roman[i + 1] != "M" and roman[i + 1] != "D":
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()
                elif R_to_A[roman[i]] < R_to_A[roman[i + 1]] and R_to_A[roman[i]] == R_to_A[roman[i - 1]]:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()

            elif roman[i] == "V" or roman[i] == "L" or roman[i] == "D":
                if R_to_A[roman[i]] < R_to_A[roman[i + 1]]:
                    print("Hey, ask me something that's not impossible to do!")
                    sys.exit()

            i = i + 1

        if roman[i] not in check:
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()

        result_R_to_A = 0
        i = 0
        while i < len(roman) - 1:
            if R_to_A[roman[i]] >= R_to_A[roman[i + 1]]:
                result_R_to_A = result_R_to_A + R_to_A[roman[i]]
            else:
                result_R_to_A = result_R_to_A + R_to_A[roman[i + 1]] - R_to_A[roman[i]]
                i = i + 1
            i = i + 1
        result_R_to_A = result_R_to_A + R_to_A[roman[i]]

        return result_R_to_A


# 2. the form " Please convert *** using *** "
def form2(converse_words, rule):
    for i in rule:
        if rule.count(i) > 1:
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()

    if converse_words.isdigit():
        arabic = converse_words
        if arabic[0] == "0":
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
        elif arabic[0] == "9" and len(arabic) * 2 + 1 > len(rule):
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
        elif int(arabic[0]) >= 4 and len(arabic) * 2 > len(rule):
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()
        elif len(arabic) * 2 - 1 > len(rule):
            print("Hey, ask me something that's not impossible to do!")
            sys.exit()

        i = 0
        j = 0
        result_word = ""
        arabic = arabic[::-1]
        rule = rule[::-1]

        while i < len(arabic):
            if arabic[i] == "0":
                added = ""
            if arabic[i] == "1":
                added = ""
                added = added + rule[j]
            if arabic[i] == "2":
                added = ""
                added = added + rule[j] * 2
            if arabic[i] == "3":
                added = ""
                added = added + rule[j] * 3
            if arabic[i] == "4":
                added = ""
                added = added + rule[j] + rule[j + 1]
            if arabic[i] == "5":
                added = ""
                added = added + rule[j + 1]
            if arabic[i] == "6":
                added = ""
                added = added + rule[j + 1] + rule[j]
            if arabic[i] == "7":
                added = ""
                added = added + rule[j + 1] + rule[j] * 2
            if arabic[i] == "8":
                added = ""
                added = added + rule[j + 1] + rule[j] * 3
            if arabic[i] == "9":
                added = ""
                added = added + rule[j] + rule[j + 2]
            result_word = added + result_word
            i = i + 1
            j = j + 2

        return result_word

    elif converse_words.isalpha():
        roman = converse_words
        for i in roman:
            if i not in rule:
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()

        rule = rule[::-1]
        count = 0
        value = 1
        dictionary = {}
        for i in rule:
            x = i
            y = value
            added = {x: y}
            dictionary.update(added)
            if count % 2 == 0:
                value = value * 5
            else:
                value = value * 2
            count = count + 1

        count = 0
        for i in dictionary:
            if count % 2 == 0 and roman.count(i) > 3:
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
            elif count % 2 == 1 and roman.count(i) > 1:
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
            count = count + 1

        check = []
        for i in rule:
            check.append(i)
        check.append("!")
        check.append("!")
        count = 0
        while count < len(check) - 2:
            if count % 2 == 0:
                if check[count + 1] != "!":
                    invalid = ""
                    invalid = check[count] + check[count + 1] + check[count]
                    if invalid in roman:
                        print("Hey, ask me something that's not impossible to do!")
                        sys.exit()
                    if check[count + 2] != "!":
                        invalid = ""
                        invalid = check[count] + check[count + 2] + check[count]
                        if invalid in roman:
                            print("Hey, ask me something that's not impossible to do!")
                            sys.exit()

                    j = 0
                    while j < len(roman) - 1:
                        if roman[j] == check[count] and dictionary[roman[j]] < dictionary[roman[j + 1]]:
                            if roman[j + 1] != check[count + 1] and roman[j + 1] != check[count + 2]:
                                print("Hey, ask me something that's not impossible to do!")
                                sys.exit()
                            elif roman[j - 1] == roman[j]:
                                print("Hey, ask me something that's not impossible to do!")
                                sys.exit()
                        j = j + 1

            elif count % 2 == 1:
                j = 0
                while j < len(roman) - 1:
                    if roman[j] == check[count] and dictionary[roman[j]] < dictionary[roman[j + 1]]:
                        print("Hey, ask me something that's not impossible to do!")
                        sys.exit()
                    j = j + 1

            count = count + 1

        i = 0
        result_R_to_A = 0
        while i < len(roman) - 1:
            if dictionary[roman[i]] >= dictionary[roman[i + 1]]:
                result_R_to_A = result_R_to_A + dictionary[roman[i]]
            else:
                result_R_to_A = result_R_to_A + dictionary[roman[i + 1]] - dictionary[roman[i]]
                i = i + 1
            i = i + 1
        result_R_to_A = result_R_to_A + dictionary[roman[i]]
        return result_R_to_A

    else:
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()


def form3(converse_words):
    if not converse_words.isalpha():
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()

    the_word = []
    for i in converse_words:
        the_word.append(str(i))

    A_to_R_single = {0: "", 1: "0", 2: "00", 3: "000", 4: "01", 5: "1", 6: "10", 7: "100", 8: "1000", 9: "02"}
    A_to_R_tens = {0: "", 1: "2", 2: "22", 3: "222", 4: "23", 5: "3", 6: "32", 7: "322", 8: "3222", 9: "24"}
    A_to_R_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100}
    result_dict = {}

    num_dict = []
    i = 0
    times = 1
    while i < 10:
        j = 0
        while j < 10:
            abc = A_to_R_tens[i] + A_to_R_single[j]
            x = [abc.index(a) for a in abc]
            y = ""
            for p in x:
                y = y + str(p)
            j = j + 1
            if y == "":
                continue
            num_dict.append(y)
        i = i + 1

    result = ""
    while 1:
        if len(the_word) == 0:
            break
        save_word = ""
        save_the_word = the_word[:]
        value = 0

        while 1:
            if len(the_word) == 0:
                break
            temp_word = save_word
            i = the_word.pop(-1)
            count = the_word.count(i)
            temp_word = i + temp_word

            while 1:
                if count == 0:
                    break
                j = the_word.pop(-1)
                if j == i:
                    temp_word = j + temp_word
                    count -= 1
                else:
                    temp_word = j + temp_word

            temp_index = [temp_word.index(a) for a in temp_word]
            temp_index_str = ""
            for p in temp_index:
                temp_index_str = temp_index_str + str(p)

            if temp_index_str not in num_dict and value == 0:
                print("Hey, ask me something that's not impossible to do!")
                sys.exit()
            elif temp_index_str in num_dict:
                q = 1
                for p in num_dict:
                    if p == temp_index_str:
                        value = q
                        break
                    q += 1
                save_word = temp_word
                save_the_word = the_word[:]

            elif temp_index_str not in num_dict and value != 0:
                the_word = save_the_word[:]
                break
        result = str(value) + result
        abc = form1(str(value))
        already_added = []
        k = 0
        for i in save_word:
            if i in already_added:
                k += 1
                continue
            already_added.append(i)
            x = i
            y = A_to_R_dict[abc[k]] * times
            add_element = {x: y}
            result_dict.update(add_element)
            k += 1
        times = times * 100

    result_dict_str = ""
    compare = 1
    element_count = len(result_dict)
    k = 0
    last_char = ""
    while element_count != 0:
        charge = 0
        for i in result_dict:
            if result_dict[i] == compare:
                result_dict_str = i + result_dict_str
                last_char = i
                charge = 1
                element_count -= 1
        if charge == 0 and last_char != "_":
            result_dict_str = "_" + result_dict_str
            last_char = "_"
        if k % 2 == 0:
            compare = compare * 5
        if k % 2 == 1:
            compare = compare * 2
        k = k + 1
    if result_dict_str[-1] == "_":
        print("Hey, ask me something that's not impossible to do!")
        sys.exit()

    print("Sure! It is %s using %s" % (result, result_dict_str))


# main function
try:
    keyboard_typing = input("How can I help you? ")
    words = keyboard_typing.split()
    if len(words) < 3 or len(words) > 5:
        raise ValueError
    elif words[0] != "Please" or words[1] != "convert":
        raise ValueError
    elif len(words) == 5 and words[3] != "using":
        raise ValueError
    elif len(words) == 4 and words[3] != "minimally":
        raise ValueError
except ValueError:
    print("I don't get what you want, sorry mate!")
    sys.exit()

# 1. when the form is 'Please convert ***'
if len(words) == 3:
    result = form1(words[2])
    print("Sure! It is " + str(result))

# 2. when the form is 'Please convert *** using ***'
if len(words) == 5:
    result = form2(words[2], words[4])
    print("Sure! It is " + str(result))

# 3. when the form is ' Please convert *** minimally'
if len(words) == 4:
    form3(words[2])
