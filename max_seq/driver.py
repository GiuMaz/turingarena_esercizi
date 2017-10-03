import sys

from interfaces.max_seq import max_seq

from turingarena.runtime.sandbox import sandbox
from turingarena.runtime.data import rebased


with sandbox.create_process("solution") as s, max_seq(s) as driver:

    N = 10
    A = rebased(1, [i*i for i in range(1,1+N)])

    S = driver.solve(A, N)

print("Answer:", S, file=sys.stderr)
