import random
from turingarena import *

N = 100

def main():
    for _ in range(10):
        # place in a random fixed position
        correct = random.randint(0, N-1)
        is_correct_answer, number_of_weigh = compute_fixed(correct)
        if is_correct_answer:
            print('correct, number_of_weigh', number_of_weigh)
        else:
            print('WRONG!')

    for _ in range(10):
        # move around the coin in the most difficult position
        is_correct_answer, number_of_weigh = compute_moving()
        if is_correct_answer:
            print('correct, number_of_weigh', number_of_weigh)
        else:
            print('WRONG!')

def compute_fixed(correct):
    with run_algorithm(submission.source) as process:

        number_of_weigh = 0
        coins_position = [0] * N

        def weigh():
            nonlocal number_of_weigh, coins_position, correct

            number_of_weigh+=1

            total = sum(coins_position)
            light_coin_pos = coins_position[correct]

            coins_position[:] = [0] * N

            if total > 0:
                return 1
            elif total < 0:
                return -1
            else:
                return -light_coin_pos

        def place(coin, position):
            nonlocal coins_position
            coins_position[coin] = position

        player_answer = process.functions.find_light_coin(N,
                callbacks=[weigh,place])

        return player_answer == correct, number_of_weigh

def compute_moving():
    with run_algorithm(submission.source) as process:

        number_of_weigh = 0
        coins_position = [0] * N

        valid_coins = list(range(0,N))

        light_coin_position = None

        def move_coin():

            nonlocal valid_coins, coins_position, light_coin_position

            # find the largest set of valid position
            total_left  = 0
            total_right = 0
            total_none  = 0

            for i in valid_coins:
                if coins_position[i] == 1:
                    total_right+=1
                elif coins_position[i] == 0:
                    total_none+=1
                elif coins_position[i] == -1:
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
            for i in valid_coins:
                if coins_position[i] == -return_value:
                    new_valid_coin.append(i)
            valid_coins[:] = new_valid_coin

            # if only a single valid position remain it must be the right position
            if len(valid_coins) == 1:
                light_coin_position = valid_coins[0]

            return return_value

        def weigh():
            nonlocal number_of_weigh, coins_position

            number_of_weigh+=1

            total = sum(coins_position)

            if total > 0:
                return 1
            elif total < 0:
                return -1

            return_val =  move_coin()
            coins_position[:] = [0] * N

            return return_val

        def place(coin, position):
            nonlocal coins_position
            coins_position[coin] = position

        player_answer = process.functions.find_light_coin(N,
                callbacks=[weigh,place])

        return player_answer == light_coin_position, number_of_weigh

main()
