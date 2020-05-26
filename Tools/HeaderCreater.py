def processBool(boolList,configFile):
    print(boolList)
    configFile.write('#if ')
    while boolList:
        currentItem = boolList.pop(0)
        if currentItem[0] == '!':
            configFile.write('!defined(' + currentItem[1:].strip() + ')')
        else:
            configFile.write('defined(' + currentItem.strip() + ')')
        if boolList:
            configFile.write(' ' + boolList.pop(0) + ' ')
    configFile.write('\n')



def processOption(lines,currentLine,outputFile,configFile):
    options = dict()
    options['name'] = currentLine.split(' ')[1]
    currentLine = lines.pop(0)
    options['default'] = []
    while len(currentLine.lstrip()) < len(currentLine):
        currentLine = currentLine.strip()
        tokens = currentLine.split(' ')
        if tokens[0] == 'default':
            options[tokens[0]].append(currentLine)
        else:
            options[tokens[0]] = currentLine
        currentLine = lines.pop(0)
    print(options)
    if 'bool' in options:
        outputFile.write(options['name'])
        print(currentLine)
        return currentLine
    else:
        #varType = 'string' if 'string' in options else 'int'
        numEndIf = 0
        # if 'depends' in options:
        #     processBool(options['depends'].split(' ')[2:],configFile)
        #     numEndIf += 1
        if not options['default']:
            if 'int' in options:
                configFile.write('#define ' + options['name'].strip() + ' ' + '0' + '\n')
            else:
                configFile.write('#define ' + options['name'].strip() + ' ' + '""' + '\n')
        for x in options['default']:
            x = x.strip()
            if '"' in x:
                print(x.split('"'))
                if len(x.split('"')) > 2 and x.split('"')[2]:
                    # processBool(x.split('"')[2][4:].split(' '),configFile)
                    configFile.write('#define ' + options['name'].strip() + ' ' + x[8:x.find('"',9) + 1] + '\n')
                    # configFile.write('#endif\n')
                else:
                    configFile.write('#define ' + options['name'].strip() + ' ' + x[8:] + '\n')
                    
            else:
                # if 'if' in x:
                #     processBool(x.split(' ')[2][4:].split(' '),configFile)
                configFile.write('#define ' + options['name'].strip() + ' ' + x.split(' ')[1] + '\n')
                # if 'if' in x:
                #     configFile.write('#endif\n')
            break
        
        # if numEndIf:
        #     configFile.write('#endif\n')
        
        return currentLine

def processConfig(lines):
    outputFile = open('openfeatures.txt','w+')
    configFile = open('header.h','w+')
    currentLine = lines.pop(0)
    while lines:
        while currentLine.find('choice') != 0 and currentLine.find('config') != 0 and currentLine.find('source') != 0:
            if not lines:
                return
            currentLine = lines.pop(0)
        print(currentLine)
        if currentLine.find('choice') == 0:
            currentLine = lines.pop(0)
        elif currentLine.find('config') == 0:
           currentLine = processOption(lines,currentLine,outputFile,configFile)
        else:
            sourceFile = currentLine.split(' ')[1].strip()
            sourceFile = open( sourceFile,'r')
            lines = sourceFile.readlines() + lines
            sourceFile.close()
            if(lines):
                currentLine = lines.pop(0)
    outputFile.close()
    configFile.close()



def main():
    lines = None
    with open('config/Config.in','r') as mainConfig:
        lines = mainConfig.readlines()
    processConfig(lines)

if __name__ == '__main__':
    main()
