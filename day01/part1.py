def main():
    process_input(get_input())

def process_input(file):
    leftnr = []
    rightnr = []
    with open(file) as f:
        for line in f:
            leftnr.append(int(line.split("   ")[0]))
            rightnr.append(int(line.split("   ")[1]))

    leftnr.sort()
    rightnr.sort()
    sums = 0
    for i in range(len(leftnr)):
        sums += rightnr[i] - leftnr[i] if rightnr[i] > leftnr[i] else leftnr[i] - rightnr[i]

    print(sums)

def get_input():
    return "input.txt"

if __name__ == "__main__":
    main()