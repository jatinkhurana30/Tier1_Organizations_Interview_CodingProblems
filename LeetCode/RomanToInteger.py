roman_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def romanToInt(s: str) -> int:
    number = 0
    i = 0
    while i < len(s):
        if s[i] == 'I':
            if i+1 < len(s):
                if s[i + 1] == 'V':
                    i += 2
                    number = number + 4
                    continue
                elif s[i + 1] == 'X':
                    i += 2
                    number = number + 9
                    continue
        elif s[i] == 'X':
            if i + 1 < len(s):
                if s[i + 1] == 'L':
                    i += 2
                    number = number + 40
                    continue
                elif s[i + 1] == 'C':
                    i += 2
                    number = number + 90
                    continue
        elif s[i] == 'C':
            if i + 1 < len(s):
                if s[i + 1] == 'D':
                    i += 2
                    number = number + 400
                    continue
                elif s[i + 1] == 'M':
                    i += 2
                    number = number + 900
                    continue

        number = number + roman_map[s[i]]
        i += 1

    return number


print(romanToInt('MCMXCIV'))