#!/bin/bash

echo 'Running Coin Determiner benchmark...'

echo '\nTest 1: n = 250'
echo '-------------------------------\n'
/usr/bin/time -v python solver.py --q --n 250

echo '\nTest 2: file = input_test.txt'
echo '-------------------------------\n'
/usr/bin/time -v python solver.py --q --i input_test.txt