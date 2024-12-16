# English ver.
'''
A non-empty array  A  containing  N  integers is given. The array  A  represents numbers arranged on a tape.

You can split this tape into two non-empty parts at any integer  P , where  0 < P < N . The split results in two parts:
	•	 A[0], A[1], …, A[P-1] 
	•	 A[P], A[P+1], …, A[N-1] .

The difference between the two parts is calculated as:

\text{Difference} = |(A[0] + A[1] + … + A[P-1]) - (A[P] + A[P+1] + … + A[N-1])|


In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

Example:
Consider the array  A :
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
  You can split the tape at four places:
	1.	 P = 1 : Difference =  |3 - 10| = 7 
	2.	 P = 2 : Difference =  |4 - 9| = 5 
	3.	 P = 3 : Difference =  |6 - 7| = 1 
	4.	 P = 4 : Difference =  |10 - 3| = 7 

Write a function:
def solution(A):
This function takes a non-empty array  A  of  N  integers and returns the minimal difference that can be achieved.

Example:
For the array  A :
The function should return  1 , as the smallest difference occurs when  P = 3 .

Assumptions:
	•	 N  is an integer within the range [2..100,000].
	•	Each element of  A  is an integer within the range [-1,000..1,000].
'''



# Chinese ver.
'''
給定一個包含  N  個整數的非空陣列  A 。陣列  A  表示膠帶上的數字。

你可以在任意  P  位置將膠帶分成兩個非空部分，其中  0 < P < N 。分割結果為：
	•	 A[0], A[1], …, A[P-1] 
	•	 A[P], A[P+1], …, A[N-1] 。

兩部分之間的差值計算公式為：

\text{差值} = |(A[0] + A[1] + … + A[P-1]) - (A[P] + A[P+1] + … + A[N-1])|


換句話說，這是兩部分的總和之間的絕對差。

範例：
考慮陣列  A ：
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
  可以在四個位置分割膠帶：
	1.	 P = 1 : 差值 =  |3 - 10| = 7 
	2.	 P = 2 : 差值 =  |4 - 9| = 5 
	3.	 P = 3 : 差值 =  |6 - 7| = 1 
	4.	 P = 4 : 差值 =  |10 - 3| = 7 

請撰寫一個函數：
def solution(A):
此函數接受包含  N  個整數的非空陣列  A ，並返回可以達成的最小差值。

範例：
對於陣列  A ：
函數應返回  1 ，因為當  P = 3  時差值最小。

假設：
	•	 N  是範圍 [2..100,000] 內的整數。
	•	 A  中的每個元素是範圍 [-1,000..1,000] 內的整數。
'''



# Japnese ver.
'''
非空の配列  A （ N  個の整数）が与えられています。配列  A  はテープ上の数字を表します。

テープを任意の  P  の位置で分割し、2つの非空部分に分けることができます（ただし、 0 < P < N ）。分割結果は以下のようになります：
	•	 A[0], A[1], …, A[P-1] 
	•	 A[P], A[P+1], …, A[N-1] 。

差分 は次の式で計算されます：

\text{差分} = |(A[0] + A[1] + … + A[P-1]) - (A[P] + A[P+1] + … + A[N-1])|


つまり、2つの部分の合計の絶対差を求めます。

例：
配列  A  を考えます：
  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
テープを次の4箇所で分割できます：
	1.	 P = 1 : 差分 =  |3 - 10| = 7 
	2.	 P = 2 : 差分 =  |4 - 9| = 5 
	3.	 P = 3 : 差分 =  |6 - 7| = 1 
	4.	 P = 4 : 差分 =  |10 - 3| = 7 

次の関数を作成してください：
def solution(A):
この関数は、 N  個の整数を含む非空配列  A  を受け取り、達成可能な最小の差分を返します。

例：
配列  A  が次の場合：
関数は  1  を返すべきです。最小の差分は  P = 3  の場合に発生します。

前提条件：
	•	 N  は [2..100,000] の範囲内の整数です。
	•	 A  の各要素は [-1,000..1,000] の範囲内の整数です。
'''


"""
    Find the minimal difference by splitting the array.
"""
def solution(A):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not A:
        raise ValueError('input range Error')
    N = len(A)
    if N < 2 or N > 100000:
        raise ValueError('input range Error')
    for num in A:
        if abs(num) > 1000:
             raise ValueError('input range Error')

    '''
    main process
    '''
    total_sum = sum(A)

    cache_left_sum = 0
    cache_min_difference = float('inf')
    
    for numP in range(1, N):
        cache_left_sum += A[numP - 1]
        right_sum = total_sum - cache_left_sum
        new_diff = abs(cache_left_sum - right_sum)
        cache_min_difference = min(new_diff, cache_min_difference)

    return cache_min_difference


# Example test
test_cases = {
    (tuple([3, 1, 2, 4, 3])): 1,  # example

    # Correctness tests
    (tuple([1, 1])): 0,                  # double
    (tuple([3, 1, 2, 4, 3])): 1,         # simple_positive
    (tuple([-3, -1, -2, -4, -3])): 1,    # simple_negative
    (tuple([1, 2, 3, 4])): 2,            # simple_boundary
    (tuple([10, 20, 30, 40, 50])): 30,   # small_random

    # Edge cases
    (tuple([-1000, 1000])): 2000,        # extreme_positive_negative
    (tuple([-500, -500, 500, 500])): 1000,  # balanced positive and negative

    # Performance tests
    (tuple([i for i in range(1000)])): 358,                # small_range
    (tuple([-1, 1] * 50000)): 0,                        # large_ones
    (tuple([1] * 100000)): 0,                           # large_constant
    (tuple([i % 1000 for i in range(100000)])): 0,         # large_sequence
    (tuple([(-1)**i * 1000 for i in range(100000)])): 0 # alternating large values
}

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for input_array, expected_output in test_cases.items():
        try:
            result = solution(list(input_array))
            if result == expected_output:
                print(f"Test Passed: input={len(input_array)}, output={result}")
                passed += 1
            else:
                print(f"Test Failed: input={len(input_array)}, expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input={len(input_array)}, error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")


run_tests()