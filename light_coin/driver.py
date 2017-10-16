import sys

from interfaces.light_coin import light_coin

from turingarena.runtime.sandbox import sandbox

from math import log, ceil, floor

class light_coin_utils:

    def __init__(self, driver, light_coin_position=None):
        self.number_of_weights = 0
        self.driver = driver
        self.coins_position = [0] * driver.N
        self.valid_coins = list(range(0,driver.N))
        self.light_coin_position = light_coin_position

    def place(self, coin, position):
        if self.coins_position[coin] != 0:
            raise ValueError("already placed")
        if coin < 0 or coin >= self.driver.N:
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

        self.coins_position[:] = [0] * self.driver.N
        return return_value

def evaluate_solution(N, light_coin_position=None):
    with sandbox.create_process("solution") as s, light_coin(s) as driver:

        driver.N = N
        lc = light_coin_utils(driver,light_coin_position=light_coin_position)

        S = driver.find_light_coin(callback_place=lc.place, callback_weigh=lc.weigh)

        return (S == lc.light_coin_position, lc.number_of_weights)

task0 = True # the false coin is in position 2
task1 = True # the false coin is either 0 or 1
task2 = True # N = 7, max weigh = 6
task3 = True # N = 7, max weigh = 4
task4 = True # N = 7, max weigh = 3
task5 = True # N = 8, max weigh = 3
task6 = True # max weigh = N - 1
task7 = True # max weigh = N / 2
task8 = True # max weigh = log2 N
task9 = True # max weigh = log3 N

for N in [3,10,100]:
    (answer_is_correct,number_of_weights) = evaluate_solution(N,light_coin_position=2)
    task0 = task0 & answer_is_correct

for N in [3,10,100]:
    (answer_is_correct,number_of_weights) = evaluate_solution(N,light_coin_position=0)
    task1 = task1 & answer_is_correct
    (answer_is_correct,number_of_weights) = evaluate_solution(N,light_coin_position=1)
    task1 = task1 & answer_is_correct

(answer_is_correct,number_of_weights) = evaluate_solution(7)
task2 = answer_is_correct & (number_of_weights <=6)

(answer_is_correct,number_of_weights) = evaluate_solution(7)
task3 = answer_is_correct & (number_of_weights <=4)

(answer_is_correct,number_of_weights) = evaluate_solution(7)
task4 = answer_is_correct & (number_of_weights <=3)

(answer_is_correct,number_of_weights) = evaluate_solution(8)
task5 = answer_is_correct & (number_of_weights <=3)

for N in [10,100,1000]:
    (answer_is_correct,number_of_weights) = evaluate_solution(N)
    task6 = task6 & answer_is_correct & (number_of_weights <= N-1 )

for N in [10,100,1000]:
    (answer_is_correct,number_of_weights) = evaluate_solution(N)
    task7 = task7 & answer_is_correct & (number_of_weights <= floor(N/2) )

for N in [10,100,1000]:
    (answer_is_correct,number_of_weights) = evaluate_solution(N)
    task8 = task8 & answer_is_correct & (number_of_weights <= ceil(log(N,2)) )

for N in [10,100,1000]:
    (answer_is_correct,number_of_weights) = evaluate_solution(N)
    task9 = task9 & answer_is_correct & (number_of_weights <= ceil(log(N,3)) )

print("Task0:", task0, file=sys.stderr)
print("Task1:", task1, file=sys.stderr)
print("Task2:", task2, file=sys.stderr)
print("Task3:", task3, file=sys.stderr)
print("Task4:", task4, file=sys.stderr)
print("Task5:", task5, file=sys.stderr)
print("Task6:", task6, file=sys.stderr)
print("Task7:", task7, file=sys.stderr)
print("Task8:", task8, file=sys.stderr)
print("Task9:", task9, file=sys.stderr)

