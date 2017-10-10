int find_light_coin()
{
    place(0,-1);
    place(1,1);

    int ans = weigh();

    if ( weigh == -1)
        return 1;
    else
        return 0;
}
