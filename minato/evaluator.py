from random import seed, randint
import sys
from turingarena import *

seed(123321)

def generate_mine_field(N,M):
    mine_field = [[int(randint(0,99) > 15) for __ in range(M)] for __ in range(N)]

    n,m = 0,0
    while n < N and m < M:
        mine_field[n][m] = 0
        if randint(0,1): n+=1
        else: m+=1

    for i in range(n,N): mine_field[i][M-1] = 0
    for j in range(m,M): mine_field[N-1][j] = 0

    return mine_field

def mine_field_from_file(file_name):
    with open(file_name,"r") as f:
        N,M = [int(x) for x in next(f).split()]
        mine_field = [[ {'*':0,'+':1}[c] for c in line.strip('\n')] for line in f]
    return N, M, mine_field

def correct_solution(N,M, mine_field):
    paths = [[-1 for i in range(M)] for j in range(N)]

    def possible_paths( row, column):
        nonlocal paths, N, M, mine_field

        if paths[row][column] != -1:
            return paths[row][column]

        if row == (N-1) and column == (M-1):
            return 1

        tot = 0;

        if (row+1) < N and mine_field[row+1][column] == 0:
            tot += possible_paths(row +1, column);

        if (column+1) < M and mine_field[row][column+1] == 0:
            tot += possible_paths(row, column +1);

        paths[row][column] = tot;
        return paths[row][column];

    result = possible_paths(0, 0)
    return result


def evaluate_problem(N,M,mine_field=None):

    if mine_field is None:
        mine_field = generate_mine_field(N,M)

    with run_algorithm(submission.source) as process:
        user    =  process.functions.find_number_of_paths(N,M,mine_field)
        correct = correct_solution(N,M,mine_field)

        if user == correct:
            print('CORRECT:',user,'paths')
        else:
            print('WRONG:',user,'user,',correct,'correct')

# solve the example case
def task1():
    N,M,mine_field = mine_field_from_file("input/example.txt")
    evaluate_problem(N,M,mine_field)

# N <= 20
def task2():
    evaluate_problem(5,5)
    evaluate_problem(10,5)
    evaluate_problem(10,10)
    evaluate_problem(15,15)
    evaluate_problem(20,20)


# N <= 50
def task3():
    evaluate_problem(20,30)
    evaluate_problem(30,30)
    evaluate_problem(40,30)
    evaluate_problem(40,40)
    evaluate_problem(50,40)
    evaluate_problem(50,50)

# N <= 100
def task4():
    evaluate_problem(60,60)
    evaluate_problem(70,70)
    evaluate_problem(75,75)
    evaluate_problem(80,50)
    evaluate_problem(80,80)
    evaluate_problem(90,90)
    evaluate_problem(100,100)
    evaluate_problem(100,1)

task1()
task2()
task3()
task4()

