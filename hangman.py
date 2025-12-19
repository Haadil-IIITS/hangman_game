import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("WELCOME TO HANGMAN GAME\nHERE U HAVE TO FIND THE MISSING LETTERS BEFORE THE PERSON GET HANGED\nENJOY THE GAME")
word_list = ["cheetah", "kangaroo","monkey","camel","tiger","horse","lion","donkey"]
word=list(random.choice(word_list))
hangman=0
finalword=list()
print("lenght of word is :",len(word))
for i in range(len(word)):
    finalword.insert(i,'_')
print(" ".join(finalword))
while hangman<6:
    x=str(input("enter letter: "))
    if x not in finalword:
        for i in range(len(word)):
            if word[i]==x:
                finalword[i]=x
    else:
        print("the letter already exist")
    if x not in word:
        print(stages[6-hangman])
        hangman+=1
        print("ur wrong: ")
        print("lives left :",6-hangman)
        
    if '_' not in finalword:
        print("u won")
        print(" ".join(finalword))
        break
    print(" ".join(finalword))
if(hangman==6):
    print(stages[0])
    print("u lose")

