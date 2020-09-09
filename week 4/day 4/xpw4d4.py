#1
# def display_message():
#     print("I'm learning python")
# display_message()

#2
# def favourite_book(title):
#     print(f"My favourite books is {title}")

# favourite_book("Harry Potter")

# #3 help

# def make_shirt(text="I love python",size="large"):
#     print(f"Your shirt will say {text} and be size {size} ")
# make_shirt(input("text"), input("size"))    


# #4
# m_names = ["Harry", "Ron", "Hermione", "Dumbledore"]
# def show_magicians(names):
#     print(names)
# show_magicians(m_names)

# def make_great(name):
#     return (f"The Great {name}")
    
# m_names = [item for item in map(make_great, m_names)]
        
# show_magicians(m_names)

#5
# def discribe_city(city="none",country="nonewhereville"):
#     print(f"This {city} is in {country}")
# discribe_city("Toronto", "Canada")
# discribe_city("Miami", "Florida")
# discribe_city()

#6
# from datetime import date
# def get_age(year, month, day):
#     today = date.today()
#     return today.year - year - ((today.month, today.day) < (month, day))


# def can_retire(gender, date_of_birth):
#     bday = date_of_birth.split('/')
#     year = int(bday[0])
#     month = int(bday[1])
#     day = int(bday[2])
#     age = get_age(year, month, day)
#     gender = gender.lower()
#     if gender == "female":
#         if age > 61:
#             print("You may retire")
#         else:
#             print("You man not retire")
#     elif gender == "male":
#         if age > 66:
#             print("You may retire")
#         else:
#             print("You man not retire")

# gender = input("Are you male of female?")
# bdate = input('enter your bday ex: year/month/day')
# can_retire(gender, bdate)

#7
from faker import Faker 

users = []

def add_users(**kwargs):
    user2 = users.append(kwargs)
    return user2
    
for i in range(10):
    fake = Faker()
    kwargs = {'name': fake.name(), 'address': fake.address(), 'langage':fake.language_name()}
    all_users = add_users(kwargs)

print(all_users)

