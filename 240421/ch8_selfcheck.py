with open("class.txt", "r", encoding="utf8") as f :
    txt = f.read()
    words = txt.split()
    for word in words :
        print(word, end=" ")
        if word.endswith("명") :
            print()