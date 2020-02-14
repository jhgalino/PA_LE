def engg_check(s: str):
    if len(s) < 4:
        return "false"
    else:
        s = list(s)
        if (s[0] == "e" or s[0] == "E") and s[1] == "N" :
            s.pop(0)
            while s[0] == "N":
                s.pop(0)
            s = "".join(s)
            if s == "GG":
                return "true"
            else:
                return engg_check(s)
        else:
            return "false"


inparr = []
testcases = int(input())
for i in range(testcases):
    inparr.append(input())

for x in inparr:
    print(engg_check(x))