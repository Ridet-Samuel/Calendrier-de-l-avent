if __name__ == '__main__' :
    fichier = open('input2.txt', 'r')
    content = fichier.read()

mdpok=0
montableau = [i for i in content.split('\n')]

for x in montableau :
    S= x.split(' ')
    pos1 = int(S[0].split('-')[0])
    pos2 = int(S[0].split('-')[1])
    mdp = S[2]
    lettre=S[1].split(":")[0]

    if mdp[pos1-1]==lettre and mdp[pos1-1]!=mdp[pos2-1] :
        mdpok=mdpok+1

    if mdp[pos2-1]==lettre and mdp[pos1-1]!=mdp[pos2-1] :
        mdpok=mdpok+1

print(mdpok)
