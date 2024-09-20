import datetime

birth = datetime.datetime.strptime(input("Your birth date (DD/MM/YYYY): "), "%d.%m.%Y") #dogum tarihi
age = datetime.datetime.now() - birth #yas hesaplamasi

print(f"You survived {age.total_seconds()} seconds") #yasini saniyeye donustur ve yazdir  
