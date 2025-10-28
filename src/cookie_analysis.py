from collections import defaultdict
from datetime import datetime
from typing import List, Tuple

def read_log_file(filename) -> List[Tuple[str, str]]:
    records = []
    with open(filename, "r") as file:
        next(file)  
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 2:
                continue  
            cookie, timestamp = parts
            try:
                dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                date_str = dt.date().isoformat()
                records.append((cookie, date_str))
            except ValueError:
                continue  
    return records

def get_most_active_cookies(records, target_date) -> List[str]:
    
    counter = defaultdict(int)
    for cookie, date in records:
        if date == target_date:
            counter[cookie] += 1

    if not counter:
        return []

    max_count = max(counter.values())
    most_active = [cookie for cookie, count in counter.items() if count == max_count]
    print(f"Most active cookies for {target_date}: {most_active} with count {max_count}")
    return most_active