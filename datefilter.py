import sys,time,os,json,datetime,operator

#SELECT * FROM cddata WHERE Date > 2019-01-01 and Date < 2019-01-20
new_file = ''
for root,dirs, files in os.walk('data'):
    #print(root,dirs,files)
    path = root.split(os.sep)
    for fn in files:
        fp = root+os.sep+fn
        #print(fp)
        f_2 = open(fp, 'r')
        for line in f_2:
            data = json.loads(line)
            payload = data['payload']
            payload = json.loads(payload)
#            print(payload['received'])
            k = payload['received'].split('T')[0]
            #print (k)
            if k > '2019-01-01' and k < '2019-01-20':
                new_file += line


with open('output.txt','wt') as w:
    w.write(new_file)
