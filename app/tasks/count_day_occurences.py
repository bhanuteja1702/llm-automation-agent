import datetime
import os
from dateutil import parser
from ..file_utils import read_lines, write_text

def count_day_occurences(input_file: str, output_file: str, day: int):
    dates = read_lines(input_file)
    count = 0

    for date in dates:
        date_str = date.strip()
        try:
            date_obj = parser.parse(date_str)
            if date_obj.weekday() == day:
                count += 1
        except ValueError:
            pass

    write_text(output_file, str(count))
