from random import randint


pc_choice = randint(1, 100)
playing = True


while playing:
    user_choice = int(input("text your choice! : "))
    
    if user_choice == pc_choice:
        print("You Win!")
        playing = False
        
    elif user_choice < pc_choice:
        print("Higher!")
        
    elif user_choice > pc_choice:
        print("Lower!")