import argparse
import requests
from urllib.parse import urlparse,parse_qs
from banner import print_banner
from discovery import discover_parameters
from fuzzers import fuzz_parameters
from response_analyzer import analyze
from request_parser import parse_burp_request
from tqdm import tqdm
from colorama import Fore


def scan_url(url,headers):

    parsed = urlparse(url)

    base = parsed.scheme + "://" + parsed.netloc + parsed.path

    params = {k:v[0] for k,v in parse_qs(parsed.query).items()}

    print(Fore.CYAN + "[+] Target:",base)

    id_params = discover_parameters(params)

    print(Fore.YELLOW + "[+] ID Parameters:",id_params)

    baseline = requests.get(base,params=params,headers=headers)

    b_status = baseline.status_code
    b_len = len(baseline.text)

    print(Fore.GREEN + f"[+] Baseline -> {b_status} | {b_len}")

    results = fuzz_parameters(base,params,headers)

    for key,val,status,length in tqdm(results):

        verdict = analyze(b_status,b_len,status,length)

        if verdict == "POSSIBLE_IDOR":

            print(Fore.RED + "\n[!] Possible IDOR Detected")
            print("Parameter:",key)
            print("Payload:",val)
            print("Status:",status)
            print("Length:",length)


def main():

    print_banner()

    parser = argparse.ArgumentParser()

    parser.add_argument("-u","--url")
    parser.add_argument("--request")
    parser.add_argument("--header")
    parser.add_argument("--cookie")

    args = parser.parse_args()

    headers = {}

    if args.header:
        k,v = args.header.split(":")
        headers[k.strip()] = v.strip()

    if args.cookie:
        headers["Cookie"] = args.cookie

    if args.url:
        scan_url(args.url,headers)

    if args.request:

        method,url,headers = parse_burp_request(args.request)

        scan_url(url,headers)


if __name__ == "__main__":
    main()
