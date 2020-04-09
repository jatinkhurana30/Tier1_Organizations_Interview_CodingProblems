"""

Sample Input:
George Sammy Jack Missie Fred Dustin Anil



Assign secret santas to each other
There are 3 conditions
1) Person1 can't be secret santa of himsef
2) If Person1 is secret Santa of Person2, Person2 can't be secret Santa of Person1
3) The result should be dynamic each time

"""
import random

people_list = input().split(' ')
assigned_secret_santa = []


def assign_secret_santa(person_name, people_left):
    if len(people_left) == 0:
        return None

    random_person = random.choice(people_left)
    assigned_secret_santa.append({'personName': person_name, 'secretSanta': random_person})
    people_left.remove(random_person)
    assign_secret_santa(random_person, people_left)


name = people_list.pop(0)
assign_secret_santa(name, people_list)
last_entry = {'personName': assigned_secret_santa[0]["personName"],
              'secretSanta': assigned_secret_santa[-1]["personName"]}
assigned_secret_santa.append(last_entry)

for person in assigned_secret_santa:
    print(f'{person["secretSanta"]} is Secret Santa of {person["personName"]}', end='\n')
