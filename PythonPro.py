phone_number = input(">>")

phone = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"zero"
}
output = ""
for number in phone_number:
    output += phone.get(number) + " "
print(output)