def new_game():
    
    correct_guesses=0
    question_num=1
    guesses=[]

    for key in questions:
        print("-"*25)
        print(key) #soruları çağırıyoruz
        for i in options[question_num-1]: 
            print(i) # şıkları çağırıyoruz
        guess= input("Cevap?. (A,B,C,D)").upper() #girilen değeri upper ile büyük yapıyoruz
        guesses.append(guess)
        
        correct_guesses+= check_answer(questions.get(key),guess) #doğru cevabı ve kendi cevabımızı yolluyoruz ve geri dönen doğru cevap puanlarını topluyoruz
        question_num+=1

    display_score(correct_guesses,guesses)
    
        
#-------------------------
def check_answer(answer, guess):
    
    if answer== guess: #verilen cevaplar ile doğru cevap eşlenirse 1 dönderip doğru yazdıracak
        print("Doğru!")
        return 1
    else:
        print("Yanlış!")
        return 0
        
#-------------------------
def display_score(corr, guesses):
    
    print("-"*31)
    print("Sonuçlar!!!")
    print("-"*31)
    print("Doğru Cevaplar: " ,end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    
    print("Sizin cevaplarınız: " ,end="")
    for i in guesses:
        print(i, end=" ")
    print()
    
    skor= int((corr/len(questions))*100)
    print("Skorunuz: %"+str(skor))
    
#-------------------------
def play_again():
    replay=input("Oynucan mı yeniden?: (yes or no) ").upper()
    if replay=="YES":
        return True
    else:
        return False

#-------------------------

questions = {
    "Who created this code: ": "A",
    "Is there a god: ": "B",
    "Are you happy?: ": "D",
}

options =[["A. Ben","B. Allah","C. Annen","D. Bill Gates"],
          ["A. Yok","B. Yokki","C. Var","D. Yedim"],
          ["A. Evet","B. Hiçte bile","C. Keşke","D. Hayır"]]

new_game()

while play_again():
    new_game()
print("Game finished")
