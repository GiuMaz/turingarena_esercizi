int find_light_coin()
{
    int ans;
    place(0,-1);
    place(1,1);

    ans = weigh();

    if ( ans == -1)
        return 1;
    else
        return 0;
}
