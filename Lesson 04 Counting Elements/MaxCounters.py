# English ver.
'''
You are given N counters, all starting at 0. Two operations can be performed on them:
	1.	increase(X): Increase the value of counter X by 1.
	2.	max counter: Set all counters to the highest value among them.

An array A of M integers is provided. This array specifies the sequence of operations:
	•	If A[K] = X where 1 ≤ X ≤ N, perform the increase(X) operation.
	•	If A[K] = N + 1, perform the max counter operation.

For example, given N = 5 and array A as follows:

A[0] = 3
A[1] = 4
A[2] = 4
A[3] = 6
A[4] = 1
A[5] = 4
A[6] = 4

The counters change as follows after each operation:
(0, 0, 1, 0, 0)  # A[0] = 3 -> increase(3)
(0, 0, 1, 1, 0)  # A[1] = 4 -> increase(4)
(0, 0, 1, 2, 0)  # A[2] = 4 -> increase(4)
(2, 2, 2, 2, 2)  # A[3] = 6 -> max counter
(3, 2, 2, 2, 2)  # A[4] = 1 -> increase(1)
(3, 2, 2, 3, 2)  # A[5] = 4 -> increase(4)
(3, 2, 2, 4, 2)  # A[6] = 4 -> increase(4)

The goal is to calculate the final values of all counters after processing all operations.

Write a function:
def solution(N, A):
This function takes an integer N and an array A as input and returns an array of integers representing the final values of the counters.

For instance, given A:
The function should return [3, 2, 2, 4, 2].

The algorithm must meet the following constraints:
	•	N and M are integers in the range [1..100,000].
	•	Each element in array A is an integer in the range [1..N + 1].
'''



# Chinese ver.
'''
您有 N 個計數器，初始值均為 0，並可以對其進行以下兩種操作：
	1.	increase(X)：將計數器 X 的值加 1。
	2.	max counter：將所有計數器的值設定為目前最大計數器的值。

給定一個長度為 M 的整數陣列 A，此陣列代表一系列連續操作：
	•	如果 A[K] = X，且 1 ≤ X ≤ N，則執行操作 increase(X)。
	•	如果 A[K] = N + 1，則執行操作 max counter。

例如，若給定 N = 5 和以下陣列 A：
A[0] = 3
A[1] = 4
A[2] = 4
A[3] = 6
A[4] = 1
A[5] = 4
A[6] = 4

每次操作後計數器的值變化如下：
(0, 0, 1, 0, 0)  # A[0] = 3 -> increase(3)
(0, 0, 1, 1, 0)  # A[1] = 4 -> increase(4)
(0, 0, 1, 2, 0)  # A[2] = 4 -> increase(4)
(2, 2, 2, 2, 2)  # A[3] = 6 -> max counter
(3, 2, 2, 2, 2)  # A[4] = 1 -> increase(1)
(3, 2, 2, 3, 2)  # A[5] = 4 -> increase(4)
(3, 2, 2, 4, 2)  # A[6] = 4 -> increase(4)

目標是計算所有操作執行完後，所有計數器的最終值。

請撰寫以下函數：
def solution(N, A):
該函數接收一個整數 N 和陣列 A，並返回一個整數陣列，表示所有計數器的最終值。

例如，給定：
函數應返回 [3, 2, 2, 4, 2]。

演算法需要符合以下條件：
	•	N 和 M 是範圍 [1..100,000] 內的整數。
	•	陣列 A 中的每個元素皆為範圍 [1..N + 1] 內的整數。
1.	输入的规模很大：
	•	N 和数组 A 的长度 M 最大可能是 100,000。
	•	如果直接暴力实现（比如每次 max counter 都去更新整个数组），会超时。
2.	如何优化：
	•	记录每次 max counter 的最大值，延迟到最后再更新所有计数器的值，而不是每次都去更新整个数组。
'''



