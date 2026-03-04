# IDOR-Hunter

Advanced IDOR Detection Tool for Security Researchers and Pentesters.

## Features

• Numeric ID fuzzing  
• UUID fuzzing  
• POST request fuzzing  
• JWT token IDOR testing  
• GraphQL IDOR testing  
• Automatic ID parameter discovery  
• Response comparison engine  a
• CLI interface  
• Windows / Linux / macOS support  

## Installation

git clone https://github.com/the4ingmaster/idor-hunter

cd idor-hunter

pip install -r requirements.txt

## Usage

GET scan

python idor_hunter.py -u "https://target.com/api/user?id=1001"

POST scan

python idor_hunter.py --post https://target/api --data "user_id=1001"

## Author

Anand Mahajan  
Pentester

## Disclaimer

For authorized security testing only.
