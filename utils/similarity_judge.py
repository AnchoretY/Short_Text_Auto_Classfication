import math

"""
    update 20190428  加入merge_sim_type
"""


def cos_sim(vector_a, vector_b):
    """
    计算两个向量之间的余弦相似度
    :param vector_a: 向量 a 
    :param vector_b: 向量 b
    :return: sim
    """
    num = 0.0
    denom = 0.0
    tmp1 = 0.0
    tmp2 = 0.0
    for i in range(len(vector_a)):
        num = num+vector_a[i]*vector_b[i]
        tmp1 = vector_a[i]*vector_a[i]+tmp1
        tmp2 = vector_b[i]*vector_b[i]+tmp2
        
    denom = math.sqrt(tmp1)*math.sqrt(tmp2)
    cos_sim = float(num) / denom
    return cos_sim



def get_sim(input_data):
    """
        获得文本之间的相似度
    """
    result = []
    for i in input_data:
        tmp = []
        for j in input_data:
            tmp.append(cos_sim(i,j))
        result.append(tmp)
    return result

def get_max_sim(input_data):
    result = []
    
    for i,data in enumerate(input_data):
        max_sim = 0
        max_sim_index = 0
        for j,sim in enumerate(data):
            if i!=j:
                if sim>=max_sim:
                    max_sim = sim
                    max_sim_index = j
        result.append((i,max_sim_index,max_sim))
    return result
    
def get_result(input_data,threshold=0.01):
            tmp_dict = {}
            type_index = 0

            for i in input_data:
                if i[2]>=threshold:
                    if tmp_dict.get(i[0],-1)==-1 and tmp_dict.get(i[1],-1)==-1:
                        tmp_dict[i[0]] = type_index
                        tmp_dict[i[1]] = type_index
                        type_index += 1
                    elif tmp_dict.get(i[0],-1)==-1 and tmp_dict.get(i[1],-1)!=-1:
                        tmp_dict[i[0]] = tmp_dict[i[1]]
                    elif tmp_dict.get(i[0],-1)!=-1 and tmp_dict.get(i[1],-1)==-1:
                        tmp_dict[i[1]] = tmp_dict[i[0]]
                else:
                    tmp_dict[i[0]] = type_index
                    type_index += 1
            return tmp_dict
        
        
#============================================
#            20190428
#============================================

def vec_sum(vector_a,vector_b):
    """
        向量和计算
    """
    result = []
    for i in range(len(vector_a)):
        result.append(vector_a[i]+vector_b[i])
    return result

def vec_divsion(vector,n):
    """
        向量除以一个数
    """

    result = []
    for i in vector:
        result.append(i/n)
    return result

    

def merge_sim_type(res,tfidf_vec,threshold=0.01):
    """
        param res:原始个文章对应的各个类列表
        param res:各个文章的tf_idf的向量化形式
        param threshold:类间合并的阈值，如果两个类间余弦距离小于这个值，那么将两个类进行合并
    """
    type_nums = len(set(res))

    type_dict = {}
    for index,type_num in enumerate(res):
        if type_dict.get(type_num,-1)==-1:
            type_dict[type_num] = [index]
        else:
            type_dict[type_num].append(index)
    center_vec_list = []

    for l in type_dict:
        sum_vec = tfidf_vec[type_dict[l][0]]
        for i in range(1,len(type_dict[l])):
            sum_vec = vec_sum(sum_vec,tfidf_vec[type_dict[l][i]])
        center_vec = vec_divsion(sum_vec,len(type_dict[l]))
        center_vec_list.append(center_vec)



    tmp_dict = dict(sorted(get_result(get_max_sim(get_sim(center_vec_list)),threshold).items(),key=lambda x:x[0]) )
    result = []
    for i in res:
        result.append(tmp_dict[i])
    return result
