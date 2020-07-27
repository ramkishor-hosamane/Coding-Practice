'''
Find the largest palindrome in a given string.
'''
def is_palindrome(s):
	return s[:]==s[::-1]


def larget_palindrome(s):
        res=""
        for word in s:
                if is_palindrome(word):
                      res=max(res,word,key=len)

        if res="":
                print("There are no palindromes")
        else:
                print(res,"is the largest palindrome")
        
s = "aabba"
s = "saas mmaa iti Malayalam "

print(largest_palindrome(s,len(s)))
