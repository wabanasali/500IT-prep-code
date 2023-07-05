def palindrome(s1,s2):
    s3 = s2[::-1]
    if s1 == s3:
        return True
    else:
        return False
    
palindrome('sas','sas')