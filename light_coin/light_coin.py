from turingarena.problem import Problem
from math import log, ceil, floor

problem = Problem()

problem.implementation_entry(
    "entry",
    protocol_name="light_coin",
    interface_name="light_coin_interface",
)

def weigh():
    return 0

def place(c,p):
    return

class light_coin_utils:

    def __init__(self, N, light_coin_position=None):
        self.number_of_weights = 0
        self.N = N
        self.coins_position = [0] * N
        self.valid_coins = list(range(0,N))
        self.light_coin_position = light_coin_position

    def place(self, coin, position):
        if self.coins_position[coin] != 0:
            raise ValueError("already placed")
        if coin < 0 or coin >= self.N:
            raise ValueError("coin out of range")
        if position not in(-1,+1):
            raise ValueError("invalid position")
        self.coins_position[coin] = position

    def _move_coin(self):

        # find the largest set of valid position
        total_left  = 0
        total_right = 0
        total_none  = 0

        for i in self.valid_coins:
            if self.coins_position[i] == 1:
                total_right+=1
            elif self.coins_position[i] == 0:
                total_none+=1
            elif self.coins_position[i] == -1:
                total_left+=1

        # move the coin in the largest set
        return_value = 0
        if total_left >= total_right:
            if total_left > total_none:
                return_value = 1
            else:
                return_value = 0
        else:
            if total_right > total_none:
                return_value = -1
            else:
                return_value = 0

        # update the valid position to be consistent with the new weigh
        new_valid_coin = []
        for i in self.valid_coins:
            if self.coins_position[i] == -return_value:
                new_valid_coin.append(i)
        self.valid_coins[:] = new_valid_coin

        # if only a single valid position remain it must be the right position
        if len(self.valid_coins) == 1:
            self.light_coin_position = self.valid_coins[0]

        return return_value

    def weigh(self):
        return_value = 0
        self.number_of_weights+=1

        total = sum(self.coins_position)

        if total > 0:
            return_value = 1
        elif total < 0:
            return_value = -1
        else:
            if self.light_coin_position is not None:
                return_value = - self.coins_position[self.light_coin_position]
            else:
                return_value = self._move_coin()

        self.coins_position[:] = [0] * self.N
        return return_value


def evaluate_solution(entry, N, light_coin_position=None):
    with entry.run(N=N) as p:
        lc = light_coin_utils(N,light_coin_position=light_coin_position)
        S = p.find_light_coin(weigh=lc.weigh,place=lc.place)
        return (S == lc.light_coin_position, lc.number_of_weights)

@problem.goal
def task0(entry): # the false coin is in position 2
    result = True
    for N in [3,10,100]:
        (answer_is_correct,number_of_weights) = evaluate_solution(entry,N,light_coin_position=2)
        result = result and answer_is_correct
    return result

@problem.goal
def task1(entry): # the false coin is either 0 or 1
    result = True
    for N in [3,10,100]:
        (answer_is_correct,number_of_weights) = evaluate_solution(entry,N,light_coin_position=0)
        result = result and answer_is_correct
        (answer_is_correct,number_of_weights) = evaluate_solution(entry,N,light_coin_position=1)
        result = result and answer_is_correct
    return result

@problem.goal
def task2(entry): # N = 7, max wigh = 6
    (answer_is_correct,number_of_weights) = evaluate_solution(entry,7)
    return  answer_is_correct and (number_of_weights <=6)

@problem.goal
def task3(entry): # N = 7, max weigh = 4
    (answer_is_correct,number_of_weights) = evaluate_solution(entry,7)
    return answer_is_correct and (number_of_weights <=4)

@problem.goal
def task4(entry): # N = 7, max weigh = 3
    (answer_is_correct,number_of_weights) = evaluate_solution(entry,7)
    return answer_is_correct and (number_of_weights <=3)

@problem.goal
def task5(entry): # N = 8, max weigh = 3
    (answer_is_correct,number_of_weights) = evaluate_solution(entry,8)
    return answer_is_correct and (number_of_weights <=3)

@problem.goal
def task6(entry): # max weigh = N - 1
    result = True
    for N in [10,100,1000]:
        (answer_is_correct,number_of_weights) = evaluate_solution(entry,N)
        result = result and answer_is_correct and (number_of_weights <= N-1 )
    return result

@problem.goal
def task7(entry): # max weigh = N / 2
    result = True
    for N in [10,100,1000]:
        (answer_is_correct,number_of_weights) = evaluate_solution(entry,N)
        result = result and answer_is_correct and (number_of_weights <= floor(N/2) )
    return result

@problem.goal
def task8(entry): # max weigh = log2 N
    result = True
    for N in [10,100,1000]:
        (answer_is_correct,number_of_weights) = evaluate_solution(entry,N)
        result = result and answer_is_correct and (number_of_weights <= ceil(log(N,2)) )
    return result

@problem.goal
def task9(entry): # max weigh = log3 N
    result = True
    for N in [10,100,1000]:
        (answer_is_correct,number_of_weights) = evaluate_solution(entry,N)
        result = result and answer_is_correct and (number_of_weights <= ceil(log(N,3)) )
    return result

