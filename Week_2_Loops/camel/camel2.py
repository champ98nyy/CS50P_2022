def main():
    # camel = input('cameCase Name: ')
    camel = input('camelCase Name: ').strip()

    # camel = to_snake(camel)
    camel = to_snake(camel)

    print("FINAL: ", camel)


def to_snake(camel):
    camel = list(camel)

    print(camel) # ['c', 'a', 'm', 'e', 'l', 'C', 'a', 's', 'e']

    letters = []
    for char in camel:
        if char.isupper() == True:
            lower = "_" + char.lower()
        else:
            lower = char
        letters.append(lower)
        print("Letters: ", letters)


    return ''.join(letters)



if __name__ == "__main__":
    main()