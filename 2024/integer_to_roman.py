def intToRoman(num: int) -> str:
        d = {1000:"M", 900:"CM",
            500:"D", 400:"CD",  
            100:"C", 90:"XC",
            50:"L", 40:"XL",
            10:"X", 9:"IX",
            5:"V", 4:"IV",
            1:"I"
        }

        res = ''

        for k,v in d.items():
            while k <= num:
                res += v
                num-= k
        return res

print('-'*20) 
print(intToRoman(3))
print('-'*20)
print(intToRoman(58))
print('-'*20)
print(intToRoman(1994))
print('-'*20)