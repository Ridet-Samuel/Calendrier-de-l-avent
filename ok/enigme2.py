if __name__ == '__main__' :
    fichier = open('input.txt', 'r')
    content = fichier.read()

    montableau = [ int(i) for i in content.split('\n')]

    for it in montableau :
        for jt in montableau :
            for kt in montableau :

                sum = it + jt + kt

                if sum == 2020 :
                    print(it*jt*kt)