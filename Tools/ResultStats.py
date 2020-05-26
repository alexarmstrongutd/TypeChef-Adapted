import json
import sys

mapping = dict()
mapping["Cfg innnvoid function"] = "Undef_Behavior"
mapping["Uninitialized memory"] = "Uninitialized_Val"
mapping["Dead store"] = "Dead_Store"
mapping["Xfree"] = "Memory_Error"
mapping["Double free"] = "Memory_Error"


def createDict():
    featuresDict = dict()
    featuresDict["Dead store"] = {}
    featuresDict["Uninitialized memory"] = {}
    featuresDict["Case termination"] = {}
    featuresDict["Check stdlibfunc return"] = {}
    featuresDict["Cfg innnvoid function"] = {}
    featuresDict["Xfree"] = {}
    featuresDict["Double free"] = {}
    featuresDict["Dangling Switch"] = {}
    for item in featuresDict:
        featuresDict[item]['num-variability'] = 0
        featuresDict[item]['num-generic'] = 0
    return featuresDict

def createMappedDict():
    mappedDict = dict()
    mappedDict["Dead_Store"] = {}
    mappedDict["Uninitialized_Val"] = {}
    mappedDict["Undef_Behavior"] = {}
    mappedDict["Memory_Error"] = {}
    for item in mappedDict:
        mappedDict[item]['num-variability'] = 0
        mappedDict[item]['num-generic'] = 0
    return mappedDict

def convertFeaturesToTuple(features):
    sortedFeatures = sorted(features)
    return tuple(sortedFeatures)

def createSet(jsonDictList):

    result = set()
    for x in jsonDictList:
        result.add((x['filename'],x['line'],convertFeaturesToTuple(x['automatic_features']),x['type']))
    return result

def printStat(key,features,numErrors,numVariability):
    print(key + " info")
    print('\tVariability warnings: {}'.format(features[key]['num-variability']))
    print('\tGeneric warnings: {}'.format(features[key]['num-generic']))
    print('\t% of total variability warnings: {}%'.format(round(features[key]['num-variability']/numVariability * 100,2)))
    print('\t% of total generic warnings: {}%'.format(round(features[key]['num-generic']/(numErrors-numVariability) * 100,2)))
    print('\t% of all warnings: {}%'.format(round((features[key]['num-generic']+features[key]['num-variability'])/numErrors * 100,2)))
    print()


def main():
    with open(sys.argv[1],'r') as fileDict:
        featuresArray = json.load(fileDict)
        featuresSet = createSet(featuresArray)
        featuresDict = createDict()
        mappedDict = createMappedDict()
        featuresSet = list(featuresSet)
        numVariability = 0
        for x in featuresSet:
            if "True" not in x[2]:
                numVariability += 1
                featuresDict[x[3].strip()]['num-variability'] += 1
            else:
                featuresDict[x[3].strip()]['num-generic'] += 1
        print("TypeChef-Stats\n")
        for x in featuresDict:
            printStat(x,featuresDict,len(featuresSet),numVariability)
        mappedWarnings = ["Cfg innnvoid function","Uninitialized memory","Dead store","Xfree","Double free"]
        for x in mapping:
            mappedDict[mapping[x]]['num-variability'] += featuresDict[x]['num-variability']
            mappedDict[mapping[x]]['num-generic'] += featuresDict[x]['num-generic']
        print("---------------------------")
        print("\n\nMapped Stats\n")
        for x in mappedDict:
            printStat(x,mappedDict,len(featuresSet),numVariability)
        print("---------------------------")
        print("\n\nFinal totals\n")
        print("Total number of variability warnings: {}".format(numVariability))
        print("Total number of generic warnings: {}".format(len(featuresSet)-numVariability))
        print("Total number of warnings: {}".format(len(featuresSet)))

main()
