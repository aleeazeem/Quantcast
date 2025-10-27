import argparse
import sys
from collections import Counter

def get_active_cookies(file_path: str, input_date: str) -> list[str]:
    cookie_map = Counter()
    try:
        with open(file_path, 'r') as file:
            next(file)
            
            for line in file:
                line = line.strip()
                if not line:
                    continue
                cookie, timestamp = line.split(',', 1)
                date = timestamp.split('T')[0]
                if date == input_date:
                    cookie_map[cookie] += 1
                elif date < input_date:
                    break
        
        if not cookie_map:
            return []
        
        return [cookie for cookie, count in cookie_map.items() 
                if count == max(cookie_map.values())]
    
    except Exception as e:
        print("Error occured during the execution:\n", {e})
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", required=True)
    parser.add_argument("-d", required=True)
    args = parser.parse_args()
    
    cookie_list = get_active_cookies(args.f, args.d)
    for cookie in cookie_list:
        print(cookie)

if __name__ == "__main__":
    main()
    
    
    
