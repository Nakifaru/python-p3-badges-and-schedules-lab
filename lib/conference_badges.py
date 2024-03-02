def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    # name_statement = [f'Hello, my name is {name}.' for name in names]
    # print(name for name in name_statement)
    # return name_statement

    names_list = []
    for name in names:
        name_statement = f'Hello, my name is {name}.'
        names_list.append(name_statement)
        print(name_statement)
    return names_list

def assign_rooms(names):
    # assigned_rooms = [f"Hello, {name}! You'll be assigned to room {names.index(name) + 1}!" for name in names]
    # print(room for room in assigned_rooms)
    # return assigned_rooms

    assigned_rooms = []
    i = 1
    for name in names:
        room = f"Hello, {name}! You'll be assigned to room {i}!"
        assigned_rooms.append(room)
        i += 1
        print(room)
    return assigned_rooms

def printer(names):
    batch_badge_creator(names)
    assign_rooms(names)
    
    