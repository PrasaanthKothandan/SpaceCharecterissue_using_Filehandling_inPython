#This code will check whether the line is starting with a 3 digit no and not any other characters.
import os
def SpaceCharcode():
    name ="2023_Countries by Population.csv"          #enter the file name in the double quotes
    path= r"Filepath with double\\"   #enter the path where the file is in the double quotes
    os.chdir(path)
    
    #code by Prasaanth
 
    #checknonintegerrows
    file2=open(name,'r',encoding="utf8")
    
    #n=0
    faultRow=2 
    faultyRowArray = []  
    filelist2 = file2.readlines()[1:]    
    for r in filelist2:
        y=r.rstrip().split(",")[0]
        if r[0].isnumeric()!=1:
            faultyRowArray.append(faultRow)
        elif(len(y) != 3 and y.isnumeric()):
            faultyRowArray.append(faultRow)
        faultRow+=1
    #print(faultyRowArray) #Will display the error rows 
    file2.close()
    faultyArrayRowLength=len(faultyRowArray) 
    print(faultyArrayRowLength) #will display the number of error rows we have in the file
    for x in range(faultyArrayRowLength):
        
        start_line=0
        endline=faultyRowArray[faultyArrayRowLength-(x+1)]-2 #Will copy 2nd line before the error line    #code by Prasaanth

        part2startline=faultyRowArray[faultyArrayRowLength-(x+1)]-1

 
        #Copylinebyline
        file3= open(name,'r',encoding="utf8")
        list1 = file3.readlines()[0: (endline)]
        #print(list1)


 
        #concardinate_two_rows
        list2=[]
        file4= open(name,'r',encoding="utf8")  
        
        w=file4.readlines()[faultyRowArray[faultyArrayRowLength-(x+1)]-2:((faultyRowArray[faultyArrayRowLength-(x+1)]))]
        w[0]=w[0].strip("\n")
        list2.append((''.join(w)))
        #print(list2)

 
        #copy_line_below
        file5= open(name,'r',encoding="utf8")
        outputtemp=file5.readlines()[part2startline+1:]
        #print(outputtemp)    #code by Prasaanth
        #join
        joinlist=(list1+list2+outputtemp)
        #print(joinlist)
        #write in a file
        output1= open(name,"w+",encoding="utf8")
        for line1 in joinlist:
            output1.write(line1)
        output1.close()



 
if __name__=="__main__":
    
    SpaceCharcode()

