# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# English ver.
'''
A binary gap in a positive integer N is defined as 
the longest sequence of consecutive zeros surrounded by ones 
on both ends in N’s binary representation.
For instance:
	•	The number 9 has a binary representation of 1001, which includes a binary gap of length ￼.
	•	The number 529 has a binary representation of 1000010001, containing two binary gaps: one of length ￼ and another of length ￼.
	•	The number 20 has a binary representation of 10100, with one binary gap of length ￼.
	•	The number 15 has a binary representation of 1111 and does not have any binary gaps.
	•	The number 32 has a binary representation of 100000 and also has no binary gaps.

Write a function:

def solution(N):

The function takes a positive integer N and returns the length of its longest binary gap. 
If N does not contain a binary gap, the function should return N.

For example:
	•	If  N = 1041 , the binary representation is 10000010001, 
        and the function returns 5 because the longest binary gap is of length ￼.
	•	If  N = 32 , the binary representation is 100000, 
        and the function returns 0, as there are no binary gaps.

Ensure the algorithm is efficient under the following conditions:
	•	N is an integer within the range [1..2,147,483,647].
'''



# Chinese ver.
'''
一個正整數  N  的 二進位間隔 是指  N  的二進位表示中，由 1 包圍的連續 0 所組成的最長序列。

例如：
	•	數字  9 ：二進位 1001 → 包含長度為  2  的二進位間隔。
	•	數字  529 ：二進位 1000010001 → 包含兩個間隔：長度為  4  和  3 。
	•	數字  20 ：二進位 10100 → 包含長度為  1  的間隔。
	•	數字  15 ：二進位 1111 → 沒有任何間隔。
	•	數字  32 ：二進位 100000 → 沒有任何間隔。

請編寫一個函數：

def solution(N):

該函數接收一個正整數  N ，並回傳最長的二進位間隔長度。如果沒有二進位間隔，則回傳  0 。

範例：
	•	若  N = 1041 ，二進位 10000010001 → 最長的間隔長度為  5 。
	•	若  N = 32 ，二進位 100000 → 沒有間隔，回傳  0 。

假設：
	•	 N  是範圍 [1..2,147,483,647] 內的整數。
'''



# Japnese ver.
'''
正の整数  N  における バイナリギャップ とは、2進数表現において 1 に挟まれた連続する0 の最も長い並びのことです。

例えば：
	•	数字  9 ：2進数 1001 → 長さ  2  のバイナリギャップ。
	•	数字  529 ：2進数 1000010001 → 長さ  4  と  3  の2つのギャップ。
	•	数字  20 ：2進数 10100 → 長さ  1  のギャップ。
	•	数字  15 ：2進数 1111 → ギャップなし。
	•	数字  32 ：2進数 100000 → ギャップなし。

次の関数を作成してください：

def solution(N):

この関数は正の整数  N  を受け取り、最も長いバイナリギャップの長さを返します。バイナリギャップが存在しない場合は  0  を返します。

例：
	•	 N = 1041  の場合、2進数 10000010001 → 最長のギャップは  5 。
	•	 N = 32  の場合、2進数 100000 → ギャップがないため  0 。

前提条件：
	•	 N  は [1..2,147,483,647] の範囲の整数です。
'''

def solution(N):
    # Implement your solution here
    '''
    checker:    given ranges
    '''
    if N < 1 or N > 2147483647:
        raise ValueError("N is out of range")
    '''
    checker:    100000...0
    '''
    if N & (N - 1) == 0:
        return 0
    '''
    checker:    111111...1
    '''
    if N & (N + 1) == 0:
        return 0
    
    '''
    main process
    '''
    bin_string = bin(N)[2:]
    # print(bin_string)

    cache_max_gap = 0
    state_now_gap_count = 0
    state_now_isgapping = False
    
    for bit in bin_string:
        if bit == '0':
            if state_now_isgapping == False:
                state_now_isgapping = True
            state_now_gap_count += 1
        if bit == '1':
            cache_max_gap = max(cache_max_gap,state_now_gap_count)
            if state_now_isgapping:
                state_now_gap_count = 0
                state_now_isgapping = False
            
    return cache_max_gap

print(solution(1041))  # expect 输出: 5
print(solution(32))    # expect 输出: 0
print(solution(529))   # expect 输出: 4
print(solution(20))    # expect 输出: 1
print(solution(15))    # expect 输出: 0


# test case
test_cases = {
    1041: 5,       # binary: 10000010001
    15: 0,         # binary: 1111
    32: 0,         # binary: 100000
    1: 0,          # binary: 1
    5: 1,          # binary: 101
    6: 0,          # binary: 110
    328: 2,        # binary: 101001000
    16: 0,         # binary: 2^4 = 10000
    1024: 0,       # binary: 2^10 = 10000000000
    9: 2,          # binary: 1001
    11: 1,         # binary: 1011
    19: 2,         # binary: 10011
    42: 1,         # binary: 101010
    1162: 3,       # binary: 10010001010
    51712: 2,      # binary: 110010100000000
    561892: 3,     # binary: 10001001001011100100
    66561: 9,      # binary: 10000010000000001
    6291457: 20,   # binary: 11000000000000000000001
    74901729: 4,   # binary: 100011101101110100011100001
    805306373: 25, # binary: 110000000000000000000000000101
    1376796946: 5, # binary: 1010010000100000100000100010010
    1073741825: 29,# binary: 1000000000000000000000000000001
    1610612737: 28 # binary: 1100000000000000000000000000001
}


def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for input_value, expected_output in test_cases.items():
        try:
            result = solution(input_value)
            if result == expected_output:
                print(f"Test Passed: input={input_value}, output={result}")
                passed += 1
            else:
                print(f"Test Failed: input={input_value}, expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input={input_value}, error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")

# 运行测试
run_tests()

