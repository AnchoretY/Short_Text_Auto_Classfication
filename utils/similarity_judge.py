import math
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
    
# def get_result(input_data):
#     """
#         相似度最高的归为一类
#     """
#     tmp_dict = {}
#     type_index = 0
    
#     for i in input_data:
#         if tmp_dict.get(i[0],-1)==-1 and tmp_dict.get(i[1],-1)==-1:
#             tmp_dict[i[0]] = type_index
#             tmp_dict[i[1]] = type_index
#             type_index += 1
#         elif tmp_dict.get(i[0],-1)==-1 and tmp_dict.get(i[1],-1)!=-1:
#             tmp_dict[i[0]] = tmp_dict[i[1]]
#         elif tmp_dict.get(i[0],-1)!=-1 and tmp_dict.get(i[1],-1)==-1:
#             tmp_dict[i[1]] = tmp_dict[i[0]]
#     return tmp_dict
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



#get_max_sim(get_sim(tfidf_vec))