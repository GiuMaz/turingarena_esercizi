int individua(int n)
{
    int start, middle, end, leftover, initial_n;
    initial_n = n;

    leftover = n % 3;

    start = 0;
    middle = (n-leftover)/3;
    end = middle * 2;

    while (1)
    {
        for( int i = 0; i<initial_n; i++)
            collocaMoneta(i, 0);

        if (n == 1) return start; //denuncia(start);

        if (n == 2)
        {
            collocaMoneta(start, -1);
            collocaMoneta(start+1, 1);

            int risp =  piatto_con_peso_maggiore();

            if (risp == -1) return start+1; //denuncia(start+1);
            else return start; //denuncia(start);
        }

        for (int i = start; i < middle; ++i) collocaMoneta(i, -1);

        for (int i = middle; i < end; ++i) collocaMoneta(i, 1);

        int risp =  piatto_con_peso_maggiore();

        if (risp == 0)
        {
            n = n - (end-start);
            leftover = n%3;

            start = end;
        }
        else if (risp == -1)
        {
            n = end-middle;
            leftover = n%3;

            start = middle;
        }
        else
        {
            n = middle-start;
            leftover = n%3;

            start = start;
        }

        middle = ((n-leftover)/3) + start;
        end = 2*((n-leftover)/3) + start;
    }
}
