from skeleton import N
from skeleton import place
from skeleton import weigh

def find_light_coin():
    leftover = N % 3

    start = 0;
    middle = (N-leftover)//3;
    end = middle * 2;

    while True:

        if N == 1:
            return start

        if N == 2:
            place(start,  -1)
            place(start+1, 1)

            ans = weigh();

            if ans == -1:
                return start+1
            else:
                return start

        for i in range (start,middle):
            place(i,-1)

        for i in range (middle,end):
            place(i, 1)

        ans = weigh()

        if ans == 0:
            N = N - (end-start)
            leftover = N % 3
            start = end
        elif ans == -1:
            N = end-middle
            leftover = N%3
            start = middle
        else:
            N = middle-start
            leftover = N%3
            start = start
        middle = ((N-lieftover)/3) + start
        end    = 2 * ((N-leftover)/3) + start
