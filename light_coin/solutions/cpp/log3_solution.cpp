int find_light_coin()
{
    int start, middle, end, leftover;

    leftover = N % 3;

    start = 0;
    middle = (N-leftover)/3;
    end = middle * 2;

    while (1)
    {
        if (N == 1) return start;

        if (N == 2)
        {
            place(start, -1);
            place(start+1, 1);

            int ans =  weigh();

            if (ans == -1) return start+1;
            else return start;
        }

        for (int i = start; i < middle; ++i) place(i, -1);

        for (int i = middle; i < end; ++i) place(i, 1);

        int ans =  weigh();

        if (ans == 0)
        {
            N = N - (end-start);
            leftover = N%3;

            start = end;
        }
        else if (ans == -1)
        {
            N = end-middle;
            leftover = N%3;

            start = middle;
        }
        else
        {
            N = middle-start;
            leftover = N%3;

            start = start;
        }

        middle = ((N-leftover)/3) + start;
        end = 2*((N-leftover)/3) + start;
    }
}
