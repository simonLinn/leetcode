def numJewelsInStones(J: str, S: str) -> int:
    count = 0
    for lj in J:
        for ls in S:
            if lj==ls:
                count+=1
    return count
J = "aA"
S = "aAAbbbb"
print(numJewelsInStones(J,S))