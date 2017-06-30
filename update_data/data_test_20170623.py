# -*- coding:utf-8 -*-
from __future__ import print_function
from impala_py import run_sql
import traceback
from sql_test_20170623 import *

sql = '''

'''
# sql 文件中sql的变量名字
sql_pool = [sql_sale_amount
            ]

# 保存csv数据的文件名字
file_name = ['sql_sale_amount']


for sql, name in zip(sql_pool, file_name):
    try:

        df = run_sql(sql)
        if 'date' in df.columns:
            df.sort_values('date', ascending=False, inplace=True)
        df.to_csv('./database/%s.csv' % name, index=False, encoding='utf-8')
        print('Sql %s read success, Rows:%s' % (name, df.shape[0]))
        # logger.info('Reading sql success %s: ' % name)
    except Exception, e:
        traceback.print_exc()
        print('ERROR. Get the data %s failed' % name)

print('save success')
