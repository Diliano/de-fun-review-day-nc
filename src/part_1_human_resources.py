from copy import deepcopy

def make_name_tags(guests):
    result = []

    copy_guests = deepcopy(guests)

    for guest in copy_guests:
        part_name_tag = (" ").join([guest["title"], guest["forename"], guest["surname"]])
        name_tag = part_name_tag + ", " + guest["company"]
        guest["name_tag"] = name_tag
        result.append(guest)

    return result


def create_poll(votes):
    result = {}

    for vote in votes:
        if vote not in result:
            result[vote] = 1
        else:
            result[vote] += 1

    return result