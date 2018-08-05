import os

os.system("c++ -O3 -Wall -shared -std=c++11 -fPIC `python3 -m pybind11 --includes` TicTacToe.cpp -o example`python3-config --extension-suffix`")