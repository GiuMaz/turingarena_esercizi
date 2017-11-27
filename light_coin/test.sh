#!/usr/bin/env bash

python setup.py develop

turingarena protocol --name light_coin install
turingarena protocol --name light_coin proxy
turingarena protocol --name light_coin skeleton

turingarena make --module light_coin --name problem run --phase compile_log3_solution && cat ./algorithms/log3_solution/compilation_output.txt
turingarena make --module light_coin --name problem run --phase goal_task0
