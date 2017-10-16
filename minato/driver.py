import sys

from interfaces.minato import minato

from turingarena.runtime.sandbox import sandbox

from random import seed, randint

seed(123321)

def generate_mine_field(N,M):
    mine_field = [[int(randint(0,99) > 85) for __ in range(M)] for __ in range(N)]

    n,m = 0,0
    while n < N and m < M:
        mine_field[n][m] = 0
        if randint(0,1): n+=1
        else: m+=1

    for i in range(n,N): mine_field[i][M-1] = 0
    for j in range(m,M): mine_field[N-1][j] = 0

    return mine_field

def evaluate_solution(algoritm_name, N, M, mine_field):
    with sandbox.create_process(algoritm_name) as s, minato(s) as driver:

        driver.N = N
        driver.M = M
        driver.mine_field = mine_field

        return driver.find_number_of_paths()

def mine_field_from_file(file_name):
    with open(file_name,"r") as f:
        N,M = [int(x) for x in next(f).split()]
        mine_field = [[ {'*':1,'+':0}[c] for c in line.strip('\n')] for line in f]
    return N, M, mine_field

def is_solution_correct(N,M,mine_field=None):

    if mine_field is None:
        mine_field = generate_mine_field(N,M)

    return evaluate_solution("solution",N,M,mine_field) == evaluate_solution("reference",N,M,mine_field)

# solve the example case
def task1():
    N,M,mine_field = mine_field_from_file("input/example.txt")
    return is_solution_correct(N,M,mine_field)

# N <= 20
def task2():
    task_result = True
    task_result &= is_solution_correct(5,5)
    task_result &= is_solution_correct(10,5)
    task_result &= is_solution_correct(10,10)
    task_result &= is_solution_correct(15,15)
    task_result &= is_solution_correct(20,20)

    return task_result

# N <= 50
def task3():
    task_result = True
    task_result &= is_solution_correct(20,30)
    task_result &= is_solution_correct(30,30)
    task_result &= is_solution_correct(40,30)
    task_result &= is_solution_correct(40,40)
    task_result &= is_solution_correct(50,40)
    task_result &= is_solution_correct(50,50)

    return task_result

# N <= 100
def task4():
    task_result = True
    task_result &= is_solution_correct(60,60)
    task_result &= is_solution_correct(70,70)
    task_result &= is_solution_correct(75,75)
    task_result &= is_solution_correct(80,50)
    task_result &= is_solution_correct(80,80)
    task_result &= is_solution_correct(90,90)
    task_result &= is_solution_correct(100,100)
    task_result &= is_solution_correct(100,1)

    return task_result

print(task1())
print(task2())
print(task3())
print(task4())

