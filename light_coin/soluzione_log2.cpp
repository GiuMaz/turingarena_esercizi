int find_light_coin()
{
    int start, middle, end, leftover;

    leftover = N % 2;

    start = 0;
    middle = (N-leftover)/2;
    end = N-leftover;

    while (1)
    {
        if (N == 1) return start;

        for (int i = start; i < middle; ++i) place(i, -1);

        for (int i = middle; i < end; ++i) place(i, 1);

        int ans =  weigh();

        if (ans == 0)
            return end;
        else if (ans == -1)
            start = middle;
        else
            end = middle;

        N = end-start;
        leftover = N%2;
        end-=leftover;
        middle = ((N-leftover)/2) + start;
    }
}
