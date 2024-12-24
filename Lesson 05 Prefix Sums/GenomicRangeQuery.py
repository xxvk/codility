# English ver.
'''
A DNA sequence can be described as a string made up of the letters A, C, G, and T, which represent four types of nucleotides. Each nucleotide has an associated impact factor as follows:
	•	A → 1
	•	C → 2
	•	G → 3
	•	T → 4

You need to answer multiple queries, each asking for the minimum impact factor of nucleotides in a specific part of the DNA sequence.

The DNA sequence is given as a non-empty string  S = S[0]S[1]…S[N-1] , where  N  is the length of the string. The queries are defined in two non-empty arrays,  P  and  Q , each containing  M  integers.
The K-th query ( 0 \leq K < M ) asks you to determine the minimum impact factor of nucleotides in the substring from position  P[K]  to  Q[K]  (inclusive).

Example:
Consider  S = “CAGCCTA”  and the arrays  P  and  Q  defined as:

P[0] = 2    Q[0] = 4
P[1] = 5    Q[1] = 5
P[2] = 0    Q[2] = 6

The answers for these  M = 3  queries are:
	1.	The substring between positions  2  and  4  is G, C, C. The minimum impact factor is 2 (C).
	2.	The substring between positions  5  and  5  is T. The impact factor is 4.
	3.	The substring between positions  0  and  6  (entire string) includes all nucleotides, with A (impact factor 1) as the minimum.

The function should return [2, 4, 1].

Write a function:

def solution(S, P, Q):

This function takes a string  S  and two arrays  P  and  Q , and returns an array of integers containing the answers to all the queries.

Assumptions:
	•	 N :  [1..100,000]  (length of string  S ).
	•	 M :  [1..50,000]  (number of queries).
	•	Elements in  P  and  Q :  [0..N-1] .
	•	 P[K] \leq Q[K]  for all  0 \leq K < M .
	•	 S  contains only the uppercase letters A, C, G, T.
'''



# Japnese ver.
'''
DNA 配列は A、C、G、T の文字列で表され、それぞれの文字は核酸を示します。各核酸には以下のような 影響因子（数値）が割り当てられています：
	•	A → 1
	•	C → 2
	•	G → 3
	•	T → 4

複数のクエリが与えられ、それぞれのクエリはDNA配列の特定部分における最小の影響因子を求めます。

DNA 配列  S = S[0]S[1]…S[N-1]  が与えられ、長さ  M  の配列  P  と  Q  でクエリが定義されます。
K番目のクエリ ( 0 \leq K < M ) では、位置  P[K]  から  Q[K] （両端を含む）までの影響因子の最小値を求めます。

例：
 S = “CAGCCTA”  と配列  P ,  Q  が次のように与えられます：
P[0] = 2    Q[0] = 4
P[1] = 5    Q[1] = 5
P[2] = 0    Q[2] = 6
この  M = 3  のクエリに対する答えは次の通りです：
	1.	位置  2  から  4  の部分文字列は G, C, C で、最小影響因子は 2（C）。
	2.	位置  5  から  5  の部分文字列は T で、影響因子は 4。
	3.	位置  0  から  6  の部分文字列（全体）は A を含み、その影響因子は 1。

関数：
def solution(S, P, Q):
この関数は、文字列  S  と2つの配列  P ,  Q  を受け取り、各クエリに対する答えを整数配列として返します。

前提条件：
	•	 N ： [1..100,000] （文字列  S  の長さ）。
	•	 M ： [1..50,000] （クエリの数）。
	•	 P  および  Q  の要素： [0..N-1] 。
	•	 P[K] \leq Q[K]  で  0 \leq K < M 。
	•	 S  は A、C、G、T のみで構成されます。
'''


