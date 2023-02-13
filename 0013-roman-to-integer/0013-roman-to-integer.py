class Solution:
    def romanToInt(self, s: str) -> int:
        
        roman_int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        
        num = 0
        skip_next = False
        for idx, char in enumerate(s):
            if skip_next:
                skip_next = False
                continue
                
            if idx+1<len(s):
                next_char = s[idx+1]
                double_char = char+next_char
                if double_char in roman_int_map:
                    num += roman_int_map[double_char]
                    skip_next = True
                else:
                    num += roman_int_map[char]
            else:
                num += roman_int_map[char]
            
            
        return num
        