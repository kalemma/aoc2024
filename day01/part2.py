def main():
    getInput()

def getInput():
    nrdict = {}
    leftnr = []
    rightnr = []
    with open("input.txt") as f:
        for line in f:
            leftnr.append(int(line.split("   ")[0]))
            rightnr.append(int(line.split("   ")[1]))


    leftnr.sort()
    for nr in leftnr:
        nrdict[nr] = rightnr.count(nr)


    sums = 0
    for k, v in nrdict.items():
        sums += k*v
    print(sums)


if __name__ == '__main__':
    main()