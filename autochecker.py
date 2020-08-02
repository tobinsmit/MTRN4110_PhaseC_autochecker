import os, platform, shutil
import numpy as np

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

test_count = 25

def checkMapFilesAreSame(path1, path2):
    f1 = open(path1, 'r')
    f2 = open(path2, 'r')
    contents1 = f1.read()
    contents2 = f2.read()
    f1.close()
    f2.close()
    return contents1 == contents2

if __name__ == "__main__":
    results = np.zeros((test_count,1), dtype=bool)
    for test in range(test_count):
        # Set map
        if os.path.isfile("./Maze.png"):
            os.remove("./Maze.png")
        if os.path.isfile("./Robot.png"):
            os.remove("./Robot.png")
        if os.path.isfile("./MapFound.txt"):
            os.remove("./MapFound.txt")
        shutil.copy(f"./tests/Maze_{test}.png", "./Maze.png")
        shutil.copy(f"./tests/Robot_{test}.png", "./Robot.png")

        print('Starting')
        os.system("cd ./programs && ipython3 PhaseC.py")
        print('Done')


        if os.path.isfile("./MapFound.txt"):
            testPassed = checkMapFilesAreSame(f"./tests/MapFound_{test}.txt", "./MapFound.txt")
            color = bcolors.OKGREEN if testPassed else bcolors.FAIL
            print(f'{color}Test {test}: {"PASS" if testPassed else "FAILED"} {bcolors.ENDC}')
            results[test] = testPassed
            shutil.copy("./MapFound.txt", f"./tests/MapFound_{test}.txt")
        else:
            print(f'{bcolors.FAIL}Test {test}: FAILED. No output of PhaseC.py {bcolors.ENDC}')
            results[test] = 0
    
    print('\n\n')
    for test in range(test_count):
        if results[test] == 1:
            print(f'{bcolors.OKGREEN}Test {test}: PASS{bcolors.ENDC}')
        else:
            print(f'{bcolors.FAIL}Test {test}: FAIL{bcolors.ENDC}')