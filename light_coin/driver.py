import sys

from interfaces.light_coin import light_coin

from turingarena.runtime.sandbox import sandbox
from turingarena.runtime.data import rebased

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
        if coin < 0 or coin >= driver.N:
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

        self.coins_position[:] = [0] * driver.N
        return return_value

with sandbox.create_process("solution") as s, light_coin(s) as driver:

    driver.N = 2**5

    # moneta in posizione fissa
    lc = light_coin_utils(driver,light_coin_position=3)

    S = driver.find_light_coin(callback_place=lc.place, callback_weigh=lc.weigh)

    if S == lc.light_coin_position:
        print ("1: right coin")
    else:
        print ("1: wrong coin")

    print("Answer:", S, "number of weights:",lc.number_of_weights, file=sys.stderr)

with sandbox.create_process("solution") as s, light_coin(s) as driver:

    driver.N = 2**4

    # moneta in posizione variabile
    lc = light_coin_utils(driver)

    S = driver.find_light_coin(callback_place=lc.place, callback_weigh=lc.weigh)

    if S == lc.light_coin_position:
        print ("2: right coin")
    else:
        print ("2: wrong coin")

    print("Answer:", S, "number of weights:",lc.number_of_weights, file=sys.stderr)

