from datetime import datetime,timedelta,date
def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")
  
def calculate_future_date():
    date_difference = int(input("Enter the number of days to add to the current date: ")) 
    delta = timedelta(days=date_difference)
    future_date = date.today() + delta
    print(f"Future date: {future_date}")