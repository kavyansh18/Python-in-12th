import pickle
with open('data.dat','rb+') as f:
    try:
        while True:
            record=pickle.load(f)
            if record[0]==397:
                cp=f.tell()
                break
        record[2]=100
        f.seek(cp)
        pickle.dump(record,f)
    except:
        pass
print('done')
