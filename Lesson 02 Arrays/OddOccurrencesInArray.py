# English ver.
'''
A non-empty array  A  consisting of  N  integers is provided. 
The array contains an odd number of elements, 
and every element in the array can be paired 
with another element of the same value, except for one element that has no pair.

For example, consider the array  A :
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

  	•	The elements at indices 0 and 2 have the value  9 .
	•	The elements at indices 1 and 3 have the value  3 .
	•	The elements at indices 4 and 6 have the value  9 .
	•	The element at index 5 has the value  7 , which has no pair.

Write a function:

def solution(A):

The function should return  7 , as it is the only value without a pair.

Write an efficient algorithm under the following assumptions:
	•	 N  is an odd integer within the range [1..1,000,000].
	•	Each element in  A  is an integer within the range [1..1,000,000,000].
	•	All values in  A , except one, appear an even number of times.

'''



# Chinese ver.
'''
給定一個包含  N  個整數的非空陣列  A 。
該陣列包含奇數個元素，其中每個元素都有一個相同值的元素可以配對，除了其中一個元素無法配對。

例如，考慮陣列  A ：
	•	索引 0 和 2 的元素值為  9 。
	•	索引 1 和 3 的元素值為  3 。
	•	索引 4 和 6 的元素值為  9 。
	•	索引 5 的元素值為  7 ，無法配對。
請撰寫一個函數：
def solution(A):
    此函數接收一個滿足上述條件的陣列  A ，並回傳無法配對的元素值。
    函數應回傳  7 ，因為它是唯一無法配對的值。

撰寫一個高效的演算法，並符合以下假設：
	•	 N  是範圍 [1..1,000,000] 內的奇數整數。
	•	陣列  A  的每個元素是範圍 [1..1,000,000,000] 內的整數。
	•	陣列  A  中，除了其中一個值以外，其餘所有值的出現次數均為偶數。

'''



# Japnese ver.
'''
非空の配列  A （ N  個の整数で構成）が与えられます。
この配列には奇数個の要素が含まれ、各要素は同じ値を持つ別の要素とペアになります。
ただし、1つの要素だけはペアが存在しません。

例えば、次の配列  A  を考えます：
  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9

  	•	インデックス 0 と 2 の要素の値は  9 。
	•	インデックス 1 と 3 の要素の値は  3 。
	•	インデックス 4 と 6 の要素の値は  9 。
	•	インデックス 5 の要素の値は  7  で、ペアが存在しません。

次の関数を作成してください：
def solution(A):
この関数は、上記の条件を満たす配列  A  を受け取り、ペアにならない要素の値を返します。
関数は  7  を返すべきです。これはペアにならない唯一の値です。

以下の仮定に基づき、高効率なアルゴリズムを作成してください：
	•	 N  は [1..1,000,000] の範囲内の奇数。
	•	配列  A  の各要素は [1..1,000,000,000] の範囲内の整数。
	•	配列  A  のすべての値は1つを除き、偶数回出現します。

'''


def solution(A):
    # Implement your solution here
    '''
    checker:    input range
    '''
    N =  len(A)
    if N > 1000000:
        raise ValueError('input range Error')
    '''
    checker:    empty
    '''
    if not A:
        raise ValueError('input range Error')
    '''
    checker:    single elements array
    '''
    if N == 1:
        return A[0]
    
    '''
    main process
    '''
    cache_map = { }
    for num in A:
        count_for_num = cache_map.get(num, 0)
        cache_map[num] = count_for_num + 1

    # [3, 3, 1] -> 1
    for (num, count) in cache_map.items():
        if count == 1:
            return num
    # [3, 3, 1, 1, 1] -> 1
    for (num, count) in cache_map.items():
        if count % 2 == 1:
            return num

    return None

# 测试用例
test_cases = {
    # Example test
    (tuple([9, 3, 9, 3, 9, 7, 9])): 7,  # example1
    
    # Correctness tests
    (tuple([1, 2, 1, 2, 3])): 3,             # simple1
    (tuple([4, 5, 4, 5, 4, 5, 6, 6, 6, 6, 7])): 7,  # simple2
    (tuple([42])): 42,                       # extreme_single_item
    (tuple([1] * 200 + [2])): 2,             # small1
    (tuple([3] * 600 + [4])): 4,             # small2
    
    # Performance tests
    (tuple([i for i in range(1, 2001)] * 2 + [2001])): 2001,  # medium1
    (tuple([i for i in range(1, 50002)] * 2 + [50002])): 50002,  # medium2
    (tuple([i for i in range(1, 500000)] * 2 + [500000])): 500000,  # big1
    (tuple([999999] * 999998 + [1000000])): 1000000,  # big2
}

# 运行测试
def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for input_array, expected_output in test_cases.items():
        try:
            # Convert tuple back to list for processing
            result = solution(list(input_array))
            if result == expected_output:
                print(f"Test Passed: input={list(input_array)}, output={result}")
                passed += 1
            else:
                print(f"Test Failed: input={list(input_array)}, expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input={list(input_array)}, error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")

# 执行测试
run_tests()
