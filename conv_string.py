import chardet
import argparse
import sys

ubNl = []

class ConvertString:
    def __init__(self,string):
        self.string = string
        self.string_values = []
    def conv_str_to_uni(self):
        for character in self.string:
            self.string_values.append(ord(character))
        return self.string_values
    def conv_uni_to_str(self):
        for character in self.string:
            self.string_values.append(chr(character))
        return self.string_values
    def conv_str_to_utf8(self):
        for character in self.string:
            self.string_values.append(character.encode("utf-8"))
        return self.string_values
    def conv_utf8_to_str(self):
        for character in self.string:
            self.string_values.append(character.decode("utf-8"))
        return self.string_values
    def conv_str_to_shi(self):
        for character in self.string:
            self.string_values.append(character.encode("shift_jis"))
        return self.string_values
    def conv_shi_to_str(self):
        for character in self.string:
            self.string_values.append(character.decode("shift_jis"))
        return self.string_values

class ConvCode:
    def __init__(self,arg_values):
        self.arg_values = arg_values
        self.string_code = ""
        self.split_values = []
    def conv_list_to_str(self,split_number):
        #文字列化
        self.string_code = ",".join(map(str,self.arg_values))
        return self.split_string_values(split_number)
    def split_string_values(self,the_number):
        def split_words_append(arg_word):
            self.split_values.append("".join(arg_word))
        for symbol_index,symbol in enumerate(self.string_code):
            if the_number != 1:
                if (symbol_index + 1) % the_number == 1:
                    #指定された文字数で文字を分断
                    try:
                        split_words_append(self.string_code[symbol_index:symbol_index+the_number])
                    #分断の際に余りが出たら、余りの文字を合計
                    except IndexError:
                        split_words_append(self.string_code[symbol_index:])
            else:
                self.split_values.append(symbol)
        return self.split_values
    def join_values(self):
        js = "".join(self.arg_values) #文字の結合
        jss = list(map(int,js.split(","))) #数値化してリストに格納
        return jss
    def join_split_values(self):
        return_values = self.arg_values.split(split_symbol)
        return return_values
    def ctadem(self):
        global stcs_dic
        stcs_dic = {}
        def dcappend(stcs_dic):
            if stcs_dic != {}:
                for v in list(stcs_dic.keys()):
                    self.arg_values[v] = "A"
                    if v == max(list(stcs_dic.keys())):
                        self.arg_values[v] = int("".join(list(stcs_dic.values())))
                stcs_dic = {}
            return stcs_dic
        for n,stc in enumerate(self.arg_values):
            if len(str(stc)) == 3:
                stcs_dic[n] = str(stc)
            else:
                stcs_dic
                stcs_dic = dcappend(stcs_dic)
        stcs_dic = dcappend(stcs_dic)
        self.arg_values = [value for value in self.arg_values if value != "A"]

        return self.arg_values
    def redem(self):
        for n,stc in enumerate(self.arg_values):
            if len(str(stc)) > 3:
                sn = 3
                stcs_list = []
                for i in range(0,len(str(stc)),sn):
                    stcs_list.append(str(stc)[i:i+sn])
                del self.arg_values[n]
                for i in reversed(stcs_list):
                    self.arg_values.insert(n,int(i))
        return self.arg_values


