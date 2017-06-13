from functions import print_wave_line


class GameUnitError(Exception):
    def __init__(self, message=""):
        super().__init__(message)
        self.error_message = "Unspecified Error!"


class HutOutRangeError(GameUnitError):
    def __init__(self, message=""):
        self.error_message ="
        OUT OF RANGE: Notice the huts number range.
        "
        print_wave_line("\nERROR: ", self.error_message)


class HutNotNumberError(GameUnitError):
    def __init__(self,message=""):
        self.error_message="
        NOT A NUMBER: Must input a int number in huts number range.
        "
        print_wave_line("\nERROR: ", self.error_message)
