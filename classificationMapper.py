import os, os.path, string,sys, re


#classifications: U C S
#dissemintationControls: RS, OC OC-USGOV, IMC, NF, PR,REL,RELIDO, DSEN, FISA
#NonIcMarkings XD, ND, LES, LES-NF, SSI
#TypeOfExemptedSource XD, ND, LES, LES-NF, SSI
#FGIsourceOpen US ONLY, JOINT, Mixed US/FGI Protected, FGI Protected, Mixed US/FGI Opn, FGI Open
#ism:classification="S" ism:ownerProducer="DNK", ism:FGIsourceOpen="DNK" ism:nonICMarkings="LES" ism:typeOfExmptedSource="FGI Open"
#ism:disseminationControls="FISA" ism:nonICMarkings="LES"


def getPattern(source):
        pattern=['re.search("^[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]/LES",source)', #CAN S//OC//NF//LES
                 're.search("^[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]/FISA",source)', #CAN S//OC//NF//FISA
                 're.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]",source)', #CAN S//OC
                 're.search("^//[A-Z][A-Z][A-Z] [UCS]/[A-Z][A-Z]",source)', #CAN S/OC
                 're.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]",source)', #CAN S//OC//NF
                 're.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]//LES",source)', #CAN S//OC//NF//LES
                 're.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]/LES",source)' #CAN S//OC//NF/LES
                ]
        for i in range(0,len(pattern)):
            result=eval(pattern[i])

            if (result != None):
                #print("pattern"+str(i)+":"+source)
                return result

def main():
        with open("c.dat") as file:
            for line in file:
                if(len(line) > 1):
                    if(getPattern(line) != None):
                        print (getPattern(line).start())

#execute program
main()