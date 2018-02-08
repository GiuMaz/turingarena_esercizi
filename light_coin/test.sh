#!/usr/bin/env bash

python setup.py install --force
python turingarena_setup.py

REPO_PATH=$HOME/.turingarena/db.git
mkdir -p $REPO_PATH

git init --bare $REPO_PATH

ENTRY=$(turingarena entry --repo-path=$REPO_PATH --file=entry.cpp:entry.cpp)

turingarena make make --plan=light_coin:problem --repo-path=$REPO_PATH --entry=entry_entry:$ENTRY evaluate_task0
turingarena make make --plan=light_coin:problem --repo-path=$REPO_PATH --entry=entry_entry:$ENTRY evaluate_task1
turingarena make make --plan=light_coin:problem --repo-path=$REPO_PATH --entry=entry_entry:$ENTRY evaluate_task2
turingarena make make --plan=light_coin:problem --repo-path=$REPO_PATH --entry=entry_entry:$ENTRY evaluate_task3
turingarena make make --plan=light_coin:problem --repo-path=$REPO_PATH --entry=entry_entry:$ENTRY evaluate_task4
turingarena make make --plan=light_coin:problem --repo-path=$REPO_PATH --entry=entry_entry:$ENTRY evaluate_task5
turingarena make make --plan=light_coin:problem --repo-path=$REPO_PATH --entry=entry_entry:$ENTRY evaluate_task6
turingarena make make --plan=light_coin:problem --repo-path=$REPO_PATH --entry=entry_entry:$ENTRY evaluate_task7
turingarena make make --plan=light_coin:problem --repo-path=$REPO_PATH --entry=entry_entry:$ENTRY evaluate_task8
turingarena make make --plan=light_coin:problem --repo-path=$REPO_PATH --entry=entry_entry:$ENTRY evaluate_task9

