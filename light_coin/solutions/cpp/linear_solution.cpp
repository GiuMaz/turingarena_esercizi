int find_light_coin()
{
    int ans;
    place(0,-1);
    place(1,1);
    ans = weigh();
    if (ans == -1)
        return 1;
    else if (ans == 1)
        return 0;

    for (int i = 2; i < N; i++)
    {
        place(0,-1);
        place(i,1);
        ans = weigh();
        if (ans == -1)
            return i;
    }
    return 0;
}


