import random

def hangman(word):
    wrong = 0
    stages = ["",
              "________       ",
              "｜             ",
              "｜      ｜     ",
              "｜       O     ",
              "｜      /｜＼   ",
              "｜       /＼    ",
              "｜             "
              ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("ハングマンへようこそ！")

    while wrong < len(stages)-1:
        print("\n")
        msg = "１文字目を予想してね"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind]="$"
        else:
            wrong +=1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け!正解は{}.".format(word))

R_list = ["cat","apple","dog","car","bike","train","bus","sport","ball","soccer",
        "music","piano","tennis","baseball","basketball","orange","egg","japan",
        "school","class","bag","camera","cap","notebook","pen","picture","tree",
        "town","city","park","people","friend","woman","man"]
r = R_list[random.randint(0,len(R_list))]
hangman(r)
