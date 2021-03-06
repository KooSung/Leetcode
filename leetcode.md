[TOC]

##### 7.[整数反转](https://leetcode-cn.com/problems/reverse-integer/)

**题目：**

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

**示例1：**

```
输入: 123
输出: 321
```

**示例2：**

```
输入: -123
输出: -321
```

**示例3：**

```
输入: 120
输出: 21
```

**注意：**

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为$[-2^{31}, 2^{31}-1]$。请根据这个假设，如果反转后整数溢出那么就返回 0。

**解答：**

```python
class Solution:
    def reverse(self, x):
        flag = x // max(1, abs(x))
        r = flag * int(str(abs(x))[::-1])
        return r if r.bit_length() < 32 or r == -2**31 else 0
```

注释：

- flag是整数的符号位，x//abs(x)可以获得其符号位，但当x为0时，不能作为除数， 故取max(1, abs(x))
- str(abs(x)是将整数转化为字符串，方便切片
- [::-1]——反向切片
- r.bit_length()——返回二进制的位数

##### [8. 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi/)

**题目：**

请你来实现一个 `atoi` 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

**说明：**

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为$[-2^{31}, 2^{31}-1]$。如果数值超过这个范围，请返回  INT_MAX ($$2^{31}-1$$] 或 INT_MIN ($-2^{31}$) 。

**示例 1:**

```
输入: "42"
输出: 42
```

**示例 2:**

```
输入: "   -42"
输出: -42
```

解释: 第一个非空白字符为 '-', 它是一个负号。我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

**示例 3:**

```
输入: "4193 with words"
输出: 4193
```


解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

**示例 4:**

```
输入: "words and 987"
输出: 0
```


解释: 第一个非空字符是 'w', 但它不是数字或正、负号。因此无法执行有效的转换。

**示例 5:**

```
输入: "-91283472332"
输出: -2147483648
```

解释: 数字 "-91283472332" 超过 32 位有符号整数范围。因此返回 INT_MIN。

```python
class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip() #删除左边空格
        result = []
        if len(str) == 0:  #若字符串为空，返回0
            return 0
        else:   #字符串不为空
            if str[0].isdigit() == True or str[0]=='-' or str[0]=='+': 
                #字符串首位是数字或者是+或-
                result.append(str[0])
                for i in str[1:]:
                    if i.isdigit():#遇到数字，添加
                        result.append(i)
                    else:#遇到非数字，中断
                        break
                if (str[0]=='-' or str[0]=='+') and len(result) < 2:#结果只有一个符号位
                    return 0
                else:
                    result = int(''.join(result))
                    if result < -2**31:
                        return -2**31
                    elif result > 2**31 -1:
                        return 2**31 - 1
                    else:
                        return result
            else: #第一个非空字符不是一个有效整数字符
                return 0 
```

解题思路：

- 首先删除字符串左边所有空格，生成新的字符串
- 判断新字符串是否为空，为空返回0
- 判断字符串首位是否为数字或者“+”或者“-”，是的话有效，不是的话返回0



##### 9.回文数

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
```

##### 15.三数之和

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[]
        i = 0
        for i in range(len(nums)):
            if i == 0 or nums[i]>nums[i-1]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    s = nums[i] + nums[l] +nums[r]
                    if s ==0:
                        res.append([nums[i],nums[l],nums[r]])
                        l +=1
                        r -=1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s>0:
                        r -=1
                    else :
                        l +=1
        return res
```

​        

##### 13. [罗马数字转整数](https://leetcode-cn.com/problems/roman-to-integer/)

罗马数字包含以下七种字符: `I`， `V`， `X`， `L`，`C`，`D` 和 `M`。

```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

  

例如， 罗马数字 2 写做 `II` ，即为两个并列的 1。12 写做 `XII` ，即为 `X` + `II` 。 27 写做  `XXVII`, 即为 `XX` + `V` + `II` 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 `IIII`，而是 `IV`。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 `IX`。这个特殊的规则只适用于以下六种情况：

- `I` 可以放在 `V` (5) 和 `X` (10) 的左边，来表示 4 和 9。
- `X` 可以放在 `L` (50) 和 `C` (100) 的左边，来表示 40 和 90。 
- `C` 可以放在 `D` (500) 和 `M` (1000) 的左边，来表示 400 和 900。

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        for i, char in enumerate(s[:-1]):
            if romanDict[char] >= romanDict[s[i+1]]:
                ans = ans + romanDict[char]
            else:
                ans = ans - romanDict[char]
        ans = ans + romanDict[s[-1]]
        return ans
```

