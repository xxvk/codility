# English ver.
'''
Write a function:
def solution(A, B, K):
This function takes three integers  A ,  B , and  K  and returns the number of integers in the range [A..B] that are divisible by  K . In other words, it calculates:


\{ i : A \leq i \leq B, \, i \mod K = 0 \}


Example:
For  A = 6 ,  B = 11 , and  K = 2 , the function should return  3 , because there are three numbers divisible by  2  within the range [6..11], namely  6, 8,  and  10 .

Assumptions:
	•	 A  and  B  are integers within the range [0..2,000,000,000].
	•	 K  is an integer within the range [1..2,000,000,000].
	•	 A \leq B .
'''



# Chinese ver.
'''
撰寫一個函數：
def solution(A, B, K):
此函數接收三個整數  A ,  B , 和  K ，並返回範圍 [A..B] 中能被  K  整除的整數個數。
換句話說，它計算：


\{ i : A \leq i \leq B, \, i \mod K = 0 \}


範例：
若  A = 6 ,  B = 11 ,  K = 2 ，則函數應返回  3 。因為在範圍 [6..11] 中，有三個數能被  2  整除，分別是  6, 8, 10 。

假設：
	•	 A  和  B  是範圍 [0..2,000,000,000] 內的整數。
	•	 K  是範圍 [1..2,000,000,000] 內的整數。
	•	 A \leq B 。
'''



# Japnese ver.
'''
次の関数を作成してください：
def solution(A, B, K):
この関数は整数  A ,  B ,  K  を受け取り、範囲 [A..B] において  K  で割り切れる整数の個数を返します。つまり、次のように計算します：

\[
\{ i : A \leq i \leq B, \, i \bmod K = 0 \}
\]

例：
 A = 6 ,  B = 11 ,  K = 2  の場合、関数は  3  を返すべきです。なぜなら、範囲 [6..11] で  2  で割り切れる数は  6, 8, 10  の3つだからです。

前提条件:
	•	 A  および  B  は [0..2,000,000,000] の範囲内の整数です。
	•	 K  は [1..2,000,000,000] の範囲内の整数です。
	•	 A \leq B 。
'''


'''
A: from
B: to
K: todo mod
'''
def solution(A, B, K):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not K:
        raise ValueError('input range Error')
    if A == 0 and B == 0:
        return 1
    if A == B:
        mod = A % K
        if mod != 0:
            return 0
        else: return 1

    max_num = 10 ** 9 * 2 
    if A > max_num or A < 0:
        raise ValueError('input range Error')
    if B > max_num or B < 0:
        raise ValueError('input range Error')
    if K > max_num or K < 1:
        raise ValueError('input range Error')
    '''
    checker:    math
    '''
    if B - A < 2:
        return 0
    if K > B:
        return 0
    '''
    main process
    '''
    # math method
    count_up_to_B = B // K
    count_up_to_A_minus_1 = (A - 1) // K if A > 0 else 0
    if A == 0:
        return count_up_to_B + 1 - count_up_to_A_minus_1
    else:
        return count_up_to_B - count_up_to_A_minus_1

test_cases = {
    # Example test cases
    (6, 11, 2): 3,                # Example: range [6..11], divisible by 2 -> {6, 8, 10}

    # Correctness test cases
    (0, 0, 11): 1,                # Single element: A = B = 0, K = 11 -> 0 is divisible by 11
    (10, 10, 5): 1,               # Single element: A = B, and divisible by K
    (10, 10, 7): 0,               # Single element: A = B, but not divisible by K
    (0, 14, 7): 3,                # Multiple divisible elements: 7, 14 in range [0..14]
    (1, 10, 1): 10,               # All numbers divisible: K = 1 -> every number in [1..10]
    (5, 15, 5): 3,                # Divisible by 5: 5, 10, 15 in range [5..15]
    (0, 100, 10): 11,             # Multiples of 10 in range [0..100] -> {0, 10, 20, ..., 100}

    # Edge test cases
    (0, 2000000000, 1): 2000000001,  # Maximum range: K = 1 -> all numbers in range [0..2B]
    (1, 2000000000, 2): 1000000000,  # Large range: K = 2 -> even numbers in range [1..2B]
    (0, 2000000000, 2000000000): 2,  # K = MAX_INT: 0 and 2000000000 are divisible
    (1, 1, 1): 1,                   # Smallest range: A = B = 1, K = 1 -> 1 is divisible
    (2, 2, 2): 1,                   # Single element divisible by K
    (3, 3, 2): 0,                   # Single element not divisible by K

    # Performance test cases
    (0, 1000000000, 1): 1000000001,  # Large range with smallest K
    (100, 123000000, 2): 61499951,   # Large range: K = 2 -> all even numbers in range
    (100, 123000000, 10000): 12300,  # Large range: multiples of 10000
}

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for (A, B, K), expected_output in test_cases.items():
        try:
            result = solution(A, B, K)
            if result == expected_output:
                print(f"Test Passed: input=(A={A}, B={B}, K={K}), output={result}")
                passed += 1
            else:
                print(f"Test Failed: input=(A={A}, B={B}, K={K}), expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input=(A={A}, B={B}, K={K}), error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")


run_tests()
