def engg_check(s: str):
    if s == "GG":
        return "true"
    else:
        s = list(s)
        if (s[0] == "e" or s[0] == "E") and s[1] == "N" :
            s.pop(0)
            while s[0] == "N":
                s.pop(0)
            s = "".join(s)
            return engg_check(s)
        else:
            return "false"


print(engg_check("ENGG"))