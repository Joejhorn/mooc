# Write your solution here
def oldest_person(people):
    oldest = people[0]
    for person in people:
        if person[1] < oldest[1]:
            oldest = person

    return oldest[0]   




if __name__ == '__main__':
    people_list = [ 
                [("Arthur", 1977), ("Emily", 2014)],
                [("Emily", 2014), ("Arthur", 1977)],
                [("Emily", 2014), ("Arthur", 1977), ("Ernest", 1985),  ("Mary", 1953), ("Ellen", 1997)],
                [("Jacob", 2016), ("Harry", 2019), ("Oliver", 2012),  ("Wendy", 2013), ("Jane Doe", 2020)],
                [("Donald", 1982), ("Daisy", 1892), ("Angela", 1965),  ("Vladimir", 2000), ("Dunja", 1919), ("Elizabeth", 1921)]
            ]

    print(oldest_person(people_list))