# English ver.
'''
A string S with N characters is considered properly nested if:
	•	S is empty;
	•	S has the structure “(U)”, where U is a properly nested string;
	•	S has the structure “VW”, where V and W are properly nested strings.

For example:
	•	The string “(()(())())” is properly nested.
	•	The string “())” is not properly nested.

Write a function:
def solution(S)
This function, given a string S of N characters, returns 1 if S is properly nested, and 0 otherwise.

For example:
	•	Given S = "(()(())())", the function should return 1.
	•	Given S = "())", the function should return 0.

Constraints:
	•	N is an integer in the range [0..1,000,000].
	•	The string S consists only of the characters '(' and ')'.
'''



# Japnese ver.
'''
文字列 S は、次の場合に適切にネストされているとみなされます：
	•	S が空である場合。
	•	S が “(U)” の形式であり、U が適切にネストされた文字列である場合。
	•	S が “VW” の形式であり、V と W が適切にネストされた文字列である場合。

例えば：
	•	文字列 “(()(())())” は適切にネストされています。
	•	文字列 “())” は適切にネストされていません。

以下の関数を作成してください：
def solution(S)
この関数は、長さ N の文字列 S を受け取り、S が適切にネストされている場合は 1 を、そうでない場合は 0 を返します。

例えば：
	•	S = "(()(())())" の場合、関数は 1 を返します。
	•	S = "())" の場合、関数は 0 を返します。

制約：
	•	N は [0..1,000,000] の範囲内の整数。
	•	文字列 S は '(' および ')' のみで構成されます。
'''


# Chinese ver.
'''
一個字串 S，如果符合以下條件，就被認為是適當嵌套的：
	•	當 S 是空的；
	•	當 S 的結構是 “(U)”，且 U 是一個適當嵌套的字串；
	•	當 S 的結構是 “VW”，且 V 和 W 都是適當嵌套的字串。

例如：
	•	字串 “(()(())())” 是適當嵌套的。
	•	字串 “())” 則不是適當嵌套的。

請撰寫以下函數：
def solution(S)
該函數接收長度為 N 的字串 S，如果 S 是適當嵌套的，則返回 1；否則返回 0。

例如：
	•	當 S = "(()(())())" 時，函數應返回 1。
	•	當 S = "())" 時，函數應返回 0。

限制條件：
	•	N 是 [0..1,000,000] 範圍內的整數。
	•	字串 S 僅由字符 '(' 和 ')' 組成。
'''



def solution(S):
    # Implement your solution here
    '''
    checker:    input range, empty
    '''
    if not S:
        return 1
    N = len(S)
    if N == 0: return 1
    '''
    main process
    '''
    char_open = '('
    char_close = ')'
    opens = []

    for char in S:
        if char == char_open:
            opens.append(1)
        if char == char_close:
            if len(opens) > 0:
                opens.pop(-1)
            else: return 0
    if len(opens) == 0: return 1
    else: return 0

def run_tests():
    print("Running tests...\n")
    passed = 0
    failed = 0

    test_cases = {
        "": 1,  # Empty string
        "()": 1,  # Single valid pair
        "(": 0,  # Single opening bracket
        ")": 0,  # Single closing bracket
        "(())": 1,  # Nested valid structure
        "()()": 1,  # Multiple valid pairs
        "(()))": 0,  # Extra closing bracket
        "((())": 0,  # Extra opening bracket
        "(()(()))": 1,  # Complex nested structure
        "(()(()))(()(()))": 1,  # Multiple complex valid structures
        "((((((((((((((((()))))))))))))))))": 1,  # Deep nested structure
        "()(" * 10000 + ")" * 10000: 1,  # Imbalanced structure
        "(" * 100000 + ")" * 100000: 1,  # Large valid structure
        "(" * 100001 + ")" * 100000: 0,  # Large invalid structure
    }

    for input_string, expected_output in test_cases.items():
        try:
            result = solution(input_string)
            if result == expected_output:
                print(f"Test Passed: input={repr(input_string[:30])}..., output={result}")
                passed += 1
            else:
                print(f"Test Failed: input={repr(input_string[:30])}..., expected={expected_output}, got={result}")
                failed += 1
        except Exception as e:
            print(f"Test Error: input={repr(input_string[:30])}..., error={str(e)}")
            failed += 1

    print("\nTest Summary:")
    print(f"  Passed: {passed}")
    print(f"  Failed: {failed}")
    print(f"  Total:  {len(test_cases)}")


run_tests()
