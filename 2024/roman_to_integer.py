def romanToInt(s: str) -> int:
        num = 0
        d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in range(len(s)):
            if i == len(s)-1:
                num += d.get(s[i])
            elif d.get(s[i]) < d.get(s[i+1]):
                num -= d.get(s[i])
            else:
                num += d.get(s[i])
        return num

print('-'*20)
print(romanToInt('III')) 
print('-'*20)
print(romanToInt('LVIII'))
print('-'*20)
print(romanToInt('MCMXCIV'))
print('-'*20)