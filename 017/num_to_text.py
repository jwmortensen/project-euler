ones = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
teens = {
    0: "ten",
    1: "eleven",
    2: "twelve",
    3: "thirteen",
    4: "fourteen",
    5: "fifteen",
    6: "sixteen",
    7: "seventeen",
    8: "eighteen",
    9: "nineteen"
}
tens = {
    0: "",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}


def num_to_string(num):
    string = ""
    hund = num // 100
    ten = num % 100 // 10
    one = num % 10
    if hund > 0:
        string += ones[hund] + "hundred"
    if len(string) > 0 and (ten > 0 or one > 0):
        string += "and"
    if ten > 1:
        string += tens[ten]
    elif ten == 1:
        string += teens[one]
    if ten != 1:
        string += ones[one]
    return string


number_name = "onethousand"
for i in range(1, 1000):
    number_name += num_to_string(i)
print(len(number_name))

