# English ver.
'''
A non-empty array  A , consisting of  N  integers, is given. The elements in array  A  represent consecutive cars on a road.

The array contains only 0s and 1s:
	•	0 represents a car moving east.
	•	1 represents a car moving west.

The goal is to count the passing car pairs. A pair of cars (P, Q), where  0 \leq P < Q < N , is considered passing when car  P  (traveling east) comes before car  Q  (traveling west).

Example:
Consider the array  A :

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1

  The passing car pairs are:
(0, 1), (0, 3), (0, 4), (2, 3), (2, 4), giving a total of 5 pairs.

Write a function:
def solution(A):
This function, given a non-empty array  A  of  N  integers, returns the total number of passing car pairs.

If the number of passing car pairs exceeds  1,000,000,000 , the function should return -1.

Example:
For the array  A :
The function should return  5 , as explained above.

Assumptions:
	•	 N  is an integer in the range [1..100,000].
	•	Each element in array  A  is either  0  or  1 .
'''



# Chinese ver.
'''
給定一個非空陣列  A ，其中包含  N  個整數。陣列  A  的連續元素代表道路上的連續車輛。

陣列  A  只包含 0 和 1：
	•	0 代表向東行駛的車輛。
	•	1 代表向西行駛的車輛。

目標是計算交會車輛對的數量。當車輛  P （向東行駛）出現在車輛  Q （向西行駛）之前（ 0 \leq P < Q < N ），則稱這對車輛為交會車輛。

範例：
考慮陣列  A ：
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
交會車輛對為：
(0, 1), (0, 3), (0, 4), (2, 3), (2, 4)，總共 5 對。

請撰寫一個函數：
  def solution(A):
  此函數接收一個非空的陣列  A ，返回交會車輛對的總數。

如果交會車輛對的數量超過  1,000,000,000 ，則返回 -1。

範例：
對於陣列  A ：
函數應返回  5 ，如上所述。

假設：
	•	 N  的範圍是 [1..100,000]。
	•	陣列  A  的每個元素只能是  0  或  1 。
'''



# Japnese ver.
'''
非空の配列  A  が与えられ、配列には  N  個の整数が含まれています。配列  A  の要素は道路上の連続した車を表します。

配列  A  には 0 と 1 だけが含まれます：
	•	0 は東に向かって進む車を表します。
	•	1 は西に向かって進む車を表します。

目標はすれ違いの車のペアを数えることです。車  P （東向き）が車  Q （西向き）の前に現れる場合（ 0 \leq P < Q < N ）、これを「すれ違いのペア」とします。

例：
配列  A  を考えます：
  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
すれ違いのペアは以下の通りです：
(0, 1), (0, 3), (0, 4), (2, 3), (2, 4)
合計で  5  ペアです。

次の関数を作成してください：
  def solution(A):
  
  この関数は非空の配列  A  を受け取り、すれ違いの車のペアの数を返します。

すれ違いのペアの数が  1,000,000,000  を超える場合、関数は -1 を返します。

例：
配列  A ：
関数は  5  を返すべきです。

前提条件：
	•	 N  は [1..100,000] の範囲内の整数です。
	•	配列  A  の各要素は  0  または  1  のいずれかです。
'''

def solution(A):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not A:
        return 0
    N = len(A)
    max_count = 100000
    error_code_boundary = -1
    if N > max_count:
        return error_code_boundary
    '''
    main process
    '''
    index_of_zeros = list([])
    index_of_ones = list([])
    count_of_pairs = 0
    max_num_pairs = 10 ** 9
    for index in range(N):
        if A[index] == 0:
            index_of_zeros.append(index)
        if A[index] == 1:
            index_of_ones.append(index)

    # print(index_of_zeros)
    # print(index_of_ones)
    count_of_ones = len(index_of_ones)
    cache_pointer_now_one = 0

    for zero_index in index_of_zeros:
        for one_i in range(cache_pointer_now_one, count_of_ones):
            one_index = index_of_ones[one_i]
            if (one_index > zero_index):
                count_of_pairs += count_of_ones - one_i
                if count_of_pairs > max_num_pairs:
                    return error_code_boundary
                break
            else:
                cache_pointer_now_one = one_i
    return count_of_pairs

test_cases = {
    # 示例测试
    tuple([0, 1, 0, 1, 1]): 5,                        # example

    # 正确性测试
    tuple([0]): 0,                                    # single: only one car (0)
    tuple([1]): 0,                                    # single: only one car (1)
    tuple([0, 1]): 1,                                 # double: one passing pair
    tuple([1, 0]): 0,                                 # double: no passing pairs
    tuple([0, 0, 1, 1]): 4,                           # simple: two pairs from each 0
    tuple([1, 1, 0, 0]): 0,                           # simple: no pairs

    # 性能测试
    tuple([0] * 50000 + [1] * 50000): -1,     # large_big_answer: edge case with many pairs
    tuple([0, 1] * 50000): -1,                # large_alternate: alternating pattern
    tuple([0] * 100000): 0,                           # large_extreme: all zeros
    tuple([1] * 100000): 0,                           # large_extreme: all ones
    tuple([0, 0, 0, 0, 1]): 4,                        # minimal large pairs
    tuple([0, 1] * 25000 + [1] * 50000): -1,   # mixed: alternating with more trailing 1s
}

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for input_array, expected_output in test_cases.items():
        try:
            result = solution(list(input_array))  # 转换为list
            if result == expected_output:
                print(f"Test Passed: input size={len(input_array)}, output={result}")
                passed += 1
            else:
                print(f"Test Failed: input size={len(input_array)}, expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input size={len(input_array)}, error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")


# 执行测试
run_tests()
