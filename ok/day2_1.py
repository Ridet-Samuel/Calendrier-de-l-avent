if __name__ == '__main__' :
    fichier = open('input2.txt', 'r')
    content = fichier.read()

mdpok=0
montableau = [i for i in content.split('\n')]

for x in montableau :
    S= x.split(' ')
    min = int(S[0].split('-')[0])
    max = int(S[0].split('-')[1])
    mdp = S[2]
    lettre=S[1].split(":")[0]

    nb=mdp.count(lettre)

    if min<=nb<=max :
        mdpok=mdpok+1


print (mdpok)



