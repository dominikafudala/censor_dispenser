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

def censor_three(text, words1, words2):
    text = censor_two(text, words1)
    count_word = 0
    i = 0
    while i < len(text):
        k = 0
        while k < len(words2):
            x = len(words2[k])
            word = words2[k]
            tekst = text[i: i+x]
            if tekst == word or tekst == word.title():
                if count_word < 2:
                    count_word += 1
                else:
                    censor_word = ""
                    for j in range(0, len(word)):
                        if word[j] == " ":
                            censor_word += " "
                        else:
                            censor_word += "X"
                    text = text.replace(text[i: i+x], censor_word)
            k += 1
        i+=1
    return text

def censor_four(text, words1, words2):
    text = censor_three(text, words1, words2)
    podzial = []
    i = 0
    for x in text.split(" "):
        x2 = x.split("\n")
        for x3 in x2:
            podzial.append(x3)
    # censoring words before and after censored words
    while i < len(podzial):
        if "XX" in podzial[i]:
            word = podzial[i+1]
            censored_word = ""
            for j in range(len(word)):
                    if word[j] == " ":
                        censored_word += " "
                    else:
                        censored_word += "X"
            podzial[i + 1] = podzial[i+1].replace(word, censored_word)
            if (i - 1) > -1:
                word = podzial[i - 1]
                censored_word = ""
                for j in range(len(word)):
                    if word[j] == " ":
                        censored_word += " "
                    else:
                        censored_word += "X"
                podzial[i-1] = podzial[i -1].replace(word, censored_word)
            i = i + 3
        i += 1
    text = " ".join(podzial)
    text = text.replace("  ", "\n")
    return text

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "herself", "her" ]
negative_words = ["concerned","behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "distressing", "reduction", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

with open("email_one_censor.txt", "w") as file:
    file.write(censor_one(email_one, "learning algorithms"))

with open("email_two_censor.txt", "w") as file:
    file.write(censor_two(email_two, proprietary_terms ))

with open("email_three_censor.txt", "w") as file:
    file.write(censor_three(email_three, proprietary_terms,negative_words))

with open("email_four_censor.txt", "w") as file:
    file.write(censor_four(email_four, proprietary_terms, negative_words))