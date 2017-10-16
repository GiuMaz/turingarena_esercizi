
int isClique(int n, int* C, int** AdjG, int k)
{
    int clique_size = 0;

    for (int i = 0; i < n; ++i)
    {
        if (!C[i]) continue;

        clique_size++;

        for (int j = i+1; j < n; ++j)
            if (C[i] && ( !AdjG[i][j] || !AdjG[j][i] )) return 0;
    }

    return clique_size == k ? 1 : 0;
}

int isIndependentSet(int n, int* S, int** AdjH, int h)
{
    int is_size = 0;

    for (int i = 0; i < n; ++i)
    {
        if (!C[i]) continue;

        is_size++;

        for (int j = i+1; j < n; ++j)
            if (C[i] && ( AdjG[i][j] || AdjG[j][i] )) return 0;
    }

    return is_size == h ? 1 : 0;
}

void map_IS_into_Clique(int nH, const bool AdjH[MAX_N][MAX_N], int h,
    int &nG, bool AdjG[MAX_N][MAX_N], int &k,
const bool S[MAX_N] = 0, bool C[MAX_N] = 0)
{

}
