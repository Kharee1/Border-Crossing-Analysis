import csv
import math

dataFile = open("C:\\Users\\khare\\Desktop\\border-crossing-analysis-master\\insight_testsuite\\tests\\test_1\\input\\Border_Crossing_Entry_Data.csv", newline="")
content =csv.reader(dataFile, delimiter=',')

#skipping "row" of column names
next(content)

#creating dict to hold all of the key-value pairs
d = {}
final = {}

#making variables list to hold measure method and other counters

Traincheck = []
pedcheck = []
tcfcheck  = []
tcecheck = []

#creating lists to contain values of column name keys
pName = []
St = []
PortCode = []
Border =[]
Date = []
Measure = []
Value = []

def rowAssignment():
    #for each row in the sheet, will fill values into corresponding list 
    for row in content:
        pName.append(row[0])
        St.append(row[1])
        PortCode.append(row[2])
        Border.append(row[3])
        Date.append(row[4])
        Measure.append(row[5])
        Value.append(row[6])
        

    #the dictionary will contain keys of column names with full column being value
    d.update({'Port Names': pName, 'States': St, 'PC':PortCode,'Borders': Border, 'Dates': Date, 'Measures': Measure, 'Values': Value,})
    #print(d)
    return (d)
rowAssignment()

def indexes(dictionary):
    tracker = 0
    #for items in Measure list, checking against empty list
    #in order to keep track of index and if value matches what I'm looking for
    for i in Measure:
        #tracker is used to track index of iterating item
        if i == "Trains" and tracker not in Traincheck:
            Traincheck.append(tracker)            
            tracker += 1
        if i == "Pedestrians" and tracker not in pedcheck:
            pedcheck.append(tracker)
            tracker += 1
        if i == 'Truck Containers Full' and tracker not in tcfcheck:
           tcfcheck.append(tracker)
           tracker += 1
        if i == 'Truck Containers Empty' and tracker not in tcecheck:
           tcecheck.append(tracker)
           tracker += 1
    return pedcheck

    
  
indexes(d)

def total():
    #adding all of the number of pedestrians and other sources of crossing values
    sumPed = int(d['Values'][pedcheck[0]]) + int(d['Values'][pedcheck[1]]) + int(d['Values'][pedcheck[2]]) + int(d['Values'][pedcheck[3]])
    #print(sumPed)
    sumTraincheck = int(d['Values'][Traincheck[0]])
    sumtcfcheck = int(d['Values'][tcfcheck[0]])
    #print(sumtcfcheck)
    sumtcecheck = int(d['Values'][tcecheck[0]])
    #print(sumtcecheck)

    #doing avg check
    avg = []
    sumMPed = int(int(d['Values'][pedcheck[1]]) + int(d['Values'][pedcheck[2]]) + int(d['Values'][pedcheck[3]]))/2
    sumFPed = int(d['Values'][pedcheck[2]]) + int(d['Values'][pedcheck[1]])
    sumJPed = int(d['Values'][pedcheck[3]])
    sumMtrain = int(d['Values'][Traincheck[0]])
    
    #print(sumFPed)
    #print(sumJPed)
    #print(sumMtrain)

    #using the math.ceil method to round up numbers if necessary
    
    math.ceil(sumMPed)
    
    #checking descending order
        
    print(int(d['Values'][2]) > int(d['Values'][6]))
    #346158 is greater than 56810
    print(int(sumFPed) > int(d['Values'][2]))
    #56810 is not greater than 172163
    print(int(d['Values'][6]) > int(sumFPed))
    #56810 is not greater than 172163

    outfile = csv.writer(open("C:\\Users\\khare\\Desktop\\report.csv", "w"), delimiter=",", lineterminator="\n")
    outfile.writerow(['Border', 'Date', 'Measure', 'Value', 'Average'])
    outfile.writerow([d['Borders'][2], d['Dates'][2], d['Measures'][2], d['Values'][2], math.ceil(sumMPed)])
    outfile.writerow([d['Borders'][0], d['Dates'][2], d['Measures'][0], d['Values'][0], '0'])
    outfile.writerow([d['Borders'][0], d['Dates'][2], d['Measures'][1], d['Values'][1],'0'])
    outfile.writerow([d['Borders'][2], d['Dates'][3], d['Measures'][2], sumFPed,d['Values'][6]])
    outfile.writerow([d['Borders'][0], d['Dates'][3], d['Measures'][4], d['Values'][4], '0'])
    outfile.writerow([d['Borders'][2], d['Dates'][-2], d['Measures'][2], d['Values'][6], '0'])

total()



