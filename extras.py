import os
import math

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def new_page(term_size, page):
    clear()

    print("#" * term_size.columns)
    print("DOCKER DOWNLOAD INSTALL SCRIPT".center(term_size.columns, "-"))

    # This gets how many lines the descripting will span plus how many choices there are to display
    # It also adds 7 for the blank space, choice section, and header.
    span = (math.ceil(len(page[0]) / term_size.columns)) + (len(page) - 1) + 7

    print("\n" * (term_size.lines - span))
    print(page[0])

    print("")

    for i in range(len(page) - 1):
        print(str(i + 1) + ".) " + page[i + 1])

    print("")

    print(">>")
