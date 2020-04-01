from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = dict()
        for cpdomain in cpdomains:
            tokens = cpdomain.split(' ')
            count = int(tokens[0])
            domain = tokens[1]
            domain_tokens = domain.split('.')
            sub_domain = ''
            token_count = len(domain_tokens)
            for i in range(0, token_count):
                sub_domain = domain_tokens[token_count-1-i] + ('' if i ==0 else '.' + sub_domain)

                if sub_domain in visits:
                    visits[sub_domain] += count
                else:
                    visits[sub_domain] = count

        result = []
        for visit in visits:
            result.append(str(visits[visit]) + ' ' + visit)

        return result

print(Solution().subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
