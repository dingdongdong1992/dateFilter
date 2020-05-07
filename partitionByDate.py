import sys,time,os,json,datetime,operator

#SELECT * FROM cddata WHERE Date > 2019-01-01 and Date < 2019-01-20
partdir = 'partitioned/'
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
            #print(payload['received'])
            partfn = payload['received'].split('T')[0].replace('-','_')

            #print(partfn)
            fout = open(partdir+partfn+'.txt','a') #file append mode
            fout.write(json.dumps(payload)+'\n')
            fout.close()
        f_2.close()
