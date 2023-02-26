def roman(number):
    n_r = {
        1000:'M',
        900 :'CM',
        500 : 'D',
        400 : 'CD',
        100 : 'C',
        90 : 'XC',
        50 : 'L',
        40 : 'XL',
        10 : 'X',
        5 : 'V',
        4 : 'IV',
        1: 'I'
    }
    roman = ""
    for num in n_r:
        while(number>=num):
            roman += n_r[num]
            number -= num
    return roman

if __name__ == "__main__":
    number = int(input("Enter a number : "))
    print(roman(number))