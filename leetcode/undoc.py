
# fork from NowCoder
# HG[3|B[2|CA]]F
# HGBCACABCACABCACAF
def uncompress(s: str):
    #s = input()
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