import requests
from bs4 import BeautifulSoup

base_url = 'https://zxcs.zip/book/'  # 目标网址
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    ,
    'Cookie': '_ga=GA1.1.49920129.1713079536; _clck=1gl5u52%7C2%7Cfml%7C0%7C1565; XSRF-TOKEN=eyJpdiI6Ik5CU29sRzFkSEFlcG0xRmpIRWVJNmc9PSIsInZhbHVlIjoiS0RYQ24rUWNoWXVvVU9qK2J4UXVBQzBIdGFLMkFhdG9YVEVGdnhCZnBjMFZuRUI2STM1eGlRWU9mUmF1OEdETXA1VVIvY1NOU2N2TEFiYzZaWmZRYmJMamdGSG9ZVkV5UmdRN3NKUTJmMXNGSzZncllXWDFIdVNKR1Y1NUZIWE8iLCJtYWMiOiI5MjhkZDJkNmVjYWExMmYzYzQyMzE5YzJjM2UxNzA4NWM2OWYxMWRmYjlkMzhhNTM0NTRmM2U5YmU1YzU5MTI4IiwidGFnIjoiIn0%3D; laravel_session=eyJpdiI6IkRJam13TTNBaHh1dHpyNTF0MFR0R1E9PSIsInZhbHVlIjoiaTRiR2xDUjEwYjRCbUVyeTZ0dWppeElmaDZWcEM2ZXd2MDBKUFlUTm9oekpCT201SnNsWWR6L3gyMlp2MFBiZ0s2WHc3cno3TVNKK0cvaks3Q2tQYVIrNis3Z3NvcCt5SE5CUi9tUWIwMGk1ZFZhZXQweitFZEcrQUYyaGJBcnoiLCJtYWMiOiIzMWRmZWQ1MWVjNDJmNmM1NzljZDA5NmU5MjdhNGRhZjYwZjQ1ZTZiY2M3YzA2YjgyMGIyMDljZGVhNGI1NmI1IiwidGFnIjoiIn0%3D; _ga_58XH0DYFV5=GS1.1.1718259930.8.1.1718260288.59.0.0; _clsk=ivrgwb%7C1718260289709%7C8%7C1%7Cq.clarity.ms%2Fcollect'
}


def fetch_data(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print("请求错误，状态码：", response.status_code)
    except Exception as e:
        print("请求过程中发生错误：", e)


def parse_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # 提取出下载连接
    download_link = soup.find('a', id='downloadtxt')
    if download_link:
        # 正确分离作品名和作者
        filename = download_link['href'].split('/')[-1]
        title_author = filename.split('《')[1].split('》')[0]  # 假设文件名格式固定
        # 更精确地获取作者名，确保不包含'.txt'
        author_part = filename.split('作者：')[-1]
        author = author_part.split('.')[0].strip()  # 分割掉'.txt'前的部分并去空格
        print("正在爬取 %s ,作者 %s" % (title_author, author))
        filename = "D:\\MyFile\\TextTxt\\" + filename
        download_file(download_link['href'], filename)


def download_file(url, filename):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print("文件下载成功！")
        else:
            print("文件下载失败，状态码：", response.status_code)
    except Exception as e:
        print("文件下载过程中发生错误：", e)


def main(i):
    url = base_url + i
    html_content = fetch_data(url)
    if html_content:
        parse_data(html_content)
