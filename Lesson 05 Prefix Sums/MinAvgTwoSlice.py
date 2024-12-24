# English ver.
'''
A non-empty array A of size N is given. A pair of indices (P, Q) is called a slice of the array if 0 ≤ P < Q < N. A slice must contain at least two elements.

The average of a slice (P, Q) is calculated as the sum of elements in the slice divided by the length of the slice:


\text{average} = \frac{\text{A[P] + A[P+1] + … + A[Q]}}{\text{Q − P + 1}}.


For example, consider the array A:
A[0] = 4
A[1] = 2
A[2] = 2
A[3] = 5
A[4] = 1
A[5] = 5
A[6] = 8

Here are some example slices:
	•	Slice (1, 2) has an average of (2 + 2) / 2 = 2.
	•	Slice (3, 4) has an average of (5 + 1) / 2 = 3.
	•	Slice (1, 4) has an average of (2 + 2 + 5 + 1) / 4 = 2.5.

The goal is to find the starting position of the slice with the minimal average. If there are multiple slices with the same minimal average, return the smallest starting position.

Write a function:

def solution(A):
that takes a non-empty array A of size N and returns the starting position of the slice with the minimal average.

Example

For the array:
The function should return 1, as explained above.
Assumptions
	•	 N  is an integer in the range [2..100,000].
	•	Each element of  A  is an integer in the range [-10,000..10,000].
'''



# Chinese ver.
'''
一個非空的陣列 A（大小為  N ）已給出。一對索引 (P, Q) 被稱為陣列的一個片段（slice），如果滿足 0 ≤ P < Q < N。片段必須包含至少兩個元素。

片段 (P, Q) 的平均值計算為該片段中元素的總和除以片段的長度：


\text{平均值} = \frac{\text{A[P] + A[P+1] + … + A[Q]}}{\text{Q − P + 1}}。


例如，考慮陣列 A：
A[0] = 4
A[1] = 2
A[2] = 2
A[3] = 5
A[4] = 1
A[5] = 5
A[6] = 8


以下是一些例子片段：
	•	片段 (1, 2) 的平均值為 (2 + 2) / 2 = 2。
	•	片段 (3, 4) 的平均值為 (5 + 1) / 2 = 3。
	•	片段 (1, 4) 的平均值為 (2 + 2 + 5 + 1) / 4 = 2.5。

目標是找到平均值最小的片段的起始位置。如果有多個片段的平均值相同，返回起始位置最小的那一個。

函數說明

編寫函數：


def solution(A):
該函數接收一個大小為  N  的非空陣列 A，返回具有最小平均值的片段的起始位置。

範例

對於以下陣列：
函數應返回 1，如上所述。
假設條件
	•	 N  是範圍 [2..100,000] 內的整數。
	•	陣列  A  的每個元素是範圍 [-10,000..10,000] 內的整數。
'''



# Japnese ver.
'''
非空の配列 A（サイズ  N ）が与えられます。インデックスのペア (P, Q) は、0 ≤ P < Q < N を満たす場合にスライス（部分配列）と呼ばれます。スライスは少なくとも2つの要素を含む必要があります。

スライス (P, Q) の平均値は、そのスライス内の要素の合計をスライスの長さで割った値として計算されます：


\text{平均値} = \frac{\text{A[P] + A[P+1] + … + A[Q]}}{\text{Q − P + 1}}。


例えば、配列 A を考えます：
A[0] = 4
A[1] = 2
A[2] = 2
A[3] = 5
A[4] = 1
A[5] = 5
A[6] = 8

いくつかのスライスの例：
	•	スライス (1, 2) の平均値は (2 + 2) / 2 = 2。
	•	スライス (3, 4) の平均値は (5 + 1) / 2 = 3。
	•	スライス (1, 4) の平均値は (2 + 2 + 5 + 1) / 4 = 2.5。

目標は、平均値が最小のスライスの開始位置を見つけることです。同じ平均値のスライスが複数存在する場合は、開始位置が最も小さいスライスを返します。

関数説明

次の関数を記述してください：

def solution(A):
この関数は、サイズ  N  の非空の配列 A を受け取り、平均値が最小のスライスの開始位置を返します。

例

次の配列の場合：
関数は 1 を返すべきです。
仮定条件
	•	 N  は範囲 [2..100,000] 内の整数。
	•	配列  A  の各要素は範囲 [-10,000..10,000] 内の整数。
'''

def solution(A):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not A:
        raise ValueError('input range Error')
    N = len(A)
    if N > 100000:
        raise ValueError('input range Error')
    if N == 1 or N == 2:
        return 0
    '''
    main process
    '''
    count_2pairs = N - 1
    count_3pairs = N - 2
    two_sum_array = [0] * count_2pairs
    three_sum_array = [0] * count_3pairs
    for i in range(0, count_2pairs):
        a_two_sum = A[i] + A[i + 1]
        two_sum_array[i] = a_two_sum

    for i in range(0, count_3pairs):
        a_three_sum = A[i] + A[i + 1] + A[i + 2]
        three_sum_array[i] = a_three_sum

    set2sum = set(two_sum_array)
    set3sum = set(three_sum_array)
    min2sum = min(set2sum)
    min3sum = min(set3sum)
    if min3sum / 3 > min2sum / 2:
        # choose 2sum
        for i in range(0, count_2pairs):
            if min2sum == two_sum_array[i]:
                return i
    else:
        # choose 3sum
        for i in range(0, count_3pairs):
            if min3sum == three_sum_array[i]:
                return i
    
    return -1


test_cases = {
    # Example case
    (4, 2, 2, 5, 1, 5, 8): 1,  # Example case

    # Edge cases
    (1, 2): 0,                # Smallest array, 2 elements
    (1, 2, 3): 0,             # Smallest array, 3 elements
    (-10000, -10000): 0,      # All minimal values
    (10000, 10000): 0,        # All maximal values

    # Performance cases
    tuple([-1, 1] * 50000): 0,  # Alternating sequence
    tuple([1] * 100000): 0,     # All elements the same
    tuple([i for i in range(1, 100001)]): 0,  # Increasing sequence
    tuple([-i for i in range(1, 100001)]): 99998,  # Decreasing sequence
}

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for input_array, expected_output in test_cases.items():
        try:
            result = solution(list(input_array))
            if result == expected_output:
                print(f"Test Passed: input=length {len(input_array)}, output={result}")
                passed += 1
            else:
                print(f"Test Failed: input=length {len(input_array)}, expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input=length {len(input_array)}, error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")


run_tests()
