

class GameUnitError(Exception):
    def __init__(self, message=""):
        super().__init__(message)
        self.error_message = "Unspecified Error!"


class HutOutRangeError(Exception):
    def __init__(self, message=""):
        super().__init__(message)
        self.error_message = "OUT OF RANGE: Notice the huts number range."
        # print_wave_line("\nERROR: ", self.error_message)


class HutNotNumberError(Exception):
    def __init__(self, message=""):
        super().__init__(message)
        self.error_message = "NOT A NUMBER: Must input a int number in huts umber range."
        # print_wave_line("\nERROR: ", self.error_message)
