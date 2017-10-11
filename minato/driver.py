import sys

from interfaces.minato import minato

from turingarena.runtime.sandbox import sandbox
from turingarena.runtime.data import rebased

class minato_utils:

    def __init__(self, N, M, mine_map):
        self.N = N
        self.M = M
        self.mine_map = mine_map

    def is_safe(self, row, column):
        if column < 1 or column > self.M:
            raise ValueError("column out of bound")
        if row < 1 or row > self.N:
            raise ValueError("row out of bound")

        return self.mine_map[row-1][column-1]


def evaluate_solution(input_file):
    with sandbox.create_process("solution") as s, minato(s) as driver, open(input_file,"r") as f:

        (N,M) = [int(x) for x in next(f).split()]
        mine_map = []
        for line in f:
            mine_line = []
            for c in line:
                if c is '*': mine_line.append(1) 
                if c is '+': mine_line.append(0) 
            mine_map.append(mine_line)

        driver.N = N
        driver.M = M

        mu = minato_utils(N,M,mine_map)
        S = driver.find_number_of_paths(callback_is_safe=mu.is_safe)

        return S

for i in range(0,20):
    with open("output/output{number}.txt".format(number=i),"r") as solution_file:
        ans = evaluate_solution("input/input{number}.txt".format(number=i))
        sol = int(solution_file.read())
        print(i, ans == sol )

