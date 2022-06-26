def countwords():
    filename = input("enter the file name:")
    noofwords = 0
    file = open(filename,"r")
    for line in file:
        words = line.split()
        noofwords += len(words)
    print("number of words = ",noofwords)

countwords()