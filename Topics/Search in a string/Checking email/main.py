def check_email(string):
    if string.count(" ") > 0 or string.count("@") < 1:
        return False
    elif string[string.index("@") + 2:len(string)].find(".") < 0:
        return False
    elif string[len(string) - 1] == ".":
        return False
    # elif len(string) < 5:
    #     return False
    # elif string.find("@") == 0:
    #     return False
    # elif string.find(".") == 0:
    #     return False
    else:
        return True

# print(check_email("good.email@examplecom."))
# print(check_email("goodemail@example.com"))
