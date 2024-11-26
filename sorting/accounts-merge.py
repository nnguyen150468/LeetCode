class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        seen = defaultdict(lambda: [set()])
                
        for acct in accounts:
            name = acct[0]
            is_duplicate = False
            if name in seen:
                new_emails = set()
                for email_idx, emails in enumerate(seen[name]):
                    for i in range(1, len(acct)):
                        new_emails.add(acct[i])
                        if acct[i] in emails:
                            is_duplicate = True
                    if is_duplicate:
                        seen[name][email_idx].update(new_emails)                        
                        break
                if not is_duplicate:
                    seen[name].append(new_emails)
            else:
                seen[name].append(set(acct[1:]))
        res = []
        for name, email_lists in seen.items():            
            for email_list in email_lists:
                if not email_list:
                    continue
                acct = []
                for email in email_list:                    
                    acct.append(email)
                acct = [name] + sorted(acct)
                res.append(acct)
        # print(res)
        return res
