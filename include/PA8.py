def engg(S: str):
    if len(S) < 4:
        if S == "GG":
            return "true"
        else:
            return "false"
    else:
        S = list(S)
        if S[0] == "e" or S[0] == "E":
            S.pop(0)
            while S[0] == "N":
                S.pop(0)
        else:
            return "false"
        S = "".join(S)
        return engg(S)


inparr = []
testcases = int(input())
for i in range(testcases):
    inparr.append(input())

for x in inparr:
    print(engg(x))
