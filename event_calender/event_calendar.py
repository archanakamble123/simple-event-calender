import pandas as pd
from datetime import datetime

def load_events(file_path):
    return pd.read_csv(file_path)

def format_dates(events):
    events['date'] = pd.to_datetime(events['date'])
    return events

def display_events(events):
    for index, row in events.iterrows():
        print(f"{row['date'].strftime('%Y-%m-%d')}: {row['title']} - {row['description']}")

def get_events_by_date(events, query_date):
    filtered_events = events[events['date'] == query_date]
    return filtered_events

def search_events(events, keyword):
    results = events[events['title'].str.contains(keyword, case=False) | 
                     events['description'].str.contains(keyword, case=False)]
    return results

def main():
    events_df = load_events('events.csv')
    events_df = format_dates(events_df)

    print("All Events:")
    display_events(events_df)

    tomorrow = datetime.now().date() + pd.DateOffset(days=1)
    events_tomorrow = get_events_by_date(events_df, tomorrow)

    print("\nEvents for Tomorrow:")
    if not events_tomorrow.empty:
        display_events(events_tomorrow)
    else:
        print("No events scheduled for tomorrow.")

    keyword = input("\nEnter a keyword to search for events: ")
    search_results = search_events(events_df, keyword)

    print("\nSearch Results:")
    if not search_results.empty:
        display_events(search_results)
    else:
        print("No events found matching your search.")

if __name__ == "__main__":
    main()