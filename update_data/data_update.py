# -*- coding:utf-8 -*-
from __future__ import print_function
import time
import datetime
import traceback
import pandas as pd
from impala_py import run_sql
from sql import *
import logging
import logging.handlers

# 设置日志文件
LOG_FILE = 'update_data.log'
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt)  # 实例化formatter
handler.setFormatter(formatter)  # 为handler添加formatter
logger = logging.getLogger('drools_test')  # 获取名为tst的logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.DEBUG)

cycle_count = 0
sql_pool = [sql_reg_cnt]

file_name = ['reg_cnt']

while True:
    cycle_count += 1
    print('== 重新开始第', cycle_count, '个轮回。佛曰：阿弥陀佛 @', datetime.datetime.now(), '==')
    day = datetime.datetime.today().weekday()
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    # t = pd.to_datetime('2016-02-07')
    # if datetime.datetime.now() < t and 8 <= hour < 18:
    if 0 <= day <= 6 and 7 <= hour <= 9:
        print('== 现在是营业时间，欢迎光临 ==')
        for sql, name in zip(sql_pool, file_name):
            try:
                # print('Reading sql %s' % name)
                logger.info('Reading sql %s: ' % name)
                df = run_sql(sql)
                if 'date' in df.columns:
                    df.sort_values('date', ascending=False, inplace=True)
                df.to_csv('./database/%s.csv' % name, index=False, encoding='utf-8')
                # print('Sql %s read success, Rows:%s' % (name, df.shape[0]))
                logger.info('Reading sql success %s: ' % name)
            except Exception, e:
                traceback.print_exc()
                print('ERROR. Get the data %s failed' % name)
                logger.debug(name, e)
                # time.sleep(10*60)
        print('== 上面执行完了 @', datetime.datetime.now(), ' ==')
        # time.sleep(24*60*60)
        if hour == 10:

            time.sleep(23 * 60 * 60)
        else:
            time.sleep(12 * 60 * 60)
    else:
        print('== 这位客官，本店已经打烊，请稍侯再来 ==')
        time.sleep(60 * 60)
        #  time.sleep(18000)
