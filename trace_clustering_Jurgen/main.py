# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from classes.fsp import Fsp


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fsp1 = Fsp('SPAM', [['A', 'X', 'B', 'C', 'E', 'D', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']], [0.8,2,2])
    print(fsp1.getResult())
    fsp2 = Fsp('CloFast', [['A', 'X', 'B', 'C', 'E', 'D', 'F'], ['A', 'E', 'C', 'Y', 'D', 'F'], ['A', 'Z', 'C', 'D', 'B', 'E', 'F']], [0.8])
    print(fsp2.getResult())
    print(fsp2.getAmount())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
