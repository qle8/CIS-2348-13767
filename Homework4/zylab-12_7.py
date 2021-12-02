# Name: Quang Le
# Student ID: 1768324


def get_age():
    age = int(input())
    # TODO: Raise excpetion for invalid ages
    if age <18 or age >35:
        raise ValueError('Invalid age.')
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = 0.7*(220-age)
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        heart_rate = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age, heart_rate))
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.\n')
