import os
wordcount = 0
alphacount={}

def process(filename):
    global wordcount
    global alphacount
    f = open(filename,'r')
    for line in f:
        a = line.strip().split(" ")
        for word in a:
            wordcount +=1          
            for letter in word:
                if letter not in alphacount:
                    alphacount[letter] = 1

                else:
                    alphacount[letter] += 1


def print_wordcount():
    print(wordcount)

def print_alpha():
    for k,v in sorted(alphacount.items()):
        print("{} {:d}".format(k,v))



if __name__ == "__main__":
    filename="hamlet.txt"
    path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(path,filename)
    process(filename)
    print_wordcount()
    print_alpha()


