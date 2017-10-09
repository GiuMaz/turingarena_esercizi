import sys

from interfaces.light_coin import light_coin

from turingarena.runtime.sandbox import sandbox
from turingarena.runtime.data import rebased


with sandbox.create_process("solution") as s, light_coin(s) as driver:

    class light_coin_utils:

        number_of_weights = 0

        def place(self, coin, position):
            if monete[coin] != 0:
                raise ValueError("already placed")
            if coin < 0 or coin >= driver.N:
                raise ValueError("coin out of range")
            if position not in(-1,+1):
                raise ValueError("invalid position")
            monete[coin] = position

        def weigh(self):
            return_value = 0
            self.number_of_weights+=1

            total = sum(monete)

            if total > 0:
                return_value = 1
            elif total < 0:
                return_value = -1
            else:
                return_value = - monete[posizione_moneta_leggera]

            monete[:] = [0] * driver.N
            return return_value

    lc = light_coin_utils()
    driver.N =27
    monete = [0] * driver.N
    posizione_moneta_leggera = 6;

    S = driver.find_light_coin(callback_place=lc.place, callback_weigh=lc.weigh)

    if S == posizione_moneta_leggera:
        print ("right coin")
    else:
        print ("wrong coin")

    print("Answer:", S, "number of weights:",lc.number_of_weights, file=sys.stderr)

