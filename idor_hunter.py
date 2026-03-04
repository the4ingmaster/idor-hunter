import argparse
import requests
from urllib.parse import urlparse, parse_qs
from banner import print_banner
from discovery import discover_id_parameters
from fuzzers import fuzz_get, fuzz_post
from tqdm import tqdm
from colorama import Fore


def compare_response(base, new):

    return base.status_code == new.status_code and len(base.text) == len(new.text)


def run_get_scan(url):

    parsed = urlparse(url)

    base_url = parsed.scheme + "://" + parsed.netloc + parsed.path
    params = {k:v[0] for k,v in parse_qs(parsed.query).items()}

    print(Fore.CYAN + f"[+] Target: {base_url}")
    print(Fore.CYAN + f"[+] Parameters: {params}")

    id_params = discover_id_parameters(params)

    print(Fore.YELLOW + f"[+] Discovered ID params: {id_params}")

    base_response = requests.get(base_url, params=params)

    for param in id_params:

        mutations = fuzz_get(base_url, params, param)

        print(Fore.YELLOW + f"[+] Testing parameter: {param}")

        for m in tqdm(mutations):

            r = requests.get(base_url, params=m)

            if compare_response(base_response, r):

                print(Fore.RED + "[!] Possible IDOR")
                print("Payload:", m)
                print()


def main():

    print_banner()

    parser = argparse.ArgumentParser()

    parser.add_argument("-u","--url",help="Target URL")
    parser.add_argument("--post",help="POST endpoint")
    parser.add_argument("--data",help="POST data example")

    args = parser.parse_args()

    if args.url:
        run_get_scan(args.url)


if __name__ == "__main__":
    main()