from random import seed
from random import randint

CHOICE_SET = {1,2,3}
WIKI_INFO = """\nThe Monty Hall problem is a brain teaser,in the form of a probability puzzle,
loosely based on the American television game show Let's Make a Deal
and named after its original host, Monty Hall.\n\nSuppose you're on a game show,
and you're given the choice of three doors: Behind one door is a car;
behind the others, goats. You pick a door, say No. 1, and the host,
who knows what's behind the doors, opens another door, say No. 3, which has a goat.
He then says to you, 'Do you want to pick door No. 2?'
Is it to your advantage to switch your choice?
\nVos Savant's response was that the contestant should switch to the other door.
Under the standard assumptions, contestants who switch have a 2/3 chance of
winning the car, while contestants who stick to their initial choice have
only a 1/3 chance.\n"""

def reward_selection(user_num) -> (int, int):
    reward_num = randint(1,3)

    #remove user's choice
    choices = [1,2,3]
    choices.remove(user_num)
    
    reveal_opts = [x for x in choices if x != reward_num]
    reveal = reveal_opts[randint(0, len(reveal_opts) - 1)]

    return reveal, reward_num

def loading_bar(wins, total) -> str:
    if total == 0:
        return "".join(["_" for i in range(50)])
    percent = wins/total
    bar = int(percent * 50)
    bar_string = ""
    for i in range(bar):
        bar_string += "#"
    for i in range(50-bar):
        bar_string += "_"
    bar_string += "\t" + str(round(percent * 100, 1)) + "%\t" + str(wins) + "/" + str(total)
    return bar_string

    
def simulate(sim_num) -> (int, int):
    wins_og = 0
    wins_alt = 0
    for i in range(int(sim_num/2)):
        guess = randint(1,3)
        reveal, reward_num = reward_selection(guess)
        if guess == reward_num:
            wins_og += 1
    for i in range(sim_num - int(sim_num/2)):
        guess = randint(1,3)
        reveal, reward_num = reward_selection(guess)
        guess = CHOICE_SET.difference({reveal, guess}).pop()
        if guess == reward_num:
            wins_alt += 1

    print()
    print ("wins without switching:\n" + loading_bar(wins_og, int(sim_num/2)))
    print ("wins having switched guesses:\n" + loading_bar(wins_alt, sim_num - int(sim_num/2)))

    
og_total = 0
switch_total = 0
user_og_wins = 0
user_switch_wins = 0
print("Welcome to the Monte Hall problem")
wiki_opt = input("Do you know how to play?\n" +
                 "Hit ENTER to continue or <any key> for more info:")
if len(wiki_opt) > 0:
    print(WIKI_INFO) 

while(True):
    play_opt = input("Would you like to play or simulate? p or s: ")
    assert play_opt[0] == "p" or play_opt[0] == "s"
    if play_opt[0] == "p":
        break

    if play_opt[0] == "s":
        sim_num = input("How many rounds would you like to simulate?: ")
        print()
        simulate(int(sim_num))
        print()
        quit_opt = input("Type ENTER to continue or <any key> to quit. ")
        if len(quit_opt) > 0:
            exit()
        

while(True):
    user_num = int(input("\nPick a number 1-3: "))
    assert user_num > 0 and user_num < 4
    reveal, reward_num = reward_selection(user_num)
    
    print("\nI can't say much about your choice but I *can* tell you that\n" 
            + str(reveal) + " is NOT the winning number.")
    print("\nDo you want to switch your number from " + str(user_num) + "?")
    switch_opt = input("enter 'y' to switch and 'n' to stick with "
                       + str(user_num) + ": ")
    assert switch_opt[0] == "y" or switch_opt[0] == "n"
    if switch_opt[0] == "y":
        user_num = CHOICE_SET.difference({reveal, user_num}).pop()
        print("you have switched to door " + str(user_num))
        switch_total += 1
    else:
        og_total += 1


    print()
    if user_num == reward_num:
        if switch_opt[0] == "y":
            user_switch_wins += 1
        else:
            user_og_wins += 1
        print("Congrats! You won. \n" +
              "You have won " + str(user_switch_wins + user_og_wins) +
              " out of " + str(switch_total + og_total) + " total rounds")
    else:
        print("Sorry you lost")

    details_opt = input("Would you like more details? y or n: ")
    assert details_opt[0] == "y" or details_opt[0] == "n"
    if details_opt[0] == "y":
        print ("\nTOTAL ROUNDS: " + str(switch_total + og_total))
        print ("wins without switching guesses:\n" + loading_bar(user_og_wins, og_total))
        print ("wins having switched guesses:\n" + loading_bar(user_switch_wins, switch_total))

    

    break_opt = input("\ntype ENTER to continue or any key to break: ")

    if(len(break_opt) > 0):
        break

