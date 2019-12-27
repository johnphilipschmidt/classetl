import os, os.path, string,sys, re


#classifications: U C S
#dissemintationControls: RS, OC OC-USGOV, IMC, NF, PR,REL,RELIDO, DSEN, FISA
#NonIcMarkings XD, ND, LES, LES-NF, SSI
#TypeOfExemptedSource XD, ND, LES, LES-NF, SSI
#FGIsourceOpen US ONLY, JOINT, Mixed US/FGI Protected, FGI Protected, Mixed US/FGI Opn, FGI Open
#ism:classification="S" ism:ownerProducer="DNK", ism:FGIsourceOpen="DNK" ism:nonICMarkings="LES" ism:typeOfExmptedSource="FGI Open"
#ism:disseminationControls="FISA" ism:nonICMarkings="LES"


def getPattern(source):
        #pattern=[['re.search("^[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]/LES",source)','A'],#CAN S//OC//NF//LES
         #        ['re.search("^[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]/FISA",source)','B'], #CAN S//OC//NF//FISA
          #       ['re.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]",source)','C'], #CAN S//OC
          #       ['re.search("^//[A-Z][A-Z][A-Z] [UCS]/[A-Z][A-Z]",source)','D'],#CAN S/OC
           #      ['re.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]",source)', 'E'],#CAN S//OC//NF
            #     ['re.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]//LES",source)','F'], #CAN S//OC//NF//LES
            #     ['re.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]/LES",source)','G'] #CAN S//OC//NF/LES
            #    ]
        #print(source)

        data = {
            'item1': ['pattern1','AA','BB'],
            'item2': ['pattern2','AA','BB']
        }

        pattern={
                #'pattern0': ['//CAN S//NC','a Pattern',{'classification':'0:3','nocitem':'4:3'}],
                'pattern0':['re.search("^[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]/LES",source)',{'classifications':'0:3','dissemintationControls':'4:5'}],#CAN S//OC//NF//LES
                'pattern1':['re.search("^[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]/FISA",source)',{'classifications':'0:3','dissemintationControls':'4:5'}], #CAN S//OC//NF//FISA
                'pattern2':['re.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]",source)',{'classifications':'0:3','dissemintationControls':'4:5'}], #CAN S//OC
                'pattern3':['re.search("^//[A-Z][A-Z][A-Z] [UCS]/[A-Z][A-Z]",source)',{'classifications':'0:3','dissemintationControls':'4:5'}],#CAN S/OC
                'pattern4':['re.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]",source)',{'classifications':'0:3','dissemintationControls':'4:5'}],#CAN S//OC//NF
                'pattern5':['re.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]//LES",source)',{'classifications':'0:3','dissemintationControls':'4:5'}], #CAN S//OC//NF//LES
                'pattern6':['re.search("^//[A-Z][A-Z][A-Z] [UCS]//[A-Z][A-Z]//[A-Z][A-Z]/LES",source)',{'classifications':'0:3','dissemintationControls':'4:5'}]#CAN S//OC//NF/LES
                 }
        for i in range(0,len(pattern)):
#for i in range(len(data)):
#    x=eval(data['pattern'+str(i)][0])
#    if ( x != None):
#        print ('pattern'+str(i)+" "+ str(x.start()))

            x=eval(pattern['pattern'+str(i)][0])
            if (x != None):
                return  x
def main():
        with open("c.dat") as file:
            for line in file:
                if(len(line) > 1):
                    if(getPattern(line) != None):
                        pattern=getPattern(line)
                        print (pattern[0])


#execute program
main()