import sys
"""
单行
for line in sys.stdin:
    a = line.split()
    print(int(a[0]) + int(a[1]))

#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)
"""
# fork from NowCoder
# HG[3|B[2|CA]]F
# HGBCACABCACABCACAF
def uncompress(s: str):
    #s = input()
    # if __name__ == "__main__":
    i = 0
    while i < len(s):
        if s[i] == ']': # backward to search first matching "["
            j, k = i, 0
            while s[j] != '[':
                if s[j] == '|':
                    k = j 
                j = j - 1
            subs = s[j:i+1]
            num = int(s[j+1:k])
            reps = s[k+1:i]
            reps = reps * num
            s = s.replace(subs, reps, 1)
            i = j
        i = i + 1
    print(s)

# Theta n^2 ，用单调栈最优
def viewBuild(height):
    n = len(height) # 
    res = []
    for i in range(n):
        cnt = 0
        # 返回结果每一个都要加上位置自身的楼栋
        if i == 0 : # edge case, -> <-
            maxRight = height[i]
            for j in range(i+1, n):
                if height[j] >= maxRight or j == i + 1:
                    cnt += 1
                    maxRight = height[j] # update Right Wall
        elif i == n - 1:
            maxLeft = height[i]
            for j in range(i-1, -1, -1):
                if height[j] >=  maxLeft or j == i - 1:
                    cnt += 1
                    maxLeft = height[j]
        else:
            maxRight = maxLeft = height[i]
            for j in range(i+1, n):
                if height[j] >= maxRight or j == i + 1:
                    cnt += 1
                    maxRight = height[j] # update Right Wall
            for j in range(i-1, -1, -1):
                if height[j] >=  maxLeft or j == i - 1:
                    cnt += 1
                    maxLeft = height[j]
            # two pass, <- ->
        cnt = cnt + 1
        res.append(str(cnt))
    return res

def viewBuildStack(heights):
    n = len(heights) # 
    res, stack = [0] * n, []
    for i in range(n):
        res[i] = len(stack)
        if i == 0:
            stack.append(heights[i]) # 1st
        elif stack[-1] > heights[i]:
            stack.append(heights[i]) # 
        else:
            while stack and stack[-1] < heights[i]:
                stack.pop()
            stack.append(heights[i])
    return res
        
if __name__ == "__main__":
    num = sys.stdin.readline().strip()
    l = []
    try:
        while True:
            line = sys.stdin.readline().strip()
            if line == "":
                break
            lines = line.split()
            l = [int(e) for e in lines]
    except:
        pass
    n = int(num)
    heights = l
    #print(n, heights)
    rA = viewBuildStack(heights)
    rB = viewBuildStack(heights[::-1])[::-1]
    r = [rA[i] + rB[i] + 1 for i in range(n)]
    r = [str(e) for e in r]
    print(" ".join(r))

"""
10
73289 45963 22522 44454 58143 31977 59209 85753 45063 9507
5 7 7 7 7 5 5 4 3 3
"""
