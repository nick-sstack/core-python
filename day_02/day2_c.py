def crowd_test_one(lst):
    if len(lst) > 3:
        print("Room is crowded")


def crowd_test_two(lst):
    if len(lst) > 3:
        print("Room is crowded")
    else:
        print("The room is not very crowded")


def crowd_test_three(lst):
    if len(lst) > 5:
        print("There is a mob")
    elif len(lst) > 2:
        print("The room is crowded")
    elif len(lst) == 0:
        print("The room is empty")
    else:
        print("The room is not very crowded")


names = ["Mark", "John", "Alex", "Sam"]
crowd_test_one(names)
names.remove("Mark")
names.remove("John")
crowd_test_one(names)
crowd_test_two(names)
names.append("Chris")
names.append("Steve")
crowd_test_two(names)
names.append("Mark")
names.append("John")
crowd_test_three(names)
