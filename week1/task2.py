class Solution(object):
    def intToRoman(self, num):
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        m = thousands[num // 1000]
        c = hundreds[(num % 1000) // 100]
        x = tens[(num % 100) // 10]
        i = units[num % 10]

        roman_numeral = m + c + x + i
        return roman_numeral
