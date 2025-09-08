# Write your solution here
def new_person(name: str, age: int) -> tuple[str, int]:
    name_invalid = len(name) <= 0 or len(name) > 40 or len(name.split()) < 2
    age_invalid = age < 0 or age > 150
    if name_invalid or age_invalid:
        print(name, age)
        error_message = f'Invalid input: "{name + ' ' + age if name_invalid and age_invalid else name if name_invalid else age}"'
        raise ValueError(error_message)
    return (name, age)
