import os
import pathlib

def main(directoryName,parentDirectory):
    for x in os.listdir(os.path.join(parentDirectory,directoryName)):
        if os.path.isdir(os.path.join(parentDirectory,directoryName,x)):
            main(x,os.path.join(parentDirectory,directoryName))
        # elif x[-2:] != '.c' and x != 'findCFiles.py':
        #         os.remove(pathlib.Path(parentDirectory,directoryName,x))
        elif x[-2:] == '.c':
            results = os.path.join(parentDirectory,directoryName,x)
            if results[0] == '.':
                results = results[2:-2]
            else:
                results = results[:-2]
            print(results)
        elif x[-2:] == '.h':
            results = os.path.join(parentDirectory,directoryName,x)
            if results[0] == '.':
                results = results[2:-2]
            else:
                results = results [:-2]
            try:
                index = results.rindex('/')
            except:
                index = len(results)
            results = results[:index]
            with open('headerLocations.txt','a+') as header:
                header.write(results + '\n')

main('.','')
