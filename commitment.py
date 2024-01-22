# No Smoking. A simple text program that tracks how long you have not smoked.

import re
import os
import datetime

class Setup:
    """
    Setup Class.

    Methods:
        date_validator: Validates date
        time_validator: Validates time
        get_date: Gets date from stdin
        get_time: Gets time from stdin
    """

    def __init__(self, quit_date, quit_time, filepath="~", filename=".nosmoking"):
        """
        Initiator for Setup class.
        Arguments:
            quit_date: string. Quit date in DD/MM/YYYY format.
            quit_time: string. Quit time in HH:MM format (24 hours)
            filepath: string. Either absolute path, or '~' to represent $HOME. Default is '~'
            filename: string. File name for commitment file.
        """
        self.quit_date = quit_date
        self.quit_time = quit_time
        self.filepath = filepath
        self.filename = filename

    def date_validator(self, date_entry):
        """
        Date validator method.
        Return value: Boolean
        """
        output = False

        if re.match("^[0-9]{2}\/[0-9]{2}\/[0-9]{4}$", date_entry):
            day, month, year = date_entry.split('/')
            day = int(day)
            month = int(month)
            year = int(year)

            # Check for +ve values only.
            if day > 0 and month > 0 and year >= 0:
                # Special condition for February
                if month == 2:
                    leap = False
                    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                        leap = True
                    if leap:
                        if day <= 29:
                            output = True
                    else:
                        if day <= 28:
                            output = True
                # Condition for months with 30 days.
                elif month in [4, 6, 9, 11]:
                    if day <= 30:
                        output = True
                # Condition for all other months (automatically 31 days)
                elif month <= 12:
                    if day <= 31:
                        output = True

        return output

    def time_validator(self, time_entry):
        """
        Time Validator method.
        Return value: Boolean
        """
        output = False

        if re.match("^[0-9]{2}:[0-9]{2}$", time_entry):
            hour, minute = time_entry.split(':')
            hour = int(hour)
            minute = int(minute)

            if (hour >= 0 and hour <= 23) and (minute >= 0 and minute <= 59):
                output = True

        return output

    def get_date(self):
        """
        Gets date from stdin. Runs in a loop until correct date is entered.
        """
        while self.quit_date == "":
            date_entry = input("Enter Quit Date (DD/MM/YYYY): ")
            if self.date_validator(date_entry):
                self.quit_date = date_entry
            else:
                print("Enter a valid date. Try Again.")

    def get_time(self):
        """
        Gets time from stdin. Runs in a loop until correct time is entered.
        """
        while self.quit_time == "":
            time_entry = input("Enter Quit Time (HH:MM): ")
            if self.time_validator(time_entry):
                self.quit_time = time_entry
            else:
                print("Enter a valid time. Try Again.")


if __name__ == "__main__":
    # Debug
    setup = Setup("","","/bin","")
