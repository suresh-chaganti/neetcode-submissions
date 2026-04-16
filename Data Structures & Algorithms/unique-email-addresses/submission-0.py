class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        email_set = set()
        for email in emails:
            tokens = email.split('@')
            local_nm = tokens[0]
            domain = tokens[1]
            local_na = local_nm.split('+')[0].replace('.','')
            email_set.add(local_na+'@'+domain)
        
        return len(email_set)
        