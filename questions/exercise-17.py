original_ages = [36, 31, 42, 3]
new_ages = []

for original_age in original_ages:
    new_age = original_age + 7
    new_ages.append(new_age)


print("Here are the original ages of all of the people in my household:")
for original_age in original_ages:
    print(original_age)



print("Here are the ages of all of the people in my household increased by 7 years:")
for new_age in new_ages:
    print(new_age)
