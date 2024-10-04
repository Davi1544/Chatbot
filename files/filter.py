import codecs

five = set()
with open("files/dicio.txt", 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if(len(line) == 5):
            line = line.lower()
            five.add(line)

with codecs.open("words.txt", "w", "utf-8") as txt_file:
    for line in five:
        txt_file.write(line + "\n")

print(five)