def calculate_birth_year(age):
    birth_year = 2022 - age
    return birth_year


age = int(input("How old are you (in years)? "))
birth_year = calculate_birth_year(age)

print(f"You were born in (roughly) {birth_year}.")
