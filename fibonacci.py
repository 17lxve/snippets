#Recursive version

def f(a) :
    if a < 0 :
        return
    if a == 0:
        return 0
    elif a == 1:
        return 1
    else:
        return f(a-1) + f(a-2)

#Iterative version

def f2(a):
    l = [0,1]
    for x in range(2, a + 1):
        l.append(l[x-2] + l[x-1])
    return l[a]

#Dynamic version

sol = [0,1]

def f3(a):
    if a < len(sol) :
        return sol[a]
    elif a >= len(sol) :
        for x in range(len(sol), a+1):
            sol.append(sol[x-1] + sol[x-2])
            #print(sol)
        return sol[a]

#Functions

def give(begin, end, step):
    x = 0
    for i in range(begin, end+1):
        x += f3(i)
    ans = (x%step == 0) 
    if ans == True:
        print("F_{} + ... + F_{} is divisible by {}".format(begin,end,step))
    else:
        print("F_{} + ... + F_{} is NOT divisible by {}".format(begin,end,step))


def main():
    nb = int(input())
    for i in range(nb):
        a, b, d = [int(j) for j in input().split()]
        give(a,b,d)

def test():
    nb = int(input("Iterative test : "))
    for t in range(nb):
        print(f2(t))

def test2():
    nb = int(input("Recursive test : "))
    for t in range(nb):
        print(f(t))

def test3():
    nb = int(input("Dynamic test : "))
    for t in range(nb):
        print(f3(t))

#Tests

#test()
#test2()
#test3()

#Run 

main()