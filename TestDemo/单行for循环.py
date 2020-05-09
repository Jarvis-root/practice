

# 列表套列表：
datas1 = [['hhh', i, d] for i in range(10) for d in range(5)]  # 单行多个for相当于for循环嵌套
print(datas1)

# 列表套元祖
datas2 = [('hhh', i, d) for i in range(10) for d in range(5)]  # 单行多个for相当于for循环嵌套
print(datas2)

# 如果元祖套列表或元祖，就变成了生成器
datas = (['hhh', str(i), d] for i in range(10) for d in range(5))
print(next(datas))
print(datas.__next__())
print(datas.__next__())
print(datas.close())

l = [i for i in range(10)]  # 创建列表
print(l)
