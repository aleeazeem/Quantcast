# Quantcast
    - Find the most active cookie for the given date. 
    - Most active cookie means the highest frequency of the cookie
    - Since the file is sorted by timestamp, countine till the input_date stays early then current_date in the loop
## Requirements
- Python3 (version 3.10.18 is used for thhis repo)
- Install dependencies "pip install -r requirements.txt"

## Command
```$PYTHONPATH=src python3 src/core/main.py -f quantcast.csv -d 2018-12-09```

