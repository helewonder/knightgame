
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
