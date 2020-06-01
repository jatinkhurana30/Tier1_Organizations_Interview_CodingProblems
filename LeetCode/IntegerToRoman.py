def intToRoman(num: int) -> str:
    roman = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    n = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ans = ''
    while num:
        i = 0
        while i < len(n) - 1 and num < n[i]:
            i += 1
        num = num - n[i]
        ans += roman[i]

    return ans


print(intToRoman(60))