'''QUIZ PROJECT GDSC'''
import Blueprint
count=0
l1=[]
l2=[]

j=Blueprint.Question()
a=0
d1={}

class Quiz:
    def startquiz(self):
            global count, l1, l2, a, d1
            for i in j.question_data:
                a+=1
                print(i["text"])
                t=input("Answer(A) or Skip(S)?(A/S): ")
                if t=="S":
                    l2.append("Skipped (0)")
                    l1.append(i)
                    d1[i["text"]]=a-1
                    print()
                    continue
                else:
                    
                    k=input("Enter your answer in 'True' or 'False': ")
                    if k==i["answer"]:
                         l2.append("Correct! (+2)")
                         count+=2
                    else:
                         l2.append("Wrong! (-1)")
                         count-=1
                print()


    def reattempt(self):
         global l1, count, l2, d1
         f=input("Do you wish to reattempt the questions you Skipped?(Y/N): ")
         if f=="Y":
            for i in l1:
                print(i["text"])
                t=input("Answer(A) or Skip(S)?(A/S): ")
                if t=="S":
                    continue
                else:
                    k=input("Enter your answer in 'True' or 'False': ")
                    if k==i["answer"]:
                            count+=2
                            l2[d1[i["text"]]]="Correct! (+2)"
                            
                    else:
                            count-=1
                            l2[d1[i["text"]]]="Wrong! (-1)"
    def checkans(self):
         global l2
         for g in l2:
              print(g)
    

              
c=Quiz()
print("Welcome to the quiz")
print("You will be awarded (+2) for each Correct answer and (-1) for each Wrong answer")
while True:
    u=input("ARE YOU READY?(Y/N): ")
    if u=='Y':
            print("Alright, let's Start!!")
            c.startquiz()
            c.reattempt()
            s=input('Congrats! you\'ve completed the quiz, would you like to see your score(Score) or answers(Ans) (or both(Both))?: ')
            if s=="Score":
               print('Your total score is:', count)
            elif s=="Ans":
                 c.checkans()
            else:
               print('Your total score is:', count)
               print("And your answers are:")
               c.checkans()
            print("Thanks for playing!!!")
            break
    
    else:
         print("Come prepared next time!")
         break
     