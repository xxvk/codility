# English ver.
'''
A frog wants to cross the road. The frog starts at position  X  and needs to reach or exceed position  Y . 
The frog always jumps a fixed distance,  D .

Your task is to calculate the minimum number of jumps the frog needs to reach or go beyond its target.

Write a function:
def solution(X, Y, D):
This function takes three integers  X ,  Y , and  D , 
and returns the minimum number of jumps required 
to get from position  X  to a position greater than or equal to  Y .

Example:
Given:
 X = 10 
 Y = 85 
 D = 30 

The function should return  3 , because:
	•	After the first jump, the frog will be at position  10 + 30 = 40 .
	•	After the second jump, the frog will be at position  10 + 30 + 30 = 70 .
	•	After the third jump, the frog will be at position  10 + 30 + 30 + 30 = 100 , which meets or exceeds  Y = 85 .

Constraints:
	•	 X ,  Y , and  D  are integers within the range [1..1,000,000,000].
	•	 X \leq Y .
'''



# Chinese ver.
'''
一隻青蛙想要穿過馬路。青蛙從位置  X  開始，需要到達或超過位置  Y 。青蛙每次跳躍的距離是固定的，為  D 。

你的任務是計算青蛙到達目標所需的最少跳躍次數。

請撰寫一個函數：
def solution(X, Y, D):
此函數接受三個整數  X ,  Y ,  D ，並返回青蛙從位置  X  跳到達或超過位置  Y  所需的最少跳躍次數。

範例：
給定：
 X = 10 
 Y = 85 
 D = 30 

函數應返回  3 ，因為：
	•	第一次跳躍後，青蛙會到達位置  10 + 30 = 40 。
	•	第二次跳躍後，青蛙會到達位置  10 + 30 + 30 = 70 。
	•	第三次跳躍後，青蛙會到達位置  10 + 30 + 30 + 30 = 100 ，達到或超過  Y = 85 。

限制條件：
	•	 X 、 Y  和  D  是範圍 [1..1,000,000,000] 內的整數。
	•	 X \leq Y 。
'''



# Japnese ver.
'''
カエルが道路を渡ろうとしています。カエルは位置  X  からスタートし、
位置  Y  に到達またはそれを超える必要があります。カエルは毎回一定の距離  D  をジャンプします。

カエルが目的地に到達するために必要な最小ジャンプ回数を計算してください。

次の関数を作成してください：
def solution(X, Y, D):
この関数は、3つの整数  X ,  Y ,  D  を受け取り、位置  X  から位置  Y  以上に到達するために必要な最小ジャンプ回数を返します。

例：
以下が与えられた場合：
 X = 10 
 Y = 85 
 D = 30 

関数は  3  を返すべきです。理由は次の通りです：
	•	最初のジャンプ後、カエルは位置  10 + 30 = 40  に到達します。
	•	2回目のジャンプ後、カエルは位置  10 + 30 + 30 = 70  に到達します。
	•	3回目のジャンプ後、カエルは位置  10 + 30 + 30 + 30 = 100  に到達し、 Y = 85  を超えます。

制約条件：
	•	 X ,  Y ,  D  は範囲 [1..1,000,000,000] 内の整数です。
	•	 X \leq Y 。
'''
def solution(X, Y, D):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    for ainput in [X, Y, D]:
        if ainput < 1 or ainput > 1000000000:
            raise ValueError('input range Error')
        if not ainput:
            raise ValueError('input range Error')
        
    if X > Y:
        raise ValueError('input range Error')
    '''
    checker:    single elements array
    '''
    if X == Y:
        return 0

    '''
    main process
    '''
    delta = Y - X
    raw_count = delta / D
    mod = delta % D
    if mod > 0:
        raw_count += 1
    return int(raw_count)

# Example tests
test_cases = {
    (10, 85, 30): 3,  # example

    # Correctness tests
    (1, 1, 1): 0,                      # extreme_position: no jump needed
    (1, 2, 1): 1,                      # simple1
    (10, 70, 20): 3,                   # simple2
    (5, 1000000000, 1000000000): 1,    # small_extreme_jump: one big jump

    # Performance tests
    (1, 1000000000, 2): 500000000,     # many_jump1
    (1, 1000000000, 99): 10101011,     # many_jump2
    (1, 1000000000, 1283): 779424,     # many_jump3
    (1, 1000000000, 1): 999999999,     # big_extreme_jump: maximal number of jumps
    (1, 1000000, 1): 999999            # small_jumps: many small jumps
}

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for (X, Y, D), expected_output in test_cases.items():
        try:
            result = solution(X, Y, D)
            if result == expected_output:
                print(f"Test Passed: input=({X}, {Y}, {D}), output={result}")
                passed += 1
            else:
                print(f"Test Failed: input=({X}, {Y}, {D}), expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input=({X}, {Y}, {D}), error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")

run_tests()
