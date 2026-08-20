class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            # Add number of letters and # before the letters
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []

        i = 0
        while i < len(s):
            # j should start from i
            j = i

            # Reach index of #
            while s[j] != "#":
                j += 1

            lenth = int(s[i:j])
            next_i = j + 1 + lenth # Next index of the staring of the lengh value

            result.append(s[j+1 : next_i])
            i = next_i

        return result