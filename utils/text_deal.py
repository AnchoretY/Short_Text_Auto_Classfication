def get_dealed_text(ori_text):
    """
        从输入数据获取各个短文
        return list
    """

    dealed_text = []
    for text in ori_text.split("\n"):
        if text!="":
            dealed_text.append(text)
    return dealed_text

def get_stopword(filepath):
    """
        获取停用词表
        return list
    """
    with open(filepath,'r') as file_object:
        tmp = file_object.read()
    stopword_list = tmp.splitlines()
        
    return stopword_list


def split_word(parase):
    """
        初步切分
        return list
    """
    tmp = parase.split(" ")
    return tmp

def get_final_split_result(text=None):
    """
        调用上面三个函数，将输入变成分好词以空格进行分割的字符串
        param text:线上使用时直接将text传入，不需要进行读取文件
    """
    dealed_texts = get_dealed_text(text)  
    stopwords = get_stopword("./english_stopword.txt")
    result = []

    for dealed_text in dealed_texts:
        words = split_word(dealed_text)
        tmp = ""
        for word in words:
            if word not in stopwords:
                tmp+=" "+word
        result.append(tmp)
    return result


def get_doc_list(docs):
    """
        将分词、去除停用词后的字符串转化成list
    """
    doc_list = []
    for doc in docs:
        doc_list.append(doc.split())
    return doc_list






