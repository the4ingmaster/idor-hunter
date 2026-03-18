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


**Example Usage**

**Basic scan**
python idor_hunter.py -u "https://api.example.com/user?id=1001"


**Authenticated endpoint**

python idor_hunter.py \
-u "https://api.example.com/user?id=1001" \
--header "Authorization: Bearer TOKEN"


**Cookie authentication**

python idor_hunter.py \
-u "https://example.com/account?id=1" \
--cookie "session=abc123"


**Burp request import**

python idor_hunter.py --request examples/burp_request.txt


**Example Output**

[+] Target: https://api.example.com/user
[+] ID Parameters: ['user_id']

[+] Baseline -> 200 | 5421

[!] Possible IDOR Detected
Parameter: user_id
Payload: 1002
Status: 200
Length: 5401
## Author

Anand Mahajan  
Pentester

## Disclaimer

For authorized security testing only.
