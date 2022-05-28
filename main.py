# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    word1 = sorted(word)
    word2 = sorted(anagram)
   
    if word1 == word2 :
        return True 
    else:
        return False

print(find_anagram("loop", "polo"))
print(find_anagram("plate", "late"))
print(find_anagram("night", "thing"))
print(find_anagram("gentle", "elegant"))