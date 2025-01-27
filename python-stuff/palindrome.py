def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while(left < right):
        if s[left] != s[right]:
            return "Not a palindrome"
        left += 1
        right -= 1
    return "Palindrome"

print(isPalindrome("racecasr"))