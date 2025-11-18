from colorama import Fore, Style, init
init()
lives = 10
word = input(f"{Fore.YELLOW}input a word: {Style.RESET_ALL}")
switch = False

end = True
list_of_filled = ""
list_of_blank = []

ans = []
ans = list(word)

for i in range(len(word)):
    list_of_blank.append("_ ")

def print_correct():
    global list_of_filled, list_of_blank, ans
    list_of_filled = list_of_filled.join(list_of_blank)
    print(list_of_filled)
    list_of_filled = ""


print("TO QUIT PRESS CTRL+C")
while end:
    switch = False

    print_correct()
    print(f"\n{Fore.BLUE}lives: {lives}/10{Style.RESET_ALL}")
    inp = str(input(f"{Fore.YELLOW}input a letter/word: {Style.RESET_ALL}"))

    for i in range(len(word)):
        if inp == word:
            end = False
            print(f"{Fore.GREEN}you won :D{Style.RESET_ALL}")
            break
        if inp == ans[i]:
            list_of_blank[i] = inp + " "
            switch = True
        if "_ " not in list_of_blank:
            print(f"{Fore.GREEN}you won :D{Style.RESET_ALL}")
            end = False
            break
        i += 1
    if switch == False and end != False:
        lives -= 1
        print(f"\n{Fore.RED}incorrect letter/word{Style.RESET_ALL}")
    if lives <= 0:
        print(f"{Fore.green}ran out of lives :p{Style.RESET_ALL}")
        break

