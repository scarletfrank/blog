## LeetCode

### 1~10

- Two Sum: 哈希表实现 Theta(1)的查询效率

- Add Two Numbers: 链表数字相加

DummyHead的使用，carry部分采用整除//，剩余的数位采用取模mod(%)

- Longest Substring: 维护两个指针，保证之间的字符串没有重复的字母

可以用集合或者哈希表查看是否找到过该字符

- Median of 2 sorted arys: 二分查找

关键是分析出两个数组时，应该满足的条件，二分查找根据是过大或者过小来调整，直到最佳。

- Lonngest Palindromic Substring

从一个字母开始左右拓展。这种解法仿佛是洞悉了问题，Trap Water也有这个特点。

- ZigZag：通过边界条件影响上下控制

- Reverse Integer：如果不使用转换函数行不行。

- atoi

- 回文数字：转换为字符串，再reverse

- 正则表达式判断：

关联：wildcard 判断

### 11~20

- Container With Most Water: 两个指针的方法

- 罗马数字转换：把各种组合列出来，然后循环检查

- LCP: 逐渐缩短，直到全部匹配

- 3Sum：排序，确定一个数，之后再这个数后的区间左右缩小搜索

- 3SumCloses: 类似，但主要是判断距离差距之后更新

- 括号匹配：利用栈

### 21~30



- 合并两个链表

- 生成有效括号: 利用回溯法，每次添加正确的括号
    复杂度分析比较神秘
- 合并k个链表: 利用Wrapper结合优先队列解决

- SwapNodeinPairs: 链表，画图处理

- reverseKGroup: ...

- removeDuplicates: 把不重复的数字i，放到对应的位置i

- removeElement: 把给定数字以外的数字放到数组前面（移除target），跟上一题类似，不是目标就放入前位

- strStr()：KMP方法

- DivideTwoIntegers: 数学

- Substring with Concatenation of All Words

引入了一个Counter来统计单词出现的频率，然后记录单词的长度，遍历一下，比对串的统计和目标的频率



### 31~40

- Next Permutation

- findFirstLast: 运用两次二分查找

- searchInsert: 插入排序

- isValidSudoku: 检查行列及九宫格

- solveSudoku: 回溯法

- CountAndSay: 很神秘的一题

- combinationSum: DFS？还是递归，不停搜下去直到失败
下一题的改变是重复要素只能使用一次。

### 41~50

- firstMissingPositive

将元素放入对应的位置

- trapWater

左右缩小，根据墙壁的性质增加水量

- 字符串相乘得到字符串结果: ord()函数结合offset实现乘法

- wildcard: DP方法和FSM方法

- Jump Games: 贪婪方法，不仅是变种，原本题目一也可以运用。

- permutation: 采用DFS方法，变体增加一个重复判断

- 旋转矩阵: 固定知识

- groupAnagrams: 原本自己写的Counter方法，复杂度很高，后面改为了NK的复杂度。

- myPow: 递归和迭代都能实现指数，注意 &和>>的应用。

### SQL part





### Links

[针对开发团队的问题](https://mp.weixin.qq.com/s/aWgu0ePiYBhdiTgYjmYCGw)

-  在编码前是否解决bug
- 所有版本，都由持续集成服务器自动编译吗

## 面试

### 后台开发面试

> 面试前看了一下别人的面试经历，就感觉自己啥问题都回答不出来。被拒，果然第一家就这个难度是失误啊。当初修改简历的时候变成了投递操作。

1. Linked List, Intersection

集合操作都可以看成归并排序变种，这里紧张了没看清题目，后面也没马上反应过来。

2. 27进位，效率提升使用ord('A') - offset(=64)

这里不应该用字典，既然想到效率问题应该直接用ord()

3. 二叉树上第三大的数（以及第三小的数）

找到最小的数，然后找父节点右（左）最大（小）值

4. 插入“,” 以及控制小于1000


### 信息技术岗面试

> 未知和信息安全岗、系统维护岗、软件开发岗的区别，虽然我在面试前才开始问这个问题。感觉要被刷（x

更注重开发，问的问题更多是经历，可能到笔试，或者没有笔试。

简历应该突出内容。

Keyword: Linux熟练度 数据库使用  C/JAVA语言开发 Python语言开发



