def main():
    animals=["rat","ox","tiger","rabbit","dragon","snake","horse","goat","monkey","rooster","dog","pig"]
    months=["","jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
    birth_date=input("Enter your birthdate(limit years from 1994-2020)(ie: xx/xx/xxxx):")
    birth_month= months[int(birth_date.split("/")[0])]
    birth_day = birth_date.split("/")[1]
    birth_year=int(birth_date.split("/")[2])%12-4
    print("your birthday is",birth_month,birth_day,birth_date.split("/")[2],",","You were born on the year of the",animals[birth_year])
main()
