# simple-event-calender
Simple event calender that allows user to listout the events and add events , delete evets as per choice

import datetime


events = {}

def add_event(date, event):
    
    if date in events:
        events[date].append(event)
    else:
        events[date] = [event]

def show_events(date):
    
    if date in events:
        print(f"Events on {date}:")
        for event in events[date]:
            print(f"- {event}")
    else:
        print(f"No events found on {date}.")

def main():
    while True:
        print("\nWelcome to the Simple Event Calendar!")
        print("Choose an option:")
        print("1. Add an event")
        print("2. Check events for a specific date")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            
            date_input = input("Enter the date for the events (YYYY-MM-DD): ")
            event_input = input("Enter the event description: ")

            try:
                
                event_date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
                add_event(event_date, event_input)
                print(f"Event added on {event_date}!")
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")

        elif choice == '2':
            
            date_input = input("Enter the date to check for events (YYYY-MM-DD): ")
            try:
                
                event_date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
                show_events(event_date)
            except ValueError:
                print("Invalid date format! Please use YYYY-MM-DD.")

        elif choice == '3':
            
            print("Exiting the calendar. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
