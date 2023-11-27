#Task 2
import random #Use random numbers
import time #Create wait times in code - stops players from spamming ENTER
import os

if os.path.isfile("leaderboard.txt") != True: #Only creates file if the file doesn't exist
    topfive_file = open("Leaderboard.txt","w")
    topfive_file.write("000  |  Non-Player Character\n"*5)
    topfive_file.close()

def dicegame(): #Large function to keep code robust

    def authentication(Name):
        Usernames = {"Ali" : "Entry21" ,"Viraj" : "User79" ,"Harvey" : "Pass64","Saahir" : "Trial25","Ambi" : "Final00"} #Array matches the usernames with a password
        while True: #If the username isn't validated the check can happen again
            IdUser=input("Input your USERNAME:\t")
            IdPass=input("Input your PASSWORD:\t")
            if IdUser in Usernames and IdPass == Usernames[IdUser]: #If the username is present...
                Name = input("Please insert the name you would like to be called:\t")#User can use a different name to the username
                if Name=="":#If nothing is typed in, the name will be the username from the array
                    Name=IdUser
                return Name
                break #End loop
            else:
                print("Username or password is incorrect; try again!")
            
    def game(Player1Name,Player2Name): #Everything relating to the rules is within the game function
        P1Score=0 #Player 1's Score
        P2Score=0 #Player 2's Score
        rounds=1 #Rounds
        def gamerounds(name,score): 
            print("\n"+name+"'s turn!")
            time.sleep(1)
            input("Press ENTER to roll two dice!") 
            print("Rolling...")
            time.sleep(1)
            DiceA = random.randint(1,6) #Random numbers (1 to 6)
            DiceB = random.randint(1,6)
            print("You got:",DiceA,"and",DiceB)
            time.sleep(1)
            total=DiceA+DiceB #Total of results
            score=score+total
            if total%2==0: #Divisible by 2 (remainder of 0) making even
                print("10 extra points for an even total!")
                score=score+10 #Adds 10 if score is even
            else:
                print("5 less points for an odd total!")
                score=score-5 #Removes 5 if it isn't even
                if score<0:
                    score=0
            if DiceA==DiceB: #In the case of a double
                time.sleep(1)
                input("Wow, you got a double! Press ENTER to roll one more die!") 
                print("Rolling...")
                time.sleep(1)
                DiceC = random.randint(1,6)
                print("You got "+str(DiceC)+"!")#Prints extra roll score
                time.sleep(1)
                score=score+DiceC #Add the new roll to the score
            print(name+" has: "+str(score))
            return score
        while rounds<6:
            StartRound=input("Press ENTER to start round "+str(rounds)) #The player must press ENTER everytime they want to play
            time.sleep(1)
            P1Score=gamerounds(Player1Name,P1Score)#Runs function with name and score
            time.sleep(3)
            P2Score=gamerounds(Player2Name,P2Score)
            time.sleep(2)
            rounds=rounds+1#Fuels loop
            print("\nThat's the end of that round!\n") #If there are rounds remaining, it will go on 

        def finalround(P1Name,P2Name):#Final round if scores are equal
            def finalroundroll(Name,Score):
                time.sleep(1)
                Roll=input("Press ENTER to roll the die, "+Name)#Asks to roll the dice
                print("Rolling...")
                time.sleep(1)
                Score=random.randint(1,6)#Another random score
                print(Name+" got:",str(Score))#Prints score
                return Score
            print("You have equal scores. Roll the highest in sudden death!\n")
            P1FScore=0
            P2FScore=0
            while True:#While loop
                time.sleep(1)
                SuddenDeathRoll=input("Press ENTER to start the Sudden Death round")#Starts sudden death
                P1FScore=finalroundroll(P1Name,P1FScore)#Sets scores to the random roll
                P2FScore=finalroundroll(P2Name,P2FScore)
                time.sleep(1)
                if P1FScore>P2FScore:
                    return P1Name
                elif P2FScore>P1FScore:
                    return P2Name
                elif P1FScore==P2FScore:
                    print("We need another round!") #Checks whether winner is identified
                
        if rounds==6:
            print("Five rounds complete! Let's see who won!") #When the rounds are finished
            if P1Score>P2Score:
                WinnerList=[Player1Name,P1Score]#Creates list of winners
            elif P1Score<P2Score:
                WinnerList=[Player2Name,P2Score]
            elif P1Score==P2Score:
                Winner=finalround(Player1Name,Player2Name)#If the scores are equal, a final round is started
                WinnerList=[Winner,P1Score]
            return WinnerList

    def leaderboardfile(Winners):#Places names in leaderboard
        print(Winners[0]+" won!")#Declares winner
        if Winners[1]<10: 
            Winners[1] = "00"+str(Winners[1])#Adds two 0s to the front of the number to make it sort-worthy
        elif Winners[1]<100:
            Winners[1] = "0"+str(Winners[1])#Adds a 0 to the front of the number to make it sort-worthy
        lbtxt = open("Leaderboard.txt","a")
        lbtxt.write(str(Winners[1]) + "  |  " + Winners[0] +"\n")#writes line to file
        lbtxt.close()
        lbtxt = open("Leaderboard.txt","r")#opens file for reading            
        lines = lbtxt.readlines()#reads lines
        lbtxt.close()
        lines = sorted(lines,reverse=True)#sorts lines from variable
        Check = 1
        time.sleep(1)
        print("\nTOP 5 Winners!")#prints winners and scores and names
        print("SCORE  |  NAME")
        for line in lines:
            if Check<6:
                print(str(Check)+")"+line[:-1])
                time.sleep(0.25)#prints the top 5 winners and names plus their positions
                Check=Check+1
        return True
        
    Player1Name=""
    Player1Name=authentication(Player1Name)#Authenticates players
    print("Successfully identified!")
    while True:
        Player2Name=""
        Player2Name=authentication(Player2Name)
        if Player1Name!=Player2Name:#Checks accounts are unique
            print("Successfully identified!")
            Winners=game(Player1Name,Player2Name)#Starts games
            Complete=leaderboardfile(Winners)
            if Complete==True:
                replay=input("\nPress ENTER to restart. Type QUIT and then press ENTER to end the program.\t")#Resets program
                if replay.upper()!="QUIT":
                    dicegame()
            break
        else:
            print("You can't log in twice or have the same name. Try again.\n")
dicegame()
            
