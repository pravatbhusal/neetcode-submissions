class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.naive(s)

    # reverse the string, remove non-alphanum, lowercase, then check equals
    def naive(self, s):
        r_s = "".join(reversed(s))
        print(self.getalphanum(s), self.getalphanum(r_s))
        return self.getalphanum(s) == self.getalphanum(r_s)

    def getalphanum(self, s):
        return "".join([char.lower() for char in s if char.isalnum()])