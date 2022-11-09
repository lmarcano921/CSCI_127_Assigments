#Luis A Marcano
#10/15/2022
#luis.marcano29@myhunter.cuny.edu

def computePrice(liquid, type):

    if liquid == "coffee":
        if type == "small":
            return 2.5
        elif type == "medium":
            return 2.75
        elif type == "large":
            return 3.00
        else:
            return -1

    elif liquid == "misto":
        if type == "small":
            return 3.15
        elif type == "medium":
            return 3.35

        elif type == "large":
            return 3.7
        else:
            return -1

    elif liquid == "mocha":
        if type == "small":
            return 3.5
        elif type == "medium":
            return 3.8
        elif type == "large":
            return 4.25
        else:
            return -1

    elif liquid == "tea":
        if type == "small":
            return 2.35
        elif type == "medium":
            return 2.45
        elif type == "large":
            return 2.90
        else:
            return -1
    else:
        return -1