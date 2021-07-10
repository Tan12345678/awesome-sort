'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


def awesomesort(Array, n):
    evenlist = []
    oddlist = []
    odd5 = []
    modioddlist = []
    flag = 0

    for i in range(0, n):
        if (Array[i] % 2 == 0):
            evenlist.append(Array[i])
        else:
            oddlist.append(Array[i])
            flag = 2
            xodd = oddlist.copy()
            y2 = len(oddlist)
    for i in range(0, y2):
        if (oddlist[i] % 5 == 0):
            odd5.append(oddlist[i])
            x1 = len(odd5)
        else:
            modioddlist.append(oddlist[i])
    if (x1 > 1):
        flag = 1
        odd5.sort(reverse=True)
    else:
        pass

    print("Even lists:", evenlist)
    print("Odd lists:", oddlist)
    print("odd 5", odd5)
    print("modiodd", modioddlist)

    temp1 = []
    temp2 = []
    for i in range(len(evenlist)):
        if (evenlist[i] % 5 == 0):

            temp1.append(evenlist[i])
            temp1.sort(reverse=True)

        else:

            temp2.append(evenlist[i])
            temp2.sort(reverse=True)
    print("temp1", temp1)
    print("temp2", temp2)
    print(oddlist)

    '''for i in range(len(oddlist)):
        if(oddlist[i]%5==0):
            odd5.append(oddlist[i])
            odd5.sort(reverse=True)
        else:
            odd6.append(oddlist[i])


    '''

    '''if(y==1):
        lenodd5=odd5.copy()
        print("lenodd5",lenodd5)
        return temp1+temp2+lenodd5+oddlist'''
    # else:
    if (flag == 1):
        return temp1 + temp2 + odd5 + modioddlist
    elif (flag == 2):
        return temp1 + temp2 + oddlist


# Driver Code
t = int(input())
for i in range(t):
    n = int(input())  # for size
    Array = list(map(int, input().split(' ')[:n]))
    out = awesomesort(Array, n)
    print(' '.join(map(str, out)))