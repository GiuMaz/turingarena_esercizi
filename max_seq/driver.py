import sys

from interfaces.max_seq import max_seq

from turingarena.runtime.sandbox import sandbox


with sandbox.create_process("solution") as s, max_seq(s) as driver:

    N = 10
    A = [i*i for i in range(N)]


    S = driver.solve(A, N)

print("Answer:", S, file=sys.stderr)
