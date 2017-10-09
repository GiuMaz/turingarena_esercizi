import sys

from interfaces.light_coin import light_coin

from turingarena.runtime.sandbox import sandbox
from turingarena.runtime.data import rebased



with sandbox.create_process("solution") as s, light_coin(s) as driver:

    driver.N = 10
    monete = [0] * driver.N
    posizione_moneta_leggera = 3;

    def place(coin, position):
        if monete[coin] != 0:
            raise ValueError("already placed")
        if coin < 0 or coin >= driver.N:
            raise ValueError("coin out of range")
        if position not in(-1,+1):
            raise ValueError("invalid position")
        monete[coin] = position

    def weigh():
        return_value = 0

        total = sum(monete)
        if total > 0:
            return_value = 1
        elif total < 0:
            return_value = -1
        else:
            return_value = - monete[posizione_moneta_leggera]

        monete[:] = [0] * driver.N
        return return_value

    S = driver.find_light_coin(callback_place=place, callback_weigh=weigh)

    if S == posizione_moneta_leggera:
        print ("right coin")
    else:
        print ("wrong coin")
    print("Answer:", S, file=sys.stderr)
