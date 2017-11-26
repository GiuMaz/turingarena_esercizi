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

void map_IS_into_Clique(int nH, int** AdjH, int h, int nG, int** AdjG, int k, int* S, bool* C)
{

    nG = nH;

    for (int i = 0; i < nH; ++i)
        for (int j = 0; j < nH; ++j)
            AdjG[i][j] = AdjH[i][j];

    k = h;

    for (int i = 0; i < nH; ++i)
        S[i] = C[i];
}

void get_IS_cert_from_Clique_cert(int nH, int** AdjH, int h, bool S[MAX_N], const bool C[MAX_N])
{
    int nG; bool AdjG[MAX_N][MAX_N]; int k;
    map_IS_into_Clique(nH, AdjH, h, nG, AdjG, k);
    assert( isClique(nG, C, AdjG, k) );
    // <-- ottieni un independent set S di H con |S|=h dalla clique C di G con |C|=k -->
    // <-- in altre parole: fornire dimostrazione costruttiva del lemma difficile -->
    map_IS_into_Clique(nH, AdjH, h, nG, AdjG, k, S, C);
    assert( isIndependentSet(nH, S, AdjH, h) );
}

