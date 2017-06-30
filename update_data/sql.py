# -*- coding:utf-8 -*-

sql_reg_cnt = '''
select substr(t1.starttime,1,10)
        ,sum(funding)
from ods.financialproducts as t1
inner join
ods_v.userdetails as t2
on t1.middleuserid = t2.userid
where t1.starttime>="2017-06-01"
    and lower(t2.username) like 'rainbow%'
'''
