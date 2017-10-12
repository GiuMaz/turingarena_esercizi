import sys

from interfaces.minato import minato

from turingarena.runtime.sandbox import sandbox
from turingarena.runtime.data import rebased
from random import seed, randint

seed(1001001)

class minato_utils:

    def __init__(self, N, M, mine_field=None):
        self.N = N
        self.M = M
        if mine_field is None:
            self._generate_mine_field()
        else:
            self.mine_field = mine_field

    def _generate_mine_field(self):
        self.mine_field = []

        for i in range(0,self.N): self.mine_field.append([1] * self.M)
        n,m = 0,0

        print(self.N,self.M)
        while n < self.N and m < self.M:
            self.mine_field[n][m] = 0
            if randint(0,1) == 0: n+=1
            else: m+=1
            print(*self.mine_field,n,m,'\n',sep='\n')

        for i in range(n,self.N): self.mine_field[i][self.M-1] = 0
        for j in range(m,self.M): self.mine_field[self.N-1][j] = 0

    def is_safe(self, row, column):
        if column < 1 or column > self.M:
            raise ValueError("column out of bound")
        if row < 1 or row > self.N:
            raise ValueError("row out of bound")

        return self.mine_field[row-1][column-1]


def evaluate_solution(N,M):
    with sandbox.create_process("solution") as s, minato(s) as driver:

        driver.N = N
        driver.M = M

        mu = minato_utils(N,M)
        driver.mine_field = mu.mine_field
        S = driver.find_number_of_paths()

        return S

evaluate_solution(5,5)

#for i in range(0,20):
#    with open("output/output{number}.txt".format(number=i),"r") as solution_file:
#        ans = evaluate_solution("input/input{number}.txt".format(number=i))
#        sol = int(solution_file.read())
#        print(i, ans == sol )
