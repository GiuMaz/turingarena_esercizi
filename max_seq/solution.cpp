int solve(int *v, int n) {
    int max = v[1];
    for ( int i = 2; i <= n; ++i)
        if (max < v[i])
            max = v[i];

    return max;
}
