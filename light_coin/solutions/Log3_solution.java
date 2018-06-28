class Solution extends Skeleton {

    // interface find_light_coin_callbacks {
    //     int weigh();
    //     void place(int coin, int position);
    // }

    int find_light_coin(int N, find_light_coin_callbacks callbacks) {
        int start, middle, end, leftover;

        leftover = N % 3;

        start = 0;
        middle = (N-leftover)/3;
        end = middle * 2;

        while (true)
        {
            if (N == 1) return start;

            if (N == 2)
            {
                callbacks.place(start, -1);
                callbacks.place(start+1, 1);

                int ans =  callbacks.weigh();

                if (ans == -1) return start+1;
                else return start;
            }

            for (int i = start; i < middle; ++i) callbacks.place(i, -1);

            for (int i = middle; i < end; ++i) callbacks.place(i, 1);

            int ans =  callbacks.weigh();

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
}
