if __name__ == '__main__':
    palindrome = "Un radata na."
    liste_palindrome = list(palindrome)
    print(liste_palindrome)
    liste_palindrome[0] = "u"
    liste_palindrome[7] = "r"
    liste_palindrome[3] = "u"
    liste_palindrome.remove(".")
    del liste_palindrome[2], liste_palindrome[8], liste_palindrome[9]

    liste_palindrome_inversee = liste_palindrome[::-1]
    for i in liste_palindrome:
        print(i)

    print()

    for a in liste_palindrome_inversee:
        print(a)