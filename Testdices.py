import io
import sys

test_input = '''5
2 2 1
2 4 2
4 9 5
5 17 11
3 15 10
4 4 3
5 20 15
'''

sys.stdin = io.StringIO(test_input)

t = int(input())
for _ in range(t):
    n, s, r = map(int, input().split())
    max_die = s - r
    result = [max_die]
    n_minus_1 = n - 1
    base_value = r // n_minus_1
    remainder = r % n_minus_1   
    for i in range(n_minus_1):
        if i < remainder:
            result.append(base_value + 1)
        else:
            result.append(base_value)
    print(*result)
