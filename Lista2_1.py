from test.test_MimeWriter import OUTPUT
def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]

def statystyki():
    tablicaSlow = read_words("tekst.txt")
    #print tablicaSlow

    keys = []
    values = []
    dictionary = dict(zip(keys, values))
    for slowo in tablicaSlow:
        if slowo in dictionary:
            dictionary[slowo] = int(dictionary[slowo]) + int('1')
        else:
            dictionary[slowo] = int('1')

    f=open('statistics.txt','w+')
    for slowo, ilosc in dictionary.items():
        f.write(slowo + " : ")
        f.write(str(ilosc) + "\n")       
    f.close()
            
   
statystyki()