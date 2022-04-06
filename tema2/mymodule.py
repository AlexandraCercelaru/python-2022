def functie_1(param_1):
    if param_1 == 0:
        return 0
    return param_1 + functie_1(param_1 - 1)


def functie_2(param_2):
    if param_2 == 0:
        return 0
    elif param_2 % 2 == 0:
        return param_2 + functie_2(param_2 - 1)
    else:
        return functie_2(param_2 - 1)


def functie_3(param_3):
    if param_3 == 0:
        return 0
    elif param_3 % 2 != 0:
        return param_3 + functie_3(param_3 - 1)
    else:
        return functie_3(param_3 - 1)
