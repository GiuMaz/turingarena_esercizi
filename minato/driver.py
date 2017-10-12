import sys

from interfaces.minato import minato

from turingarena.runtime.sandbox import sandbox

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

        for i in range(0,self.N):
            for j in range(0, self.M):
                if randint(0,99) > 85: self.mine_field[i][j] = 0

        n,m = 0,0

        while n < self.N and m < self.M:
            self.mine_field[n][m] = 0
            if randint(0,1) == 0: n+=1
            else: m+=1

        for i in range(n,self.N): self.mine_field[i][self.M-1] = 0
        for j in range(m,self.M): self.mine_field[self.N-1][j] = 0


def evaluate_solution(N,M):
    with sandbox.create_process("solution") as s, minato(s) as driver_solution,\
            sandbox.create_process("reference") as r, minato(r) as driver_reference:

        mu = minato_utils(N,M)

        driver_solution.N = N
        driver_solution.M = M
        driver_solution.mine_field = mu.mine_field
        user_ans = driver_solution.find_number_of_paths()

        driver_reference.N = N
        driver_reference.M = M
        driver_reference.mine_field = mu.mine_field
        reference_ans = driver_reference.find_number_of_paths()

        return user_ans == reference_ans

def evaluate_input_solution(input_file):
    with sandbox.create_process("solution") as s, minato(s) as driver_solution,\
            sandbox.create_process("reference") as r, minato(r) as driver_reference, \
            open(input_file,"r") as f:

        (N,M) = [int(x) for x in next(f).split()]
        mine_map = []
        for line in f:
            mine_line = []
            for c in line:
                if c is '*': mine_line.append(0) 
                if c is '+': mine_line.append(1) 
            mine_map.append(mine_line)

        mu = minato_utils(N,M,mine_map)

        driver_solution.N = N
        driver_solution.M = M
        driver_solution.mine_field = mu.mine_field
        user_ans = driver_solution.find_number_of_paths()

        driver_reference.N = N
        driver_reference.M = M
        driver_reference.mine_field = mu.mine_field
        reference_ans = driver_reference.find_number_of_paths()

        return user_ans == reference_ans

# solve the example case
def task1():
    return evaluate_input_solution("input/input0.txt")

# N <= 20
def task2():
    task_result = True
    task_result &= evaluate_solution(5,5)
    task_result &= evaluate_solution(10,5)
    task_result &= evaluate_solution(10,10)
    task_result &= evaluate_solution(15,15)
    task_result &= evaluate_solution(20,20)

    return task_result

# N <= 50
def task3():
    task_result = True
    task_result &= evaluate_solution(20,30)
    task_result &= evaluate_solution(30,30)
    task_result &= evaluate_solution(40,30)
    task_result &= evaluate_solution(40,40)
    task_result &= evaluate_solution(50,40)
    task_result &= evaluate_solution(50,50)

    return task_result

# N <= 100
def task4():
    task_result = True
    task_result &= evaluate_solution(60,60)
    task_result &= evaluate_solution(70,70)
    task_result &= evaluate_solution(75,75)
    task_result &= evaluate_solution(80,50)
    task_result &= evaluate_solution(80,80)
    task_result &= evaluate_solution(90,90)
    task_result &= evaluate_solution(100,100)
    task_result &= evaluate_solution(100,1)

    return task_result

print(task1())
print(task2())
print(task3())
print(task4())

