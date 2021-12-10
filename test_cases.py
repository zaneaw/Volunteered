import solution as sol


class Test():
    def __init__(self, start, stop, board_size, answer):
        self.start = start
        self.stop = stop
        self.board_size = board_size
        print(sol.solution(self.start, self.stop, self.board_size))



if __name__ == '__main__':
    test1 = Test(19, 36, 8, 1)
    test2 = Test(0, 1, 8, 3)

    
    # test_1 = sol.solution(19, 36, 8)
    # answer_1 = 1
    # test_2 = sol.solution(0, 1, 8)
    # answer_2 = 3
    # if test_1 == answer_1 and test_2 == answer_2:
    #     print("All good in the 'hood.")
    # elif test_1 != answer_1 and test_2 == answer_2:
    #     print("Test 1 failed, Test 2 passed.")
    # elif test_1 == answer_1 and test_2 != answer_2:
    #     print("Test 1 passed, Test 2 failed.")
    # else:
    #     print("It all failed. RIP.")
