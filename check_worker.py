#!/usr/bin/env python3

# This Script checks your Worker service

# Imports
import requests, sys, bs4


# Check the worker
def check_worker(worker: str) -> None:
    try:
        print("\033[2;32mChecking...\033[m")
        response = requests.get(worker, timeout=10)
        if response.status_code == 200:
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            print(
                "\033[2;32m"
                + soup.find("p").text.replace("page", "message")
                + f"\nStatus code:     {response.status_code}\033[m"
            )
    except requests.exceptions.Timeout:
        print("\033[2;31mError: Timeout!! \033[m")
    except requests.exceptions.TooManyRedirects:
        print("\033[2;31mError: Too Many Redirects!! \033[m")
    except requests.exceptions.RequestException:
        print("\033[2;31mError: Request Exception!! \033[m")


# Run the program
if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h":
            print("Help: python check_worker https://workers-todo-snowy-breeze-0c41.victorisgeek.workers.dev/")
            sys.exit()
        check_worker(sys.argv[1])
        sys.exit()
    print("Error: No argument found!! rerun with -h")
