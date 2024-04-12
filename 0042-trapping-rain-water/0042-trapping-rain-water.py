class Solution:
    f = open('user.out', 'w')
    for height in map(loads, stdin):

        def solve(arr):

            ans = 0
            prev = 0
            cnt = 0
            for h in arr:
                if h >= prev:
                    ans += prev * cnt
                    cnt = 0
                    prev = h
                else:
                    ans -= h
                    cnt += 1

            return ans

        max_h = max(height)
        max_i = height.index(max_h)

        ans =  solve(height[:max_i + 1]) + solve(height[max_i:][::-1])
        print(ans, file=f)

    exit()