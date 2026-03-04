class India():
    def capital(Self):
        print("New Delhi is the capital of India")
    def Language(Self):
        print("Hindi is the most widely spoken language of India")
    def type(Self):
        print("India is a developing country")
class USA():
    def capital(Self):
        print("Washington D.C. is the capital of The United States")
    def Language(Self):
        print("English is the primary lnguage of The United States")
    def type(Self):
        print("U.S.A is a developing country")
obj_ind=India()
obj_usa=USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.Language()
    country.type()
        

