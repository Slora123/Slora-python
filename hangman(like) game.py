words=["cat", "dog", "horse", "cow"]
remaining_words=words.copy()
letter_collection=[]
attempts=5
while attempts>0 and len(remaining_words)>1:
    new_remaining_words=[]
    guess=input("Guess the letter of the word:-")
    for word in remaining_words:
        if guess in word:
            new_remaining_words.append(word) 
    if new_remaining_words!=[]:
        print("Yes!")
        remaining_words=new_remaining_words
        letter_collection.append(guess)
        print("Letters of the word:-",letter_collection)
        print("Words Remaining:",len(remaining_words))
    else:
        print("No")
        attempts-= 1
    print("Remaining attempts:", attempts)
if len(remaining_words)==1:
    guess_word=input("Guess entire word:")
    if guess_word==remaining_words[0]:
        print("Yes it's ",remaining_words [0])
        print ("You Win!")
    else:
        print("No.. its", remaining_words[0])
        print("You Lose")
elif attempts==0:
    print("You are out of attempts")