from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = dict()
        for cpdomain in cpdomains:
            cnt, domains = cpdomain.split(" ")
            cnt = int(cnt)
            for i in range(domains.count(".") + 1):
                domain = '.'.join(domains.split('.')[i:])
                d[domain] = d.get(domain, 0) + cnt

        return [f"{cnt} {domain}" for domain, cnt in d.items()]


s = Solution()
assert s.subdomainVisits(["9001 discuss.leetcode.com"]) == ["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
