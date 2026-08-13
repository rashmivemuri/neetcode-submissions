class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        t = "".join(char for char in s if char.isalnum() or   char.isspace())
        text = t.replace(" ", "")
        if text.lower()==text[::-1].lower():
            return True 
        return False
        