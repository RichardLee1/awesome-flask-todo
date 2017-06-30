# -*- coding:utf-8 -*-

sql_sale_amount = '''
select substr(t1.starttime,1,10) as sale_date
        ,sum(funding) as sale_amount
from ods.financialproducts as t1
inner join
ods_v.userdetails as t2
on t1.middleuserid = t2.userid
where t1.starttime>="2017-06-01"
    and lower(t2.username) like 'rainbow%'
group by 1
'''