# Chinese ver.
'''
DNA 序列可以表示為由字母 A、C、G、T 組成的字串，分別代表四種核苷酸。每個核苷酸有一個對應的影響因子：
	•	A → 1
	•	C → 2
	•	G → 3
	•	T → 4

現在，您需要回答多個查詢，查詢內容是指定 DNA 序列中的某一部分核苷酸的最小影響因子。

DNA 序列由非空字串  S = S[0]S[1]…S[N-1]  組成，其中  N  是字串的長度。查詢定義在兩個非空陣列  P  和  Q  中，每個陣列有  M  個整數。
第 K 個查詢（ 0 \leq K < M ）要求您找出從位置  P[K]  到  Q[K] （包含）的子字串中核苷酸的最小影響因子。

範例：
考慮字串  S = “CAGCCTA”  和陣列  P  和  Q  如下：
P[0] = 2    Q[0] = 4
P[1] = 5    Q[1] = 5
P[2] = 0    Q[2] = 6

這  M = 3  個查詢的答案是：
	1.	位置  2  到  4  之間的子字串是 G, C, C，最小影響因子是 2（C）。
	2.	位置  5  到  5  的子字串是 T，影響因子是 4。
	3.	位置  0  到  6  的子字串（整個字串）包含所有核苷酸，其中最小的是 A（影響因子 1）。

函數應返回 [2, 4, 1]。

撰寫一個函數：
def solution(S, P, Q):
此函數接收字串  S  和兩個陣列  P  和  Q ，並返回一個整數陣列，包含所有查詢的答案。

假設：
	•	 N ： [1..100,000] （字串  S  的長度）。
	•	 M ： [1..50,000] （查詢的數量）。
	•	 P  和  Q  的元素： [0..N-1] 。
	•	 P[K] \leq Q[K] ，其中  0 \leq K < M 。
	•	 S  僅包含字母 A、C、G、T。
'''

def transS_toNum(bitS):
    # •	A → 1
    # •	C → 2
    # •	G → 3
    # •	T → 4
    if bitS == 'A': return 1
    if bitS == 'C': return 2
    if bitS == 'G': return 3
    if bitS == 'T': return 4
    return -1

def solution(S, P, Q):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not S:
        return []
    if not P or not Q:
        return []
    N = len(S)
    if N > 100000:
        raise ValueError('input range Error')
    M = len(P)
    Mq = len(Q)
    if M > 50000:
        raise ValueError('input range Error')
    if M != Mq:
        raise ValueError('input range Error')
    '''
    main process
    '''
    # impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    prefix_A = [0] * (N + 1)
    prefix_C = [0] * (N + 1)
    prefix_G = [0] * (N + 1)
    for i, nucleotide in enumerate(S):
        prefix_A[i + 1] = prefix_A[i]
        prefix_C[i + 1] = prefix_C[i]
        prefix_G[i + 1] = prefix_G[i]
        
        if nucleotide == 'A':
            prefix_A[i + 1] += 1
        elif nucleotide == 'C':
            prefix_C[i + 1] += 1
        elif nucleotide == 'G':
            prefix_G[i + 1] += 1

    arrayResults = []
    for k in range(M):
        start = P[k]
        end = Q[k] + 1

        if prefix_A[end] - prefix_A[start] > 0:
            arrayResults.append(1)  # A 
        elif prefix_C[end] - prefix_C[start] > 0:
            arrayResults.append(2)  # C 
        elif prefix_G[end] - prefix_G[start] > 0:
            arrayResults.append(3)  # G 
        else:
            arrayResults.append(4)  # T 

    return arrayResults

        

test_cases = {
    # Example cases
    ("CAGCCTA", (2, 5, 0), (4, 5, 6)): [2, 4, 1],  # Standard example

    # Edge cases
    ("A", (0,), (0,)): [1],                         # Single character string
    ("T", (0,), (0,)): [4],                         # Single character, T
    ("ACGT", (0, 1, 2, 3), (0, 1, 2, 3)): [1, 2, 3, 4],  # One query per character
    ("AAAA", (0, 1, 2), (3, 3, 3)): [1, 1, 1],    # Only A's in the string

    # Large input tests
    ("C" * 100000, (0,), (99999,)): [2],            # Entire string of C's
    ("G" * 100000, (0, 50000, 99999), (99999, 99999, 99999)): [3, 3, 3],  # Large query overlap
    ("A" * 50000 + "T" * 50000, (0, 49999, 50000), (49999, 50000, 99999)): [1, 1, 4],  # Split string
}

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    for (S, P, Q), expected_output in test_cases.items():
        try:
            result = solution(S, list(P), list(Q))
            if result == expected_output:
                print(f"Test Passed: input=S({len(S)}), P={P}, Q={Q}, output={result}")
                passed += 1
            else:
                print(f"Test Failed: input=S({len(S)}), P={P}, Q={Q}, expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input=S({len(S)}), P={P}, Q={Q}, error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")


# Run the tests
run_tests()

