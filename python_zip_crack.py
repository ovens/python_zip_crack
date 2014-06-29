#code=utf-8

import zipfile
import optparse
from threading import Thread
def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Found password  is ' + password +'\n'
    except:
        pass
def main():
    parser = optparse.OptionParser("usage%prog" + "-f <zipfile> -d <dictionary>")   
    parser.add_option('-f',dest = 'zName',type = 'string',help='specify zip file')
    parser.add_option('-d',dest= 'dName',type='string',help='specify dictionary file ')
    (options,args)=parser.parse_args()
    if (options.zName == None) | (options.dName == None):  
        print parser.usage
        exit(0)
    else:
        zName = options.zName
        dName = option.dName
    zFile = zipfile.ZipFile(zName)
    passFile = open(dName)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile,args=(zFile,password))
        t.start()
if __name__=='__main__':
    main()