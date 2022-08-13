from time import time

import requests

from part1.sites import sites

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:103.0)" \
             "Gecko/20100101 Firefox/103.0"


def elapsed_time(function):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)

        func_name = function.__name__
        result_str = f'({result})' if result else ''
        url = f'[{args[0]}]' if args else ''

        print(f'[{func_name}][{url} Time elapsed: {time() - start_time:.2f}s {result_str}')

        return result

    return wrapper


@elapsed_time
def send_request(url):
    response = requests.get(url, headers={'User-Agent': user_agent})
    return response.status_code


@elapsed_time
def main():
    for site in sites:
        send_request(site)


if __name__ == '__main__':
    main()
