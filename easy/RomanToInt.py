#class Solution:
#    def romanToInt(self, s: str) -> int:

class Solution:
    def romanToInt(self, roman: str):
        all_roman = [(1000, 'M'), 
                     (900, 'CM'), 
                     (500, 'D'), 
                     (400, 'CD'), 
                     (100, 'C'), 
                     (90, 'XC'), 
                     (50, 'L'), 
                     (40, 'XL'), 
                     (10, 'X'), 
                     (9, 'IX'), 
                     (5, 'V'), 
                     (4, 'IV'), 
                     (1, 'I')]

        # на старте десятичное число равно нулю
        dec = 0
        # перебираем все пары из словаря
        for i, r in all_roman:
            # пока римское число начинается буквы из словаря
            while roman.startswith(r):
                # увеличиваем десятичное число на соответствующее значение из словаря
                dec += i
                # убираем найденную букву из римского числа
                roman = roman[len(r):]
        # как все циклы закончились — возвращаем десятичное число
        return dec    


a=Solution()

print(a.romanToInt('IX')) 
