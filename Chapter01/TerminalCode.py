#!/usr/bin/python3

import pprint

bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']

bob[0], sue[2]  # 获取姓名，薪水
# ('Bob Smith', 40000)

bob[0].split()[-1]  # Bob 姓什么？
# 'Smith'

sue[2] *= 1.25  # 给 sue 加薪 25%
# ['Sue Jones', 45, 50000.0, 'hardware']

people = [bob, sue] # 引用列表的列表

for person in people:
    print(person)

people[1][0]

for person in people:
    print(person[0].split()[-1])    # 打印姓氏
    person[2] *= 1.20   # 涨 20% 的薪水

for person in people: print(person[2])  # 检查新的薪酬

pays = [person[2] for person in people]	# 收集薪酬信息
print(pays)

pays = map((lambda x: x[2]), people)	# 同上（map 是 3.x 中的生成器）
pays = list(pays)
print(pays)

pay_sum = sum(person[2] for person in people)
print(pay_sum)

people.append(['Tom', 50, 0, None])
print(len(people))
print(people[-1][0])

NAME, AGE, PAY = range(3)   # 0, 1 和 2
bob = ['Bob Smith', 42, 10000] 
print(bob[NAME])
print(f"{PAY}, {bob[PAY]}")

bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]

for person in people:  
    print(person[0][1], person[2][1]) # name, pay

names = [person[0][1] for person in people] # 收集姓名
print(names)

for person in people:
    print(person[0][1].split()[-1]) # 获得姓
    person[2][1] *= 1.10    # 加 10% 的工资

for person in people: print(person[2])

for person in people:
    for (name, value) in person:   
        if name == 'name': print(value) # 寻找特定的字段

def field(record, label):
    for (fname, fvalue) in record:  # 根据名字寻找字段
        if fname == label:
            return fvalue

print(field(bob, 'name'))
print(field(sue, 'pay'))

for rec in people:
    print(field(rec, 'age'))    # 打印所有年龄


bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

print(bob['name'], sue['pay'])  # 既没有 bob[0] 也没有 sue[2]

print(bob['name'].split()[-1])  

sue['pay'] *= 1.0
print(sue['pay'])

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(bob)
print(sue)

sue = {}
sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['pay'] = 40000
sue['job'] = 'hdw'
print(sue)

names = ['name', 'age', 'pay', 'job']
values = ['Sue Jones', 45, 40000, 'hdw']
print(list(zip(names, values)))
sue = dict(zip(names, values))
print(sue)

fields = ('name', 'age', 'job', 'pay')
record = dict.fromkeys(fields, '?')
print(record)

print(bob)
print(sue)

people = [bob, sue] # 引用列表
for person in people:   
    print(person['name'], person['pay'], sep=',')   # 所有的名字和薪水

for person in people:
    if person['name'] == 'Sue Jones':   # 获取 sue 的薪水
        print(person['pay'])

names = [person['name'] for person in people]   # 收集姓名
print(names)

names = list(map((lambda x: x['name']), people))  # 同上，生成式
print(names)

pay_sum = sum(person['pay'] for person in people)   # 汇总薪水
print(pay_sum)

names = [rec['name'] for rec in people if rec['age'] >= 45] # 类似 SQL 查询
print(names)

ages = [(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people]
print(ages)

G = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(G))

G = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(G.__next__())

for person in people:
    print(person['name'].split()[-1])   # 姓
    person['pay'] *= 1.10

for person in people: print(person['pay'])

bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'age': 42,
        'job': ['sofware', 'writing'],
        'pay': (40000, 50000)}

print(bob2['name']) # bob 的全名
print(bob2['name']['last']) # bob 的姓氏
print(bob2['pay'][1])   # bob 的最高薪资

for job in bob2['job']: print(job)  # bob 的所有工作

print(bob2['job'][-1])  # bob 最近的工作
print(bob2['job'].append('janitor'))    # bob 得到一个新工作
print(bob2)

bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
print(bob)

db = {}
db['bob'] = bob # 引用字典的字典
db['sue'] = sue
print(db['bob']['name'])    # 获取 bob 的名字
db['sue']['pay'] = 50000 # 改变 sue 的薪水
print(db['sue']['pay']) # 获取 sue 的薪水

pprint.pprint(db)

for key in db:
    print(key, '=>', db[key]['name'])

for key in db:
    print(key, '=>', db[key]['pay'])

for key in db:
    print(db[key]['name'].split()[-1])
    db[key]['pay'] *= 1.10

for record in db.values(): print(record['pay'])

db['tom'] = dict(name='Tom', age=50, job=None, pay=0)
print(db['tom'])
print(db['tom']['name'])
print(list(db.keys()))
print(len(db))
print([rec['age'] for rec in db.values()])
print([rec['name'] for rec in db.values() if rec['age'] >= 45])