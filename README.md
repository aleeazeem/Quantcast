# Quantcast - Most Active Cookie Finder
This project provides a command line tool to find the most active cookie from a csv cookie log for a specific date. It is designed to be robust, maintainable, and production ready.

## Highlights
    - Find the most active cookie for the given date. 
    - Most active cookie means the highest frequency of the cookie
    - Since the file is sorted by timestamp, countine till the input_date stays early then current_date in the loop
    - Logging to app.log for info, warnings, and errors
    
### Production Grade Error Handling
- File not found
- Permission denied
- Invalid csv lines
- invalid data format

---

## Requirements
- Python 3.10+
- No third party libraries are required (no requirements.txt file)

---

## Usage

### Single File Execution
```python main.py -f ./data/cookie_log.csv -d 2018-12-09```

### Multiple Files with Shell Script
```
chmod +x run_all.sh
./run_all.sh
```
---

## Testing
Run all tests: ```pytest -v```

Run tests with coverage: 
```
pip install pytest-cov
pytest --cov=src tests/
```


---

## Logging
All logs are written to app.log file in the root directory. That includes info, error, warning
Fromat: YYYY-MM-DD HH:MM:SS [Log Level] Log Text

### Example: 
```
2025-10-24 14:10:01 [INFO] Processed file ./data/cookie_log.csv for date 2018-12-09: 1 most active cookie found
2025-10-24 14:11:02 [ERROR] File not found: ./data/missing_file.csv
2025-10-24 14:12:05 [WARNING] Execution interrupted
```

---

## Production Ready Features
1. Robust error handling (file, CSV, date format, keyboard interrupts)
2. Logging for traceability
3. Clean CLI interface with argparse
4. Modular design
5. Fully testable with pytest



