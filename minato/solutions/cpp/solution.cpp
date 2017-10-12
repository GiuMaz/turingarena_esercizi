#define MAX_NUM 101

int percorsi[MAX_NUM+1][MAX_NUM+1];

int possible_paths(int row, int column)
{
    if (percorsi[row][column] != -1) return percorsi[row][column];

    if (row == N && column == M) return 1;

    int tot = 0;

    if ( row < N && mine_field[row +1][column] )
        tot += possible_paths(row +1, column);

    if ( column < M && mine_field[row][column+1] )
        tot += possible_paths(row, column +1);

    percorsi[row][column] = tot;
    return percorsi[row][column];
}

int find_number_of_paths()
{
    for (int i = 0; i <= N; ++i)
        for (int j = 0; j <= M; ++j)
            percorsi[i][j] = -1;

    return possible_paths(1,1);
}

