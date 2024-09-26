#write program that captalizes the first letter and last letter of the sentances:
def captalize_first_and_last_letter(sentance: str):
    words = sentance.split()
    captilize_words = []
    for word in words:
        if len(word) > 1:
            captilize_word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            captilize_word= word.upper()
        captilize_words.append(captilize_words)    
    return ''.join(captilize_words)        
x= input("enter the words")
print(captalize_first_and_last_letter(x))