class ConvBase:
    def __init__(self,arg_split_values):
        self.arg_split_values = arg_split_values
        self.base_list = []
    def basee_t(self):
        for eb in self.arg_split_values:
            if "," in eb:
                #","を数字の"A"に置換する
                set_t = eb.replace(",","A")
            else:
                set_t = eb
            set_t = int(set_t,11) #11進数に変換
            self.base_list.append(set_t)
        return self.base_list
    def baset_e(self):
        for tb in self.arg_split_values:
            Nlc = []
            #10進数を11進数に
            while True:
                if tb == 0:
                    break
                #該当の値を11で割り、その余りをNlcに格納
                Nlc.append(tb % 11)
                #商は次に越す
                tb //= 11
            for n,nl in enumerate(Nlc):
                if nl == 10:
                    Nlc[n] = "A"
            Nlc = Nlc[::-1]
            set_e = "".join(map(str,Nlc))
            if "A" in set_e:
                set_e = set_e.replace("A",",")
            self.base_list.append(set_e)
        return self.base_list
    def Nbase_cl(self):
        base = len(ubNl) #189
        for ent in self.arg_split_values:
            Nlc = []
            #10進数をbase(189)進数に
            while True:
                if ent == 0:
                    break
                #該当の値をbase(189)で割り、その余りをNlcに格納
                Nlc.append(ubNl[ent % base])
                #商は次に越す
                ent //= base

            Nlc = Nlc[::-1]
            self.base_list.append("".join(Nlc))
        return self.base_list
    def Nbase_re(self):
        base = len(ubNl) #189
        for rent in self.arg_split_values:
            i = 0
            #base(189)進数から10進数に
            for n,v in enumerate(reversed(rent)):
                tbase = ubNl.index(v)
                #baseのn乗で
                i += base ** n * tbase
            self.base_list.append(i)
        return self.base_list
        

class Encrypt_small_data:
    def __init__(self,enctb_values):
        self.enctb_values = enctb_values
        self.enctb_list = []
    def encrypt_data(self):
        for tb in self.enctb_values:
            self.enctb_list.append(chr(tb))
        enc = "".join(self.enctb_list)
        with open("enc_sd.txt","w",encoding="utf-8") as f:
            f.write(enc) 
        return enc
    def encret_data(self):
        with open("enc_sd.txt","r",encoding="utf-8") as f:
            esr = f.read()
        for v in esr:
            self.enctb_list.append(ord(v))
        return self.enctb_list
    

def convstr(arg,type_):
    conv_type = type(arg)
    if type_ == "unicode":
        if conv_type is str:
            return ConvertString(arg).conv_str_to_uni()
        elif conv_type is list:
            return ConvertString(arg).conv_uni_to_str()
        else:
            raise("TypeError")
    elif type_ == "utf8":
        if conv_type is str:
            return ConvertString(arg).conv_str_to_utf8()
        elif conv_type is list:
            return ConvertString(arg).conv_utf8_to_str()
        else:
            raise("TypeError")
    elif type_ == "shift_jis":
        if conv_type is str:
            return ConvertString(arg).conv_str_to_shi()
        elif conv_type is list:
            return ConvertString(arg).conv_shi_to_str()
        else:
            raise("TypeError")

def convcode(list_,arg):
    return ConvCode(list_).conv_list_to_str(arg)

def revcode(list_):
    return ConvCode(list_).join_values()

def join_encryption(str_):
    return ConvCode(str_).join_split_values()

def datem(list_,type_):
    if type_ == "en":
        return ConvCode(list_).ctadem()
    elif type_ == "re":
        return ConvCode(list_).redem()
    else:
        raise("TypeError")

def convbase(arg,type_):
    if type_ == "et":
        return ConvBase(arg).basee_t()
    elif type_ == "te":
        return ConvBase(arg).baset_e()
    else:
        raise("TypeError")

def convbaseNl(arg,type_):
    if type_ == "en":
        return ConvBase(arg).Nbase_cl()
    elif type_ == "ren":
        return ConvBase(arg).Nbase_re()
    else:
        raise("TypeError")

def encsd(arg):
    return Encrypt_small_data(arg).encrypt_data()

def esrsd(arg):
    return Encrypt_small_data(arg).encret_data()

def encrypt(arg):
    s = convstr(arg,"unicode")
    r = convcode(s,5)
    b = convbase(r,"et")
    e = encsd(b)
    return "".join(e)


def rencsr(arg):
    e = esrsd(arg) #Unicode変換
    b = convbase(e,"te") #11進数化
    print(b)
    for n,sn in enumerate(b):
        #もし4桁以下なら
        if len(sn) <= 4:
            #0を上の桁に補填
            b[n] = "0" * (5-len(sn)) + sn
    r = revcode(b) #文字の結合
    s = convstr(r,"unicode") #文字化
    return "".join(s)
   
def encwb(arg):
    s = convstr(arg,"unicode")
    #計算の遅延化を防ぐため、データは100000文字ずつ区切る
    #(↑それ以外の場合区切らない。)
    r = convcode(s,100000)
    b = convbase(r,"et")
    t = convbaseNl(b,"en")
    #100000文字の句切れがあった場合、分ける。
    return split_symbol.join(t)

