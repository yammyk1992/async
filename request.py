import requests


def download(q: str, p: str):
    header = {"Authorization": "563492ad6f91700001000001291a5eea47384eafbbb2db56a3f2c6bb"}
    i = 1
    while i <= int(p):
        url = f"https://api.pexels.com/v1/search?query={q}&per_page=1&page={i}"
        r = requests.get(url, headers=header)
        if r.status_code == 200:
            _r = r.json()
            print(_r)
            for item in _r.get('photos'):
                print(item.get('url'))

        else:
            print(r.text)
        i += 1


# поиск фотографий по ключевому слову!
def main() -> None:
    q = input("Query ")
    p = input("Count page ")
    download(q, p)


main()
