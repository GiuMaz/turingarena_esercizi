#!/usr/bin/env bash

python setup.py develop

turingarena protocol --name light_coin install
turingarena protocol --name light_coin proxy
turingarena protocol --name light_coin skeleton

turingarena make --module light_coin --name problem run --phase compile_entry
turingarena make --module light_coin --name problem run --phase goal_task0
