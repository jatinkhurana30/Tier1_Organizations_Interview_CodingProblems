"""
Question:

We are given 2 calendar's of 2 person's each
Line 1: Calendar of person 1 which contains the time slots in which he has a meeting
Line 2: Person 1's available office timings
Line 3: Calendar of person 2 which contains the time slots in which he has a meeting
Line 4: Person 2's available office timings
Line 5: New meeting to be scheduled for this minutes

Expected: We need to find all the available time slots from both the person's calendar where a meeting can be held,
basically which are the time slots in which both of them are free


INPUT:
9:00,10:30 12:00,13:00 16:00,18:00
9:20,20:00
10:00,11:30 13:30,14:30 14:30,15:00 16:00,17:00
10:00,18:00
30

"""
import datetime

# Taking Input
calendar_1 = input().split(' ')
person_1 = input()
calendar_2 = input().split(' ')
person_2 = input()
meeting_time = int(input())

person1_meeting_slots = []
person2_meeting_slots = []


# A function which will convert given times into a time object
def convert_into_time(time):
    return datetime.datetime.strptime(time, '%H:%M')


# Will store the calendar schedule into each person's meeting slots, whee time will be stored as time object
for time_slot in calendar_1:
    time_slot = list(map(convert_into_time, time_slot.split(',')))
    person1_meeting_slots.append(time_slot)

for time_slot in calendar_2:
    time_slot = list(map(convert_into_time, time_slot.split(',')))
    person2_meeting_slots.append(time_slot)

"""
Here from both people's calendar, we find the already booked slots where meeting can't happen. i.e if person 1 is 
busy from 12:00 - 13:00 and person 2 is busy from 12:30 to 13:30, then total time booked for that slot is 12:00 
-13:30. SO if there are intersecting time slots in the given calendars, they will be merged, if no then they will be
taken as it is ,Provided we are also maintaining the sorted time
"""
booked_time_slots = []
start_time = None
end_time = None
p1 = p2 = 0
while p1 != len(person1_meeting_slots):
    p2 = 0
    while p2 <= len(person2_meeting_slots) - 1:
        flag = 1
        if (person2_meeting_slots[p2][0] <= person1_meeting_slots[p1][0] <= person2_meeting_slots[p2][1]) or (
                person2_meeting_slots[p2][0] <= person1_meeting_slots[p1][1] <= person2_meeting_slots[p2][1]):
            if person1_meeting_slots[p1][0] >= person2_meeting_slots[p2][0]:
                start_time = person2_meeting_slots[p2][0]
            else:
                start_time = person1_meeting_slots[p1][0]

            if person1_meeting_slots[p1][1] >= person2_meeting_slots[p2][1]:
                end_time = person1_meeting_slots[p1][1]
            else:
                end_time = person2_meeting_slots[p2][1]
            booked_time_slots.append([start_time, end_time])
            flag = 0
            person2_meeting_slots.pop(p2)
            break
        else:
            p2 += 1

    if flag == 1: booked_time_slots.append(person1_meeting_slots[p1])

    person1_meeting_slots.pop(p1)

# Remaining time slots of person 2's calendar are inserted and order is maintained
if person2_meeting_slots:
    i = 0
    while i <= len(booked_time_slots):
        if booked_time_slots[i][0] > person2_meeting_slots[0][0]:
            for item in reversed(person2_meeting_slots):
                booked_time_slots.insert(i, item)
            break
        else:
            i += 1

# Now we start finding the time slots where meeting can happen Here first we find which is the overall upper cap of
# time period available for meetings, then we find chunks of time slots left
person_1 = list(map(convert_into_time, person_1.split(',')))
person_2 = list(map(convert_into_time, person_2.split(',')))

available_time = []
if person_1[0] >= person_2[0]:
    available_time.append(person_1[0])
else:
    available_time.append(person_2[0])

if person_1[1] <= person_2[1]:
    available_time.append(person_1[1])
else:
    available_time.append(person_2[1])

counter = 0
meeting_time_slots = []

"""
Finally free meeting time slots are calculated
"""
while counter <= len(booked_time_slots):
    if counter == 0:
        if available_time[0] < booked_time_slots[counter][0] and (
                booked_time_slots[counter][0] - available_time[0]).total_seconds() / 60 >= meeting_time:
            start_time = available_time[0]
            end_time = booked_time_slots[counter][0]
            meeting_time_slots.append([start_time, end_time])
    elif counter == len(booked_time_slots):
        if booked_time_slots[counter - 1][1] < available_time[1] and (
                available_time[0] - booked_time_slots[counter - 1][1]).total_seconds() / 60 >= meeting_time:
            start_time = booked_time_slots[counter - 1][1]
            end_time = available_time[1]
            meeting_time_slots.append([start_time, end_time])
    else:
        if booked_time_slots[counter - 1][1] != booked_time_slots[counter][0] and (
                booked_time_slots[counter][0] - booked_time_slots[counter - 1][1]).total_seconds() / 60 >= meeting_time:
            start_time = booked_time_slots[counter - 1][1]
            end_time = booked_time_slots[counter][0]
            meeting_time_slots.append([start_time, end_time])

    counter += 1
    start_time = end_time = None

# Print he output in required format
for meeting_time in meeting_time_slots:
    print(f"{meeting_time[0].strftime('%H:%M')},{meeting_time[1].strftime('%H:%M')}", end=' ')
