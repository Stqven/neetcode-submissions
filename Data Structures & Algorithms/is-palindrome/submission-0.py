class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_word = ""
        for i in s:
            if i.isalnum():
                new_word += i.lower()
        l,r = 0, len(new_word) - 1
        while l < r:
            if(new_word[l] == new_word[r]):
                l += 1
                r -= 1
            else:
                return False
        
        return True
