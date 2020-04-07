# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()
def censor_one(text, word):
    censor_word = ""
    for i in range(0, len(word)):
        if word[i] == " ":
            censor_word += " "
        else:
            censor_word += "X"
    return text.replace(word, censor_word)

def censor_two(text, words):
    for word in words:
        censor_word = ""
        for i in range(0, len(word)):
            if word[i] == " ":
                censor_word += " "
            else:
                censor_word += "X"
        text = text.replace(word, censor_word)
    return text

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

with open("email_one_censor.txt", "w") as file:
    file.write(censor_one(email_one, "learning algorithms"))

with open("email_two_censor.txt", "w") as file:
    file.write(censor_two(email_two, proprietary_terms ))