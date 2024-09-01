def count_voowels(text):
        vowels = 'aeiou'
        return sum(1 for char in text.lower() if char in vowels)