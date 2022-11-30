def validPasswordCheck(password: str):
    lengthPass = len(password)
    specialChar = False
    number = False
    lowerCase = False
    upperCase = False
    lowestNumber = 13
    highestNumber = 25

    if(lengthPass < lowestNumber or lengthPass > highestNumber):
        return False

    for char in password:
        if(allowedSpecialChar(char)):
            specialChar = True
        if(char.isnumeric()):
           number = True
        if(char.islower()):
            lowerCase = True
        if(char.isupper()):
            upperCase = True
        if(specialChar and number and lowerCase and upperCase):
            return True
    return False

def allowedSpecialChar(charToCheck: chr):
    if(charToCheck == '!' or charToCheck == '@' or charToCheck == '#' or charToCheck == '$' or charToCheck == '%' or charToCheck == '&' or charToCheck == '*' or charToCheck == '(' or charToCheck == ')'):
        return True
    return False

#print(validPasswordCheck("DlGkS!2#4%6&8(0"))
#print(validPasswordCheck("D12312312312311233"))
#The valid password requires at least one special character from (!@#$%&*()), and at least one number, and at least one lower case letter and at least one uppercase letter.
#The valid password should have minimum of 13 characters and maximum of 25 characters.
