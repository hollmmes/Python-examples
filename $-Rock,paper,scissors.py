import random

ihtimaller=["rock","paper","scissors"]
computer=random.choice(ihtimaller)

player= None
while player not in ihtimaller: # player ihtimaller içerisinden bir şey yazmadığı sürece loopa girdi
    player=input("Rock Paper Scissors?: ").lower() # .lower ile büyük harflerle girsekte küçültecek böylelikle karışmayacak

if player == computer:
    print("Computer: ",computer)
    print("Player: ",player)
    print("Berabere!")
elif player == "rock" :
    if computer == "paper":
        print("Computer: ",computer)
        print("Player: ",player)      
        print("Kağıt taşı yener, Pc kazandı!")
    if computer == "scissors":
        print("Computer: ",computer)
        print("Player: ",player)      
        print("Taş makası yener, Oyuncu kazandı!")
elif player == "scissors" :
    if computer == "paper":
        print("Computer: ",computer)
        print("Player: ",player)      
        print("Makas kağıdı yener, Oyuncu kazandı!")
    if computer == "rock":
        print("Computer: ",computer)
        print("Player: ",player)      
        print("Taş makası yener, Oyuncu kazandı!")
