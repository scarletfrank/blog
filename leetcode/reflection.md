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

- ZigZag：通过边界条件影响上下控制，联想题目，90°矩阵（是否可以用一个4以内循环控制）。

- Reverse Integer：如果不使用转换函数行不行。（%10，与除以10的结合，用一个栈反转）

- atoi: 类似，应该使用ord来代替转换函数，ord(c) - ord('0')

- 回文数字：转换为字符串，再reverse。如果不用转换函数，可以逐步分解数字输入栈再返回来就行。

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

- Search in Rotated Sorted Array：找到有序的一边，然后二分查找。变种需要去除重复元素

- findFirstLast: 运用两次二分查找

- searchInsert: 插入排序

- isValidSudoku: 检查行列及九宫格

- solveSudoku: 回溯法

- CountAndSay: 很神秘的一题

- combinationSum: DFS？还是递归，不停搜下去直到失败。下一题的改变是重复要素只能使用一次。

### 41~50

- firstMissingPositive

将元素放入对应的位置

- trapWater

左右缩小，根据墙壁的性质增加水量

- 字符串相乘得到字符串结果: ord()函数结合offset实现乘法

- wildcard: DP方法和FSM方法

- Jump Games: 贪婪方法，不仅是变种，原本题目一也可以运用。

- permutation: 采用DFS方法，变体增加一个重复判断。变种为N个元素里取K个做排列

- 旋转矩阵: 固定知识

- groupAnagrams: 原本自己写的Counter方法，复杂度很高，后面改为了NK的复杂度。

- myPow: 递归和迭代都能实现指数，注意 &和>>的应用。

### 51~60

- n-Queens: backtrack(dfs) 

- maxSubArray: DP 方法第一次理解（可能因为例子比较简单）
- Spiral Matrix: Stimulation，生成的变种代码类似
- JumpGame:
- MergeInterval: 原本的思路是冒泡似的循环，后面发现需要先进行排序。
- InsertInterval：插入排序后沿用上一题代码
- LenghtofLastWord: python string trick
- Permutation Sequence

### 61 ~ 70

- Rotate List: 链表情况与数组类似
- Unique Paths: 参考书上的迷宫通过栈来解决，这里采用DP
- Unique Paths 2: 增加一个判断条件来更新dp
- Minimum Path Sum: 纯DP，按步骤更新
- Valid Number: 似乎没法写出正确的正则表达式，看到了一个我心中的完美答案，使用了DFA。（参考龙书）
- Plus One: 链表的加一
- Add Binary: 模拟二进制，注意ord的使用
- Text Justification
- Sqrt(x): 循环结合二分查找，找到合适的x
- Climbing Stairs： 基础DP，或者说是斐波那契数列

### 4.26

1. 模拟队列
2. 欧氏距离
3. 卡牌
4. 两个栈实现队列
5. 第k层祖先

### SQL part

事务性质ACID：

- 原子性： 有或无
- 隔离性：并发事务执行
- 持久性：改变是永久的
- 一致性

事务隔离级别：

- 读未提交
- 读提交
- 可重复读
- 可串行化

问题：
- 脏读
- 不可重复读
- 幻读

位操作：

- 626 Exchange Seats

Bit manipulation expression (id+1)^1-1 can calculate the new id after switch

- 627 Swap Salary

update salary set sex = CHAR(ASCII('f') ^ ASCII('m') ^ ASCII(sex));
The COALESCE() function returns the first non-null value in a list.

### Links

[针对开发团队的问题](https://mp.weixin.qq.com/s/aWgu0ePiYBhdiTgYjmYCGw)

-  在编码前是否解决bug
- 所有版本，都由持续集成服务器自动编译吗

## 面试

### Self Introduction



### Description of Project
- challenge
- mistake
- enjoyed
- leadership
- conflict
- what you'd do differently
*technical decision* *choice of technologies(trade off)*

### 后台开发面试

> 面试前看了一下别人的面试经历，就感觉自己啥问题都回答不出来。被拒，果然第一家就这个难度是失误啊。当初修改简历的时候变成了投递操作。

1. Linked List, Intersection

集合操作都可以看成归并排序变种，这里紧张了没看清题目，后面也没马上反应过来。

2. 27进位，效率提升使用ord('A') - offset(=64)

这里不应该用字典，既然想到效率问题应该直接用ord()

3. 二叉树上第三大的数（以及第三小的数）

找到最小的数，然后找父节点右（左）最大（小）值。
> 看了下书，最直观的方法是中序遍历得到有序序列。可以输出3或者n-3的元素？

4. 插入“,” 以及控制小于1000


### 信息技术岗面试

> 未知和信息安全岗、系统维护岗、软件开发岗的区别，虽然我在面试前才开始问这个问题。感觉要被刷。据说就是软件开发岗。

#### 1面

更注重开发，问的问题更多是经历，可能到笔试，或者没有笔试。

简历应该突出内容。

Keyword: Linux熟练度 数据库使用  C/JAVA语言开发 Python语言开发

#### 2面

感觉聊的比较开心，主要回答了HTTP发起请求到服务器的过程（ATM为例子）。之后考虑了安全性要求，其他的有点不太记得了。

#### 3面 及 终面

结束了，不是技术面...问了很多上下级关系的问题...比如否决了你的方案啥的。过了一天马上来电话说有最终的面试。问了问为啥选择以及吃不吃早餐和熬夜的问题...最后问了问意向程度。


### 应用软件设计面试


#### 1面

自我介绍后，问了实习干了啥。问了各种概念，二分排序、数据库、自己开发的项目（我介绍了Django+nginx的内容）。草，想不起来他软件工程问的一个问题了，反正我没答上来，跟他说课程上主要了解了开发模式。原来是单例模式（软件设计模式）

