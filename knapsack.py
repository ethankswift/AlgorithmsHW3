def getInput():
    try:
        infile = open('data.txt', 'r')
    except IOError:
        print("File IO Error")
        quit()
    finally:
        return infile.read()

def knapSack(W, items, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif items[i-1][0] <= w:
                K[i][w] = max(items[i-1][1] + K[i-1][w-items[i-1][0]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K

def knapSackOptimal(K, W, items, n):
    optItems = []
    res = K[n][W]
    w = W
    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == K[i - 1][w]:
            continue
        else:
            optItems.append(i - 1)
            res = res - items[i - 1][1]
            w = w - items[i - 1][0]
    return optItems

def main():
    test = getInput().rstrip()
    list = test.split('\n')
    for i in range(len(list)):
        list[i] = list[i].split(' ')
        list[i][0] = int(list[i][0])
        list[i][1] = int(list[i][1])
    cap = int(input("What is the capacity of your sack?\n"))
    matrix = knapSack(cap,list,len(list))
    print("The most value you can put in your sack is: ", matrix[len(list)][cap])
    optItems = knapSackOptimal(matrix, cap, list, len(list))
    print("The optimal subset was made of these items: ")
    for i in range(len(optItems)):
        print("Item ", optItems[i], " Weight: ", list[optItems[i]][0], " Value: ", list[optItems[i]][1])
    return 0

main()
