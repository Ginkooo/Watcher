import os
import csv
import datetime
from watch_log import get_date
import analysis as anls
import time_operations as to

class Color:

    def GREY(self):
        return '\033[90m' + self + '\033[0m'

    def BLUE(self):
        return '\033[34m' + self + '\033[0m'

    def GREEN(self):
        return '\033[32m' + self + '\033[0m'

    def YELLOW(self):
        return '\033[33m' + self + '\033[0m'

    def RED(self):
        return '\033[31m' + self + '\033[0m'

    def PURPLE(self):
        return '\033[35m' + self + '\033[0m'

    def DARKCYAN(self):
        return '\033[36m' + self + '\033[0m'

    def BOLD(self):
        return '\033[1m' + self + '\033[0m'

    def UNDERLINE(self):
        return '\033[4m' + self + '\033[0m'

def daily_summary(date = get_date()):
    window_opened, time_spent = anls.extract_data(date)
    Total_screen_time = "00:00:00"
    for x,y in anls.final_report(window_opened, time_spent).items():
        Total_screen_time = to.time_addition(y, Total_screen_time)

    if date == get_date():
        if len(to.format_time(Total_screen_time)) == 3:
            print(Color.YELLOW("\n   Today's Screen-Time\t\t   ") + Color.BLUE(f'{to.format_time(Total_screen_time):>16}'))
        elif len(to.format_time(Total_screen_time)) == 7:
            print(Color.YELLOW("\n   Today's Screen-Time\t\t   ") + Color.BLUE(f'{to.format_time(Total_screen_time):>11}'))
        elif len(to.format_time(Total_screen_time)) == 11:
            print(Color.YELLOW("\n   Today's Screen-Time\t\t   ") + Color.BLUE(to.format_time(Total_screen_time)))
    elif date == os.popen("""date -d "1 day ago" '+%Y-%m-%d'""").read()[:-1]:
        if len(to.format_time(Total_screen_time)) == 3:
            print(Color.YELLOW("\n   Yestarday's Screen-Time\t   ") + Color.BLUE(f'{to.format_time(Total_screen_time):>16}'))
        elif len(to.format_time(Total_screen_time)) == 7:
            print(Color.YELLOW("\n   Yestarday's Screen-Time\t   ") + Color.BLUE(f'{to.format_time(Total_screen_time):>11}'))
        elif len(to.format_time(Total_screen_time)) == 11:
            print(Color.YELLOW("\n   Yestarday's Screen-Time\t   ") + Color.BLUE(to.format_time(Total_screen_time)))
    elif len(to.format_time(Total_screen_time)) == 3:
        print(Color.YELLOW("\n   "+date+"'s Screen-Time\t   ") + Color.BLUE(f'{to.format_time(Total_screen_time):>6}'))
    elif len(to.format_time(Total_screen_time)) == 7:
        print(Color.YELLOW("\n  "+ date+ "'s Screen-Time\t   ") + Color.BLUE(f'{to.format_time(Total_screen_time):>1}'))
    elif len(to.format_time(Total_screen_time)) == 11:
        print(Color.YELLOW("\n   "+date+"'s Screen-Time\t   ") + Color.BLUE(to.format_time(Total_screen_time)))

    print(" ────────────────────────────────────────────────")
    print(Color.RED(f'{" App Usages":>29}'))
    print(" ────────────────────────────────────────────────")

    for x,y in anls.final_report(window_opened, time_spent).items():
        if x == "":
            x = "Home-Screen"
        print("   " + Color.GREEN(f'{x:<22}') + '\t ',f'{to.format_time(y):>12}')

def week_summary(week = os.popen('''date +"W%V-%Y"''').read()[:-1]):
    user = os.getlogin()
    filename = f"/home/{user}/.cache/Watcher/Analysis/{week}.csv"
    with open(filename, 'r') as file:
        csvreader = csv.reader(file, delimiter='\t')
        week_overview = {}
        app_usages = {}
        for row in csvreader:
            if len(row[0]) == 3:
                week_overview[row[0]] = row[1]
            else:
                app_usages[row[1]] = row[0]

    week_screen_time = "00:00:00"
    for y in week_overview.values():
        week_screen_time = to.time_addition(y, week_screen_time)

    if week == os.popen('''date +"W%V-%Y"''').read()[:-1]:
        print(Color.PURPLE("\n   Week's screen-time\t\t   ") + Color.BLUE(to.format_time(week_screen_time)))
    elif week == os.popen("""date -d 'last week' '+W%W-%Y'""").read()[:-1]:
        print(Color.PURPLE("\n   Previous Week's \t\t   ") + Color.BLUE(to.format_time(week_screen_time)))
        print(Color.PURPLE("     Screen-Time"))
    else:
        print(Color.PURPLE("\n     "+week[1:3]+ "th week of\t   ") + Color.BLUE(to.format_time(week_screen_time)))
        print(Color.PURPLE(f"   {week[4:]}" + " screen-time\t    "))

    print(" ────────────────────────────────────────────────")

    for x, y in week_overview.items():
        print(f'  {Color.YELLOW(x):>21}' + "\t\t   " + Color.BLUE(to.format_time(y)))

    #anls.prints_report(window_opened, time_spent, is_week)
    print(" ────────────────────────────────────────────────")
    print(Color.RED(f'{" App Usages":>29}'))
    print(" ────────────────────────────────────────────────")
    for x,y in app_usages.items():
        if x == "":
            x = "Home-Screen"
        print("   " + Color.GREEN(f'{x:<22}') + '\t ',f'{to.format_time(y):>12}')

#testing
if __name__ == "__main__":
    week_summary("W27-2022")
    #daily_summary("2022-07-18")
