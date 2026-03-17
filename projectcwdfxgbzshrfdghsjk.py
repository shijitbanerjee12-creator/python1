class IntegerToRoman:
    
    def __init__(self, number):
        if not 1 <= number <= 3999:
            raise ValueError("Number must be between 1 and 3999")
        self.number = number
        self.roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ] #

    def convert(self):
        
        num_to_convert = self.number
        result = []
        for value, numeral in self.roman_map:
           
            factor, num_to_convert = divmod(num_to_convert, value)
            result.append(numeral * factor)
            if num_to_convert == 0:
                break
        return "".join(result)

number_instance = IntegerToRoman(1994)

roman_numeral = number_instance.convert()
print(f"The Roman numeral for 1994 is: {roman_numeral}")

number_instance_2 = IntegerToRoman(3549)
roman_numeral_2 = number_instance_2.convert()
print(f"The Roman numeral for 3549 is: {roman_numeral_2}") 
