'''
Find the largest palindrome in a given string.
'''
def is_palindrome(s):
	return s[:]==s[::-1]

def largest_palindrome(s,j,i=0):

	if is_palindrome(s[i:j]):
		return s[i:j]
	else:
		return max(largest_palindrome(s,j-1,i),largest_palindrome(s,j,i+1),key=len)


s = "aabba"
s = "aabbaaa"

print(largest_palindrome(s,len(s)))