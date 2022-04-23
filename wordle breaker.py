ban_list = []
correct_word = [""for _ in range(5)]
no_pos = [[]for _ in range(5)]
all_no_pos = []
file = open("wb.txt")
ordered_letter = []
con = False
keep_list = []


def separate_correct_letter_to_list(inp):
    for _ in range(5):
        if inp[_:_+1] != " ":
            correct_word[_] = inp[_:_+1]
    
    print(correct_word)


def input_banned_list():
    print(f"\nbanned word now is: {ban_list}")
    print(f"Input the baned word: ", end="")
    ban_list_pre = sorted(str.lower(input()))
    for i in range(len(ban_list_pre)):
        if ban_list_pre[i] not in ban_list and str(ban_list_pre[i]).isalpha():
            ban_list.append(ban_list_pre[i])
    
    ban_list.sort()


def input_correct_letter():
    tof = "null"
    print()
    while not (tof == "y" or tof == "n" or tof == ""):
        print(f"The word now is {correct_word}\nIs it correct?(y/n): ", end="")
        tof = str.lower(input())

    if tof == "y" or tof == "":
        return

    tof = "n"
    
    while tof == "n":
        print("Input the World You know(replace the letter with space if you don't know): ", end="")
        correct_word_input = input()
        if len(correct_word_input) != 5:
            continue
        if not(all(x.isalpha() or x.isspace() for x in correct_word_input)):
            continue

        print(f"The word now is \"{correct_word_input}\"\nIs it correct?(y/n)", end="")
        tof = str.lower(input())
        separate_correct_letter_to_list(correct_word_input)


def input_no_pos_letter():
    print()
    for _ in range(5):
        print(f"Input the wrong position letter in {_+1} position(yellow one): ", end='')
        no_pos_input = list(input())
        for j in range(len(no_pos_input)):
            if no_pos_input[j].isalpha():
                if no_pos_input[j] not in no_pos[_]:
                    no_pos[_].append(no_pos_input[j])
                if no_pos_input[j] not in all_no_pos:
                    all_no_pos.append(no_pos_input[j])


print("+="*10+"Wordle Breaker"+"+="*10)
while True:
    input_banned_list()  # 3 type of inputting
    input_correct_letter()
    input_no_pos_letter()
    remove_list = []  # initialise to empty array

    for line in file:
        word = line.replace('\n', '')
        keep_list.append(word)

    for _ in range(len(keep_list)):
        word = keep_list[_]
        ordered_letter = list(keep_list[_])
        for j in range(5):
            if ordered_letter[j] in ban_list:  # these three output is the same
                con = True  # throw the wrong word out
                break
            elif not (ordered_letter[j] == correct_word[j] or correct_word[j] == ""):
                con = True
                break
            elif ordered_letter[j] in no_pos[j]:
                con = True
                break
        
        for j in range(len(all_no_pos)): 
            if all_no_pos[j] not in word:
                con = True
                break

        if con:  # break the big "for" and remove the wrong words
            con = False
            remove_list.append(keep_list[_])
            continue

    for _ in range(len(remove_list)):
        keep_list.remove(remove_list[_]) 
    
    print(keep_list)
