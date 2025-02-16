import random
print(r'''
 _   _                                            ____                      _ 
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __    / ___| __ _ _ __ ___   ___| |
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  | |  _ / _` | '_ ` _ \ / _ \ |
|  _  | (_| | | | | (_| | | | | | | (_| | | | | | |_| | (_| | | | | | |  __/_|
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|  \____|\__,_|_| |_| |_|\___(_)
                   |___/                                                                        
      ''')
stages=[  '''
    +----+      
    |    |
         |
         |        
         |
         | ''','''
    +----+
    |    |
    O    |
         |
         |
         |
    ''','''
    +----+
    |    |
    O    |
    |    |
         |
         |
    ''','''
    +----+
    |    |
    O    |
  / |    |
         |
         |
    ''','''
    +----+
    |    |
    O    |
  / | \  |
         |
         |
    ''','''
    +----+
    |    |
    O    |
  / | \  |
   /     |
         |
    ''','''
    +----+
    |    |
    O    |
  / | \  |
   / \   |
         |
    '''
]
lives=6
l3=["devdas","coolie no 1","bade miyan chote miyan","patthar ke phool","baazigar","shahenshah"]
word=random.choice(l3)
l1=[]
for i in range(len(word)):
    l1.append("_")
print(l1)
l2=[i for i in word]
print("You have 6 lives to correctly guess the word")
print(stages[6])
while(True):
    guess=input("Enter the letter:").lower()
    for index,char in enumerate(word):
        if(guess==char):
            l1[index]=guess
    if guess not in word:
        lives=lives-1
        print(f"You have {lives} chances left")
    print(l1)
    if(lives==0):
        print("Game Ends.You Lose!")
        break
    if(l1==l2):
        break
    print(stages[lives])