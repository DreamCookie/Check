import urllib.request
import requests
from datetime import datetime

urls = [
    "https://webservices.mirea.ru/upload/iblock/59d/qzcm0x7ldzx47rm8mi88g1cb7mkx5wwl/IIT_1-kurs_2022_2023_zima.xlsx",
    "https://webservices.mirea.ru/upload/iblock/2bf/cmd3o40atu8lloph4p3xol5cihc5vc30/IIT_2-kurs_2022_2023_zima.xlsx",
    "https://webservices.mirea.ru/upload/iblock/d05/uli1u341z71h8otjanmly153mdpzkgu7/IIT_3-kurs_2022_2023_zima.xlsx",
    "https://webservices.mirea.ru/upload/iblock/69c/2849u0n5h0okevgui6wm44cvw3l1stl0/IIT_4-kurs_2022_2023_zima.xlsx"
]
save_dir = "Загрузки"

for url in urls:
    response = requests.head(url)

    last_modified_header = response.headers.get("Last-Modified")

    last_modified_date = datetime.strptime(last_modified_header, '%a, %d %b %Y %H:%M:%S %Z')

    file_name = url.split("/")[-1]
    urllib.request.urlretrieve(url, file_name)

    print(f"Расписание {file_name} было загружено {last_modified_date}")

input("Press Enter to close the script...")
exit()
