import sys
import googletrans
from googletrans import Translator

words = []
dict = {}


try:
    book_name = sys.argv[1]
except:
    f"dsgg"




with open(f"{book_name}.txt", encoding="utf8") as file:
    lines = file.readlines()




for line in lines:
    line_words = line.split(" ")
    for word in line_words:
        word = word.lower()
        word = word.strip("«»»)(-—1234567890…\/!¡¿?:;.,\n")
        words.append(word)


for _ in range(len(words)-1):

    count=1
    for i in range(1, len(words)):
        if words[0] == words[i]:
            count+=1

    dict[f"{words[0]}"] = count


    first_word = words[0]
    for i in range(len(words)-1):
        words[i] = words[i+1]
    words[len(words)-1] = first_word




sorted_list = sorted(dict.items(), key=lambda x: (-x[1], x[0]))


with open(f"{sys.argv[1]}_freq.txt", "w") as file:
    file.write("")

# print(dict)

for word in sorted_list:
#    print(f"{word[0]} - {word[1]}")

    translator = Translator()
    try:
        translation = translator.translate(word[0], dest="en", src='es')
    except:
        translation.text = ">>>>>>>"

    sp = translation.text

    with open(f"{sys.argv[1]}_freq2.txt", "a", encoding="utf8") as file:
    #    file.write(f"{word[0]} -  - {word[1]}\n")
        file.write(f"{word[0]} - {sp} - {word[1]}\n")



