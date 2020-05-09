import pandas as pd


# 读取excel并合并两个excel，实现类似vlookup
def v_lookup(name: str, excel_to_merge, excel_to_be_merged):
    """

    :param name:
    :param excel_to_merge:
    :param excel_to_be_merged:
    """
    excel_to_merge = pd.read_excel(excel_to_merge)
    excel_to_be_merged = pd.read_excel(excel_to_be_merged)
    re = pd.merge(excel_to_be_merged, excel_to_merge[['学号', '成绩']], on='学号')
    print(re)


v_lookup('学号', 'D:/PycharmProjects/1.xlsx', 'D:/PycharmProjects/2.xlsx')
