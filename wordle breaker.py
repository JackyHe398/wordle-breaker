ban_list = []
ban_list_pre = []
correct_word_input = "     "
correct_word = ["","","","",""]
no_pos_input = ""
no_pos = [[]for _ in range(5)]
all_no_pos = []
ToF = "null" # y/n/""
file = open("wb.txt")
ordered_letter = []
con = False
keep_list = []


def separate_correct_letter_to_list(correct_word_input):
    for _ in range(5):
        if correct_word_input[_:_+1] != " ":
            correct_word[_] = correct_word_input[_:_+1]
    
    print(correct_word)


def input_banned_list():
    print(f"Input the baned word: ", end="")
    ban_list_pre = sorted(str.lower(input()))
    for i in range(len(ban_list_pre)):
        if ban_list_pre[i] not in ban_list and str(ban_list_pre[i]).isalpha():
            ban_list.append(ban_list_pre[i])
    
    ban_list.sort()

def input_correct_letter():
    ToF = "null"
    while not (ToF == "y" or ToF == "n" or ToF == ""):
        print(f"The word now is {correct_word}, is it correct?(y/n): ",end = "")
        ToF = str.lower(input())

    if ToF == "y" or ToF == "":
        ToF = "null"
        return

    ToF = "n" #initialise ToF
    
    while ToF == "n":
        print("Input the World You know(replace the letter with space if you don't know): ", end="")
        correct_word_input = input()
        if len(correct_word_input) != 5:
            continue
        if not(all(x.isalpha() or x.isspace() for x in correct_word_input)):
            continue

        print(f"The word now is {correct_word_input}, is it correct?(y/n)")
        ToF = str.lower(input())
        separate_correct_letter_to_list(correct_word_input)

    ToF = "null"

def input_no_pos_letter():
    for _ in range(5):
        print(f"Input the wrong position letter in {_+1} position(yellow one): ",end='')
        no_pos_input = list(input())
        for j in range(len(no_pos_input)):
            if no_pos_input[j].isalpha():
                if no_pos_input[j] not in no_pos[_]:
                    no_pos[_].append(no_pos_input[j])
                if no_pos_input[j] not in all_no_pos:
                    all_no_pos.append(no_pos_input[j])

while True:
    input_banned_list()
    input_correct_letter()
    input_no_pos_letter()
    remove_list = []

    for line in file:
        word = line.replace('\n', '')
        keep_list.append(word)

    for _ in range(len(keep_list)):
        word = keep_list[_]
        ordered_letter = list(keep_list[_])
        for j in range(5):
            if ordered_letter[j] in ban_list:
                con = True
                break
            
            if not (ordered_letter[j] == correct_word[j] or correct_word[j] == ""):
                con = True
                break

            if ordered_letter[j] in no_pos[j]:
                con = True
                break
        
        for j in range(len(all_no_pos)):
            if all_no_pos[j] not in word:
                con = True
                break

        if con:
            con = False
            remove_list.append(keep_list[_])
            continue

    for _ in range(len(remove_list)):
        keep_list.remove(remove_list[_]) 
    
    print(keep_list)