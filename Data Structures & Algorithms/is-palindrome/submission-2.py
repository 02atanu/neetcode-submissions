class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create a string with only numerics and lower letters
        all_chars = ""
        for c in s:
            if c.isalnum():
                all_chars += c.lower()

        if len(all_chars) in {0, 1}:
            return True

        for i in range(len(all_chars)):
            if all_chars[i] != all_chars[-i-1]:
                return False
            # Break the loop for odd and even index
            if i == (len(all_chars)//2) - 1:
                return True
                break


        