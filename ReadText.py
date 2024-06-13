import chardet


# 读取本地txt文件,一行行读取
def read_txt(file_path):
    with open(file_path, 'r', encoding='GB2312') as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())


def detect_encoding_and_read(file_path):
    # 检测文件编码
    with open(file_path, 'rb') as rawdata:
        result = chardet.detect(rawdata.read(10000))
    print(result['encoding'])
    # 使用检测到的编码读取文件
    encoding = result['encoding'] or 'utf-8'
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()


read_txt('D:/MyFile/Norle/纣临.txt')

# content = detect_encoding_and_read('D:/MyFile/Norle/纣临.txt')
# print(content)
