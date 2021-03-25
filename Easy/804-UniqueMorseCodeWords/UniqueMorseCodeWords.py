class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_alphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                          "-.",
                          "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        transformations = set()

        for word in words:
            morse_string = ""
            for character in word:
                morse_string += morse_alphabet[ord(character) - 97]
            transformations.add(morse_string)

        return len(transformations)


solution = Solution()
testWords = ["gin", "zen", "gig", "msg"]
print("Expecting 2\n" +
      "Returned: " + str(solution.uniqueMorseRepresentations(testWords)))
