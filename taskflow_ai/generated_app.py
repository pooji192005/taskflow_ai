
from datetime import date

class PeriodTracker:
    def __init__(self):
        self.period_dates = []

    def add_period(self, start_date, end_date):
        if len(self.period_dates) == 0:
            self.period_dates.append({
                'start_date': date.fromisoformat(start_date),
                'end_date': date.fromisoformat(end_date)
            })
        else:
            last_start_date = self.get_last_start_date()
            if start_date > str(last_start_date):
                self.period_dates.append({
                    'start_date': date.fromisoformat(start_date),
                    'end_date': end_date
                })

    def get_last_start_date(self):
        return self.period_dates[-1]['start_date']

    def display_periods(self):
        for period in self.period_dates:
            print(f"Start Date: {period['start_date']}, End Date: {period['end_date']}")

def main():
    tracker = PeriodTracker()
    while True:
        user_input = input("Enter start and end dates (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        start_date, end_date = user_input.split(' ')
        tracker.add_period(start_date, end_date)
    tracker.display_periods()

if __name__ == "__main__":
    main()