def rencwb(arg):
    #文字列の分断
    f = join_encryption(arg)
    #base(189)進数から10進数へ
    v = convbaseNl(f,"ren")
    #10進数から11進数に
    b = convbase(v,"te")
    #list内の数字の文字列を数値に
    for ne,be in enumerate(b):
        b[ne] = list(map(int,be.split(",")))
    cp_list = []
    for cp in b:
        cp_list += cp
    #文字化
    t = convstr(cp,"unicode")
    return "".join(t)

def ex1():
    with open("english_sentences.txt","r",encoding="utf-8") as f:
        p = encrypt(f.read())

    print(p)
    c = rencsr(p)
    with open("revenc_sd.txt","w",encoding="utf-8") as f:
        f.write(c) #revenc_sd.txtに書き込み  

    print(c)

def opcl(op):
    #サンプルセンテンスの読み込み
    with open(op,"r",encoding="utf-8") as f:
        fr = f.read()
        p = encwb(fr)
    #暗号化
    with open("en_sentences/en_"+op,"w",encoding="Shift-JIS") as f:
        f.write(p)
    with open("en_sentences/en_"+op,"r",encoding='Shift-JIS') as f:
        o = f.read()
    for n,pb in enumerate(p):
        if pb!=o[n]:
            print([pb,o[n]])
    #暗号を復元
    with open("de_sentences/de_"+op,"w",encoding="utf-8") as f:
        g = rencwb(o)
        f.write(g)
    #元の文と暗号化した文の一致性
    print(fr==g)

def ex2():
    opcl("element_sentences.txt")
    opcl("newspaper.txt")
    opcl("random_sentences.txt")


def setNl(code,arg):
    global split_symbol
    ubNl = []
    de_2byte = []
    for i in range(1114112):
        try:
            if len(chr(i).encode(code)) <= arg:
                ubNl.append(chr(i))
        except UnicodeEncodeError:
            pass
    split_symbol = ubNl[-1]
    del ubNl[ubNl.index("\r")]
    del ubNl[ubNl.index("‾")]
    del ubNl[ubNl.index("¥")]
    ubNl = ubNl[:-1]
    return ubNl



if __name__ == "__main__":
    ubNl = setNl("shift-JIS",1)
    parser = argparse.ArgumentParser(
            description="You can encrypt sentences with base189",
            epilog="end", # 引数のヘルプの後で表示
            add_help=True, # -h/–help オプションの追加
            )
    
    # 引数の追加
    parser.add_argument("-e", "--encode", help="encode sentences",nargs=2)
    parser.add_argument("-d","--decode",help="decode sentences",nargs=2)
    parser.add_argument("-c","--character",help="""choose character when you decode sentences. \n
        If you don't use this argument, the file that character is utf-8 will be generated.""",nargs=1)

    # 引数を解析する
    args = parser.parse_args()
    if args.encode:
        if len(args.encode) < 2:
            print("ArgumentError:You must type input-file and output-file!")
            sys.exit()
        if len(args.encode) > 2:
            print("ArgumentError:You must type input-file and output-file only!")
            sys.exit()
        if args.character:
            print("ArgumentError: You can't use -c/--character argument when you encode sentences.")
            sys.exit()
        with open(args.encode[0],"rb") as f:
            symbol_code = list(chardet.detect(f.read()).values())[0]
        with open(args.encode[0],"r",encoding=symbol_code) as f:
            enc = encwb(f.read())
        with open(args.encode[1],"w",encoding="shift-JIS") as f:
            f.write(enc) 
    if args.decode:
        if len(args.decode) < 2:
            print("ArgumentError:You must type input-file and output-file!")
            sys.exit()
        if len(args.decode) > 2:
            print("ArgumentError:You must type input-file and output-file only!")
            sys.exit()
        with open(args.decode[0],"r",encoding="shift-JIS") as f:
            renc = rencwb(f.read())
        echaracter='utf-8'
        if args.character:
            echaracter = args.character[0]
        with open(args.decode[1],"w",encoding=echaracter) as f:
            f.write(renc)