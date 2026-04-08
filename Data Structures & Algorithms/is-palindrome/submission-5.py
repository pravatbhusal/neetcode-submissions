class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.efficient(s)

    # two pointers, solves this in O(N) time with O(1) space
    # one pointer in the front, one pointer in the tail
    def efficient(self, s):
        front_p = 0
        end_p = len(s) - 1
        while front_p < end_p:
            front_c = s[front_p]
            end_c = s[end_p]
            if front_c.isalnum() and end_c.isalnum():
                # compare
                if (front_c.lower() != end_c.lower()):
                    return False
                front_p += 1
                end_p -= 1
            # skip non-alphanum
            if not front_c.isalnum():
                front_p += 1
            if not end_c.isalnum():
                end_p -= 1
        return True

    # reverse the string, remove non-alphanum, lowercase, then check equals
    # O(S) time and space
    def naive(self, s):
        r_s = "".join(reversed(s))
        print(self.getalphanum(s), self.getalphanum(r_s))
        return self.getalphanum(s) == self.getalphanum(r_s)

    # O(S) time and space
    def getalphanum(self, s):
        return "".join([char.lower() for char in s if char.isalnum()])