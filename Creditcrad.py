ccnumber = input("Please enter the credit card number ")


def validator(ccnumber):
    validnumber = []
    multiplynumber = 0
    sum = 0
    for i in range(len(ccnumber)):
        validnumber.append(ccnumber[i])
    validnumber.reverse()

    for j in range(len(validnumber)):
        if j % 2 != 0:
            multiplynumber = int(validnumber[j]) * 2
            if multiplynumber > 9:
                sum += multiplynumber % 10 + multiplynumber // 10
            else:
                sum += multiplynumber
        else:
            sum += int(validnumber[j])

    if sum % 10 == 0:
        return bool
        # print("Card is legit")
    # else:
    # print("Enter correct credit card number")


def cc(ccnumber):
    abc = int(ccnumber[:2])
    if abc // 10 == 4 and validator(ccnumber):
        print("Visa")
    if abc == 34 or abc ==37 and validator(ccnumber) :
         print("American Express ")
    if abc > 50 and abc <=55 and validator(ccnumber):
        print("Master Card ")
    else :
        print("Please enter correct credit card number ")
# validator(ccnumber)


cc(ccnumber)
