'''
Created on 2011-9-24

ARG1: FILE NAME
ARG2: YEAR
ARG3: MONTH

SAMPLE: d:\dp21 2011 SEP

USAGE: JIE XI BAO GAO

@author: caspar32
'''
import sys

initialDay=17 
endDay=21 
startTime=20
endTime=05
specialBeginDay=20
specialEndDay=21

if __name__ == '__main__':
    fileName=sys.argv[1] 
    year=sys.argv[2]
    month=sys.argv[3]
    date=month+" "+year
    while(initialDay<=endDay):
        inputFile = open(fileName,'r')
        for lineContent in inputFile:         
            if (lineContent.find(date)!=-1):           
                tmpDate=str(initialDay)+" "+date
                if(lineContent.find(tmpDate)!=-1):
                    outputFileName=inputFile.name+'-'+str(month)+'-'+str(initialDay)
                    outputFile=open(outputFileName,'w')
                    outputFile.write(lineContent)
                    newLineContent=inputFile.next()
                    judgeDate=str(initialDay+1)+' '+date
                    count=0
                    while (newLineContent.find(judgeDate)==-1):
                        outputFile.write(newLineContent)
                        if(newLineContent.find('FULL ARCHIVE LOG')!=-1):
                            count=count+1
                        newLineContent=inputFile.next()
                    print count           
        inputFile.close()
        outputFile.close()
        initialDay=initialDay+1;
        
    inputFile1 = open(fileName,'r')
    
    for lineContent in inputFile1:  
        tmpDate=str(specialBeginDay)+" "+date
        if(lineContent.find(tmpDate)!=-1):
            while (lineContent[1:3]<str(startTime)):
                lineContent=inputFile1.next()
            else:
                outputFileName=inputFile1.name+'-'+str(month)+'-special'
                outputFile1=open(outputFileName,'w')
                tmpDate1=str(specialEndDay)+" "+date
                newLineContent=lineContent
                count=0
                while(newLineContent.find(tmpDate1)==-1):  
                    outputFile1.write(newLineContent)
                    if(newLineContent.find('FULL ARCHIVE LOG')!=-1):
                            count=count+1 
                    newLineContent=inputFile1.next()
                while (newLineContent[2:3]<str(endTime)):
                    outputFile1.write(newLineContent)
                    if(newLineContent.find('FULL ARCHIVE LOG')!=-1):
                            count=count+1
                    newLineContent=inputFile1.next()
                print count
            outputFile1.close()
            
