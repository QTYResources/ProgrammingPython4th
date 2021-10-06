import pickle

dbfile = open('people-pickle', 'rb')    # 使用 3.x 的二进制模式文件
db = pickle.load(dbfile)
for key in db:
    print(key, '=>\n', db[key])

print(db['sue']['name'])