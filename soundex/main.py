# pip install lxml
# pip install bs4

from bs4 import BeautifulSoup

soundex_dict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 0, 'F': 1, 'G': 2, 'H': 0, 'I': 0, 'J': 2,
    'K': 2, 'L': 4, 'M': 5, 'N': 5, 'O': 0, 'P': 1, 'Q': 2, 'R': 6, 'S': 2, 'T': 3,
    'U': 0, 'V': 1, 'W': 0, 'X': 2, 'Y': 0, 'Z': 2,

    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 0, 'f': 1, 'g': 2, 'h': 0, 'i': 0, 'j': 2,
    'k': 2, 'l': 4, 'm': 5, 'n': 5, 'o': 0, 'p': 1, 'q': 2, 'r': 6, 's': 2, 't': 3,
    'u': 0, 'v': 1, 'w': 0, 'x': 2, 'y': 0, 'z': 2,

    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
}


def soundex(str1):
    # cut one character off to be the first character
    first_char = str1[0]
    str1 = str1[1:]
    # make the number
    rest_number = 0
    for c in str1:
        temp_number = soundex_dict.get(c, 0)  # if you didn't find it, use 0
        if temp_number != rest_number % 10:  # if not repetitive
            rest_number = rest_number * 10 + temp_number
            if rest_number > 100000:
                break

    final_number = 0
    for c in str(rest_number):
        if int(c):
            final_number = final_number * 10 + int(c)  # remove 0s

    if final_number == 0:
        return first_char + "000"
    elif final_number > 1000:
        final_number %= 1000
    else:
        while final_number < 100:
            final_number *= 10  # Add trailing zeros

    return first_char + str(final_number)


def change_XML(file_in, file_out, url_strip):
    # read XML
    with open(file_in, 'r') as f:
        data = f.read()
    Bs_data = BeautifulSoup(data, "xml")

    # change XML
    for i in Bs_data.findAll('loc'):
        untokenized = i.text
        stripped = untokenized.strip(url_strip)
        new_stripped = ""
        if stripped:  # sometimes, it's empty
            for part in stripped.split('/'):  # tokenize by /
                if part:  # if a / is at the end, an empty array is made. This fixes that
                    for smidge in part.split('-'):  # tokenize by -
                        if smidge:  # if an - is at the end, an empty array is made. This fixes that
                            print(smidge)
                            smidge = soundex(smidge)  # run soundex
                            print(smidge)
                            new_stripped += smidge + "-"
                    new_stripped = new_stripped.strip('-')
                    new_stripped += "/"  # the last - becomes a /
        i.string = url_strip + new_stripped

    # write XML
    with open(file_out, 'w') as f:
        f.write(Bs_data.prettify())


# print(soundex("Narges Mohammadi"))
change_XML('sitemap.xml', 'output.xml', 'https://www.apple.com/')
# change_XML('sitemap copy.xml', 'output.xml', 'https://www.apple.com/')