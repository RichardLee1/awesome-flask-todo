# encoding=utf8
##########################################################################
# 1.安装Python package
#
#   1.1 使用anaconda做包管理
#   conda install impyla
# 在运行中可能会遇到缺少thrift_sasl包的问题，用以下命令安装：
#   conda install thrift_sasl
# 如果在anaconda上找不到这个包，则可改用：
#   conda install --channel https://conda.anaconda.org/blaze thrift_sasl
#
#   1.2 使用pip做包管理
#   pip install impyla
#   pip install thrift_sasl
##########################################################################

##########################################################################
# 2.python客户端与impala交互
##########################################################################

# 2.1 连接impala
from __future__ import print_function
from impala.dbapi import connect
from impala.util import as_pandas


def run_sql(sql):
    conn = connect(host='172.17.69.25', auth_mechanism='PLAIN', port=21050, user='libingwei', password='libingwei')
    cursor = conn.cursor()
    cnt = 1

    # 2.2 对impala执行SQL查询
    if ';' in sql:
        sql_list = sql.rstrip().split(';')
        # print(type(sql_list))
        if len(sql_list[-1]):
            for s in sql_list:
                print("runing sql @ %s" % cnt)
                cursor.execute(s)
                cnt += 1
        else:
            sql_list.pop()
            for s in sql_list:
                print("runing sql @ %s" % cnt)
                cursor.execute(s)
                cnt += 1
    else:
        print("runing sql @ %s" % cnt)
        cursor.execute(sql)
    # 2.3 把结果转化成pandas的dataframe格式，以便进行数据分析
    # df = as_pandas(cursor)
    # print(df)
    return as_pandas(cursor) if cursor.description != None else 'null'


if __name__ == '__main__':
    sql = '''select * from ods.appuserecord limit 10;'''
    df = run_sql(sql)
    print(df)
