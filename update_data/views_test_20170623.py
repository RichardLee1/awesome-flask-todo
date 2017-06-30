# -*-coding:utf-8 -*-
from flask import render_template
from pandas_highcharts.core import serialize
from app import app
import os
import pandas as pd
# from model import *


@app.route('/')
def index():
    return render_template('index.html')

# 无需修改
# a-01
@app.route('/monitor/register/count')
def register_cnt():
    return render_template('sale_amout_test_20170627.html')


@app.route('/monitor/register/count/figure')
def register_cnt_figure():
    # 读取csv数据
    df = pd.read_csv(os.getcwd() + '/update_data/database/sql_sale_amout.csv', nrows=60)
    # 小数转换为百分比，是否需要
    # for a, b in zip(['total', 'android', 'ios'], ['credit_cnt_total', 'credit_cnt_android', 'credit_cnt_ios']):
    #    df[a + '_rate'] = (df[b] / df[a] * 100).apply(lambda x: format(x, ".4")).astype(
    #    float)
    # 设置图表
    chart = serialize(
        df[['sale_date', 'sale_amout']].head(30).sort_values('sale_date').rename(
            columns={'sale_date': '销售日期'}),
        output_type='json',
        x='销售日期', title=u'彩虹计划销售量', first_y_type='column')

    # chart1 = serialize(
    #    df[['date', 'total_rate', 'android_rate', 'ios_rate']].head(30).sort_values('date').rename(
    #        columns={'date': '注册日期', 'total_rate': 'total', 'android_rate': 'android', 'ios_rate': 'ios'
    #                 }),
    #    output_type='json',
    #    x='注册日期', title=u'app每日戳额率', first_y_type='line', tooltip={'valueSuffix': '%'}, ytitle="percentage")
    # return render_template('a01_reg_cnt_figure.html', chart=chart, chart1=chart1)
