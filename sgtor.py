from urllib import request
from tqdm import tqdm
from PIL import Image
import re
import os
import pyocr
import pyocr.builders
import random


def generate_elements_sentences():
    element_dict = {}

    url = 'https://ja.wikipedia.org/wiki/%E5%85%83%E7%B4%A0%E3%81%AE%E4%B8%80%E8%A6%A7?adlt=strict&toWww=1&redig=7C55D86D377B44469E6140D2C4618D8C'
    response = request.urlopen(url) #Webのソースコードを取得
    content = response.read()
    response.close()
    html = content.decode()

    with open("de_html.txt","w",encoding="utf-8") as f:
        f.write(html) #ソースコードをde_html.txtに書き込む

    with open("de_html.txt","r",encoding='utf-8') as f:
        s = f.readlines() #一行ずつ読み込んでリストに格納
        print("Appending elements...")
        for i in tqdm(range(118)):
            #元素名を含む行番号を取得
            if i <= 108:
                row = 577 + i * 19
            else:
                row = 577 + i * 19 - 1
            including_element_name = s[row]
            #元素名を取得
            element_name = re.findall(r'title="(.+)"',including_element_name)[0]
            element = re.findall(r'>(.*)<',s[row-1])[0] #元素記号を取得
            if element == "H2":
                element = "H" #(2022念8月7日時点)水素が分子表示になっている為。
            #element_dictという辞書型リストに格納
            element_dict[element] = element_name

    #文章の作成、txtに書き込み
    with open("element_sentences.txt","w",encoding='utf-8') as f:
        keys = list(element_dict.keys())
        print("Writing elements_file...")
        for i in tqdm(range(len(element_dict))):
            element = keys[i]
            f.write("{0}:{1}\n".format(element,element_dict[element]))


def read_with_ocr():
    #Tesseractのパスを通す
    path_tesseract = "C:\\Program Files\\Tesseract-OCR"
    if path_tesseract not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + path_tesseract

    tools = pyocr.get_available_tools() #OCRエンジンの取得
    tool = tools[0]

    img_org = Image.open("IMG_E0242.jpg")
    builder = pyocr.builders.TextBuilder()
    result = tool.image_to_string(img_org, lang="jpn_vert", builder=builder)

    print(result)

def random_sentences():
    symbol_list = []
    break_ = False
    #制御文字の数値が格納されたリスト
    control_characters = [127,1564,8206,8207,8234,8235,8236,8237,8238,8294,8295,8296,8297]
    print("Writing random sentences...")
    for i in tqdm(range(250)):
        while True:
            number = random.randint(32,40918)
            try:
                a = chr(number)
            except UnicodeEncodeError:
                continue
            #空白のUnicodeに当てはまらないか確認する。
            if number >= 55296 and number <= 57343:
                continue
            #制御文字でないか確認する。
            for character in control_characters:
                if number != character:
                    break_ = True
                    break
            if break_:
                break
        symbol_list.append(chr(number)) #symbol_listに格納
    with open("random_sentences.txt","w",encoding='utf-8') as f:
        f.write(''.join(symbol_list)) #symbol_listの文字を全て書き入れる。

if __name__ == "__main__":
    random_sentences()