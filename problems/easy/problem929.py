from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            local_name, domain = email.split("@")
            local_name = local_name.replace('.', '').split('+')[0]
            ans.add((local_name, domain))
        return len(ans)


s = Solution()
assert s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]) == 2
