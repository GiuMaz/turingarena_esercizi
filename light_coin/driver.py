import sys

from interfaces.light_coin import light_coin

from turingarena.runtime.sandbox import sandbox
from turingarena.runtime.data import rebased


with sandbox.create_process("solution") as s, light_coin(s) as driver:
    
    totale_monete = 10
    driver. posizione_moneta_leggera = 3;

    driver.individua(totale_monete)

    S=0
    if S == -1:
        print ("moneta sbagliata")
    else:
        print ("moneta corretta: ",S)



print("Answer:", S, file=sys.stderr)