# Japnese ver.
'''
N 個のカウンターがあり、初期値はすべて 0 です。それに対して次の 2 つの操作を行うことができます：
	1.	increase(X)：カウンター X の値を 1 増やします。
	2.	max counter：すべてのカウンターを、現在の最大カウンターの値に設定します。

M 個の整数からなる配列 A が与えられています。この配列は操作の順序を表します：
	•	A[K] = X（1 ≤ X ≤ N）の場合、操作 increase(X) を実行します。
	•	A[K] = N + 1 の場合、操作 max counter を実行します。

例えば、N = 5 で次の配列 A が与えられた場合：
A[0] = 3
A[1] = 4
A[2] = 4
A[3] = 6
A[4] = 1
A[5] = 4
A[6] = 4

各操作後のカウンター値は次のようになります：
(0, 0, 1, 0, 0)  # A[0] = 3 -> increase(3)
(0, 0, 1, 1, 0)  # A[1] = 4 -> increase(4)
(0, 0, 1, 2, 0)  # A[2] = 4 -> increase(4)
(2, 2, 2, 2, 2)  # A[3] = 6 -> max counter
(3, 2, 2, 2, 2)  # A[4] = 1 -> increase(1)
(3, 2, 2, 3, 2)  # A[5] = 4 -> increase(4)
(3, 2, 2, 4, 2)  # A[6] = 4 -> increase(4)

目的は、すべての操作を実行した後、各カウンターの最終値を計算することです。

次の関数を作成してください：
def solution(N, A):
この関数は整数 N と配列 A を受け取り、カウンターの最終値を表す整数の配列を返します。

例えば：
この関数は [3, 2, 2, 4, 2] を返します。

アルゴリズムは次の制約を満たす必要があります：
	•	N と M は [1..100,000] の範囲内の整数です。
	•	配列 A の各要素は [1..N + 1] の範囲内の整数です。
'''

def solution(N, A):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not A or not N:
        raise ValueError('input range Error')
    if N > 100000 or N < 1:
        raise ValueError('input range Error')
    M = len(A)
    if M > 100000 or M < 1:
        raise ValueError('input range Error')
    if min(A) < 1 or max(A) > N + 1:
        raise ValueError('input range Error')
    '''
    main process
    '''
    
    state_counter = [0] * N
    cache_advance_max_ctr = 0       # Track the real-time maximum value
    cache_base_line = 0             # Track the delayed max counter value

    for num in A:
        if num <= N: 
            # increase(num)
            index = num - 1
            if state_counter[index] < cache_base_line:
                state_counter[index] = cache_base_line
            state_counter[index] += 1
            cache_advance_max_ctr = max(cache_advance_max_ctr, state_counter[index])
            
        elif num == N + 1:
            # max counter
            cache_base_line = cache_advance_max_ctr
            # Update the current_max to delay the max counter operation

    # Finalize counters: ensure all are updated to at least current_max
    for index in range(N):
        if state_counter[index] < cache_base_line:
            state_counter[index] = cache_base_line

    return state_counter


test_cases = {
    # Example case
    (5, (3, 4, 4, 6, 1, 4, 4)): [3, 2, 2, 4, 2],

    # Edge cases
    (1, (1, 2, 1, 1)): [3],
    (1, (2, 2, 2, 2)): [0],
    (3, (4, 4, 4)): [0, 0, 0],
    (5, (1, 2, 3, 4, 5, 6)): [1, 1, 1, 1, 1],

    # Small cases
    (3, (1, 2, 3, 4, 1, 2, 3, 4)): [2, 2, 2],
    (5, (1, 2, 3, 3, 3, 6, 6, 2)): [3, 4, 3, 3, 3],

    # Large cases
    (5, (3,) * 100000): [ 0, 0, 100000, 0, 0],
    (5, (6,) * 100000): [0, 0, 0, 0, 0],
    (5, (3,) * 50000 + (6,) * 50000): [50000, 50000, 50000, 50000, 50000],
    (100000, (1, 100001, 2) * 33333): [33333] + [33334] + [33333] * 99998,
}

def run_tests():
    print("Running tests...\n")


    passed = 0
    failed = 0

    for (N, input_array), expected_output in test_cases.items():
        try:
            result = solution(N, list(input_array))
            if result == expected_output:
                print(f"Test Passed: N={N}, input_length={len(input_array)}, output={result[:10]}...")
                passed += 1
            else:
                print(f"Test Failed: N={N}, input_length={len(input_array)}, expected={expected_output[:10]}..., got={result[:10]}...")
                failed += 1
        except Exception as e:
            print(f"Test Error: N={N}, input_length={len(input_array)}, error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")


# Run the tests
run_tests()
