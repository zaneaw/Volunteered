import solution as sol

if __name__ == '__main__':
    test_1 = sol.solution(19, 36)
    answer_1 = 1
    test_2 = sol.solution(0, 1)
    answer_2 = 3
    if test_1 == answer_1 and test_2 == answer_2:
        print("All good in the 'hood.")
    elif test_1 != answer_1 and test_2 == answer_2:
        print("Test 1 failed, Test 2 passed.")
    elif test_1 == answer_1 and test_2 != answer_2:
        print("Test 1 passed, Test 2 failed.")
