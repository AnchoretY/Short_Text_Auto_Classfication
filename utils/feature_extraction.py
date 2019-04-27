import math
        


def train_idf(doc_list):
    """
        从整体语料库中学习到各个词的idf值
        param doc_list:文章列表
    """
    idf_dic = {}

    tf_count = len(doc_list)

    #每个词出现的文档数
    for doc in doc_list:
        for word in set(doc):
            idf_dic[word] = idf_dic.get(word,0.0) +1.0

    #按照公式转化为idf值，分母加1进行平滑处理
    for k,v in idf_dic.items():
        idf_dic[k] = math.log(tf_count/(1.0+v))
    return idf_dic

# idf_dic = train_idf(doc_list)


class TfIdf:
    def __init__(self, idf_dic, default_idf, word_list,words):
        """
        TF-IDF类的构造函数
        :param idf_dic: 训练好的idf词典
        :param default_idf: 默认idf值
        :param word_list: 经处理的(过滤停用词)待提取关键词文本列表
        :param keyword_num: 关键词数量
        """
        self.word_list = word_list
        self.idf_dic = idf_dic
        self.default_idf = default_idf
        self.words = words
        self.tf_dic = self.get_tf_dic()
        
        

    def get_tf_dic(self):
        """
        计算输入的文本列表所有词的tf值
        :return:
        """
        
        tf_dic = {}
        for word in self.word_list:
            tf_dic[word] = tf_dic.get(word, 0) + 1.0
        
        
        for k, v in tf_dic.items():
            tf_dic[k] = float(v) / len(self.word_list)

        return tf_dic

    def get_tfidf(self):
        """
        计算输入的文本列表所有词的tf-idf值：tf * idf
        :return: 打印前keyword_num个待提取关键词文本的提取关键词结果
        """
        tfidf_dic = {}
        for word in self.word_list:
            idf = self.idf_dic.get(word, self.default_idf)
            tf = self.tf_dic.get(word, 0.0)

            tfidf = tf * idf
            tfidf_dic[word] = tfidf
        
        tfidf_vec = []
        for word in self.words:
            if tfidf_dic.get(word,-1)!=-1:
                tfidf_vec.append(tfidf_dic[word])
            else:
                tfidf_vec.append(round(0,5))
            
        
        return tfidf_vec
                
                
    