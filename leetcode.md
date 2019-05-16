[TOC]

##### 7.[整数反转](https://leetcode-cn.com/problems/reverse-integer/)

题目：给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

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