import os, os.path, string,sys, re
# J. Philip Schmidt Dec 23, 2019
# Classification conversion utility based upon a portion marking to convert to XMLattributes
# Uses  a map of Regex with the associated substr ranges in a map for dynamic processing from a csv text file.


#classifications: U C S
#'ism:disseminationControls: RS, OC OC-USGOV, IMC, NF, PR,REL,RELIDO, DSEN, FISA
#NonIcMarkings XD, ND, LES, LES-NF, SSI
#ism:TypeOfExemptedSource XD, ND, LES, LES-NF, SSI
#ism:FGIsourceOpen US ONLY, JOINT, Mixed US/FGI Protected, FGI Protected, Mixed US/FGI Opn, FGI Open
#ism:classification="S" ism:ownerProducer="DNK", ism:ism:FGIsourceOpen="DNK" ism:nonICMarkings="LES" ism:typeOfExmptedSource="FGI Open"
#ism:disseminationControls="FISA" ism:nonICMarkings="LES"

#match the pattern and return the parsing map
def getPattern(source,pattern):
    for i in range(0,len(pattern)):
            x=eval(pattern['pattern'+str(i)][0])
            if (x != None):
                return  'pattern'+str(i)


def parsePattern(pattern,patternMatch,source):
    #define the output map
    outPutMap={}
    # get the element dict for the pattern that matched
    attributeMap=eval(str(pattern[str(patternMatch)][1]))

    #Iterate throught  thekeys to get the substring definition
    for elementName in attributeMap.keys():
        #attribute map is a list of two values(start and end)
        attKey=(attributeMap[elementName])
        #Get the subtring value fromthe matched pattern in source
        matchedPattern=source[attKey[0]:attKey[1]]
        outPutMap[elementName]=matchedPattern

    return outPutMap




def main():
    #The Masterm map
    # mapkey, regex pattern to search for dynamic eval execution, attribute map of substring parse range
    patternMap={
        'pattern0':['re.search("^[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]/LES$",source)',{'ism:classifications':[4,5],'ism:disseminationControls':[7,9],'ism:FGIsourceOpen':[14,17]},'CAN S//OC '], #CAN S//OC//NF//LES
        'pattern1':['re.search("^[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]/FISA$",source)',{'ism:classifications':[4,5],'ism:disseminationControls':[8,9],'ism:TypeOfExemptedSource':[10,12],'ism:FGIsourceOpen':[16,19]},'1'], #CAN S//OC//NF//FISA
        'pattern2':['re.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]$",source)',{'ism:classifications':[6,7],'ism:disseminationControls':[9,11],'ism:TypeOfExemptedSource':[10,12],'ism:FGIsourceOpen':[16,19]},'2'], #CAN S//OC
        'pattern3':['re.search("^//[A-Z][A-Z][A-Z] [UCS]/[A-Z][A-Z]$",source)',{'ism:classifications':[6,7],'ism:disseminationControls':[7,9],'ism:TypeOfExemptedSource':[10,12],'ism:FGIsourceOpen':[14,15]},'3'],#CAN S/OC
        'pattern4':['re.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]$",source)',{'ism:classifications':[6,7],'ism:disseminationControls':[4,5],'ism:TypeOfExemptedSource':[10,12],'ism:FGIsourceOpen':[12,13]},'4'],#CAN S//OC//NF
        'pattern5':['re.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]//LES$",source)',{'ism:classifications':[6,7],'ism:disseminationControls':[4,5],'ism:TypeOfExemptedSource':[10,12],'ism:FGIsourceOpen':[12,13]},'5'], #CAN S//OC//NF//LES
        'pattern6':['re.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]/LES$",source)',{'ism:classifications':[6,7],'ism:disseminationControls':[4,5],'ism:TypeOfExemptedSource':[10,12],'ism:FGIsourceOpen':[12,13]},'6']#CAN S//OC//NF/LES
    }
    with open("c.dat") as file:
        result={}

        for line in file:
            if(len(line) > 1):
                #split the line by comma 0=ClassString, 2 fd930id,3=columnName
                lineElements=line.split(',')


                #get the pattern key
                patternMatch=getPattern(lineElements[0],patternMap)
                if ((patternMatch) != None):
                    #print ("pattern key is:"+patternMatch)
                    result[patternMatch+'-'+lineElements[0]+') ('+lineElements[2]+') ='+lineElements[2]]=parsePattern(patternMap,patternMatch,lineElements[0])

        for key in result:
                print ((key.lstrip('\''),(result[key])))



#execute program
main()