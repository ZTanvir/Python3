def smallest_average(person1: dict, person2: dict, person3: dict):
    people1 = person1.copy()
    people2 = person2.copy()
    people3 = person3.copy()

    peoples = [people1, people2, people3]

    for people in peoples:
        avg = (people["result1"] + people["result2"] + people["result3"]) / 3
        people["avg"] = avg
        print(people)

    # lowest
    lowest = people1["avg"]
    print(lowest)
    for people in peoples:
        if people["avg"] < lowest:
            lowest = people["avg"]

    print(lowest)

    # find lowest
    def lowest_avg_dict(all_peoples: list):
        for people in all_peoples:
            if lowest == people["avg"]:
                people.pop("avg")
                return people

    return lowest_avg_dict(peoples)


if __name__ == "__main__":
    person1 = {"name": "Anna", "result1": 9, "result2": 9, "result3": 9}
    person2 = {"name": "Anna", "result1": 7, "result2": 7, "result3": 7}
    person3 = {"name": "Anna", "result1": 8, "result2": 8, "result3": 8}

    print(smallest_average(person1, person2, person3))
