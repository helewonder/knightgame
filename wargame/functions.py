
def print_bold(msg, end='\n'):
    print("\033[1m" + msg + '\033[0m', end=end)


def print_dotted_line(width=80):
    print("-" * width)


def print_wave_line(width=80):
    print('~' * 80)


def show_health(rider, bold=False, end=' '):
    info = "||{:}'s Health=>{:2d}||".format(rider.name, rider.health_meter)
    if bold:
        print_bold(info, end=end)
    else:
        print(info, end=end)


def weighted_random_selection(obj1, obj2):
    weighted_list = [id(obj1)] * 3 + [id(obj2)] * 6 + [None] * 1
    selection = random.choice(weighted_list)

    if selection == id(obj1):
        return obj1
    elif selection == id(obj2):
        return obj2
    else:
        return None
