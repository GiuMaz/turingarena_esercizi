int solve(int *v, int n) {
    int max = v[0];
    for ( int i = 1; i < n; ++i)
        if (max < v[i])
            max = v[i];

    return max;
}
