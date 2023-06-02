import random

possibleMoves = ["Rock","Paper","Scissors","Lizard","Spock"]

userPoint = computerPoint = 0

tie =False



def entireProcess(possibleMoves, userPoint, computerPoint,i,tie):
    while(i<5):
        print("\n")
        if(tie):
            print("---Tie breaker round---")
        else:
            print("---Round ",(i+1),"---")
        computerHand = possibleMoves[random.randint(0,4)]
        print("Possible moves:\n1. Rock\n2. Paper\n3. Scissors\n4. Lizard\n5. Spock")
        n = int(input("Enter you choice (1-5): "))
        if(n>5):
            print("Enter a valid choice.")
            continue;
        else:

            userHand = possibleMoves[n-1]
            if(userHand == computerHand):
                print("Computer played: ",computerHand)
                print("User played: ", userHand)
                print("That's a tie!")
                print("Computer: ",computerPoint," || ","User: ",userPoint)
                print("--------------------------\n")
                i+=1

            elif(userHand=="Rock"):
                if(computerHand=="Scissors"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Rock crushes Scissors")
                    userPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")

                elif(computerHand=="Paper"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Paper covers rock!")
                    computerPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")

                elif(computerHand=="Lizard"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Rock crushes Lizard!")
                    userPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")

                elif(computerHand=="Spock"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Spock vapourizes rock!")
                    computerPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")
                i+=1


            elif(userHand=="Paper"):
                if(computerHand=="Scissors"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Scissors cut Paper!")
                    computerPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")

                elif(computerHand=="Rock"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Paper covers rock!")
                    userPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")

                elif(computerHand=="Lizard"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Lizard eats paper!")
                    computerPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")
                    
                elif(computerHand=="Spock"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Paper disproves Spock!")
                    userPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")
                i+=1
                    

            elif(userHand=="Scissors"):
                if(computerHand=="Paper"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Scissors cut Paper!")
                    userPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")

                elif(computerHand=="Rock"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Rock crushes Scissors!")
                    computerPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")

                elif(computerHand=="Lizard"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Scissors decapitates lizard!")
                    userPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")
                    
                elif(computerHand=="Spock"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Spock smashes scissors!")
                    computerPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")
                i+=1

            elif(userHand=="Lizard"):
                if(computerHand=="Paper"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Lizard eats paper!")
                    userPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")

                elif(computerHand=="Rock"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Rock crushes Lizard!")
                    computerPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")

                elif(computerHand=="Scissors"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Scissors decapitates lizard!")
                    computerPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")
                    
                elif(computerHand=="Spock"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Lizard poisons Spock!")
                    userPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")
                i+=1

            elif(userHand=="Spock"):
                if(computerHand=="Paper"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Paper disproves Spock!")
                    computerPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")

                elif(computerHand=="Rock"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Spock vapourizes rock!")
                    userPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")

                elif(computerHand=="Scissors"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Spock smashes Scissors!")
                    userPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")
                    
                elif(computerHand=="Lizard"):
                    print("Computer played: ",computerHand)
                    print("User played: ", userHand)
                    print("Lizard poisons Spock!")
                    computerPoint+=1
                    print("Computer: ",computerPoint," || ","User: ",userPoint)
                    print("--------------------------\n")
                i+=1
        
    if(computerPoint>userPoint):
        print("Computer Wins!!! Better luck next time..")
        exit
    elif(userPoint>computerPoint):
        print("Congrats! You win!")
        exit
    else:
        print("Time for a tie breaker!")
        entireProcess(possibleMoves,userPoint,computerPoint,i=4,tie=True)

entireProcess(possibleMoves,userPoint,computerPoint,i=0,tie=False)



 
