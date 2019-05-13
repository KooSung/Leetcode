class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_s = s[0]
        for core in range(len(s) - 1):
            if s[core - 1] == s[core + 1] and core >= 1:
                r_range = min(core, len(s) - core - 1)
                for r1 in range(r_range + 1):
                    if s[core - r1] == s[core + r1]:
                        if 2 * r1 + 1 > len(max_s):
                            max_s = s[core - r1:core + r1 + 1]
                    else:
                        break

            if s[core] == s[core + 1]:
                r_range = min(core, len(s) - core - 2)
                for r2 in range(r_range + 1):
                    if s[core - r2] == s[core + r2 + 1]:
                        if 2 * r2 + 2 > len(max_s):
                            max_s = s[core - r2:core + r2 + 2]
                    else:
                        break
        return max_s              
