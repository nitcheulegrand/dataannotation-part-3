import math

with open('a.txt') as f:
    tLines = []
    for line in f:
        tLines.append(line.split(" "))
    tLines = sorted(tLines, key=lambda x: x[0])
    # First vérifications
    index = 0
    for line in tLines:
        if index==0 and int(tLines[index][0]) != 1 or index > 0 and int(tLines[index-1][0]) != int(tLines[index][0]) - 1:
            print("Bad encoding: missing key.")
            exit(1)
            # A key is missing
        index = index + 1
    # Encoding
    n = len(tLines)
    N = math.floor(math.sqrt(n))
    step = 1
    result = []
    while len(tLines)>0 and len(tLines)>=step:
        subTLines = tLines[0:step]
        tLines = tLines[step:]
        result.append(subTLines[-1])
        step = step + 1
    # Last decoding step verification
    if len(tLines)>0 and len(tLines)<step:
        print("Bad encoding: wrong decoding piramid.")
        exit(1)
    print(''.join([' '.join(x) for x in result]))