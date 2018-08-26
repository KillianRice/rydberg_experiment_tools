import os
import datetime
import shutil

#get date and create timestamps
dateWithPeriods = datetime.datetime.today().strftime('%Y.%m.%d')
dateWithoutPeriods = datetime.datetime.today().strftime('%Y%m%d')

#ask for base name and isotope
baseName = raw_input('Enter base name: ')
isotope = raw_input('Enter Isotope: ')
while isotope not in ['84','86','87','88']:
    isotope = raw_input('Please select valid isotope: ')

#base fold should be wherever you are storing your data
baseFolder = 'C:\\Users\\Rydberg\\Documents\\Data'

#change to the base folder
os.chdir(baseFolder)

#verify that there is a folder for the isotope you selected, if not
#make one
try:
    os.chdir(baseFolder+'\\Analysis\\'+isotope+'Sr')
    os.chdir(baseFolder+'\\Raw_Data\\'+isotope+'Sr')
except:
    os.mkdir(baseFolder+'\\Analysis\\'+isotope+'Sr')
    os.mkdir(baseFolder+'\\Raw_Data\\'+isotope+'Sr')

analysisFolder = baseFolder+'\\Analysis\\'+isotope+'Sr'
dataFolder = baseFolder+'\\Raw_Data\\'+isotope+'Sr'

#create the directories that will contain the data and analysis
os.mkdir(analysisFolder+'\\'+baseName+dateWithPeriods)
os.mkdir(dataFolder+'\\'+dateWithPeriods)

todayAnalysisFolder = analysisFolder+'\\'+baseName+dateWithPeriods
todayDataFolder = dataFolder+'\\'+dateWithPeriods

#create the master batch files
f = open(todayDataFolder+'\\Files_'+dateWithoutPeriods+'.txt','w')
f.close()
f = open(todayDataFolder+'\\Files_'+dateWithoutPeriods+'_Bg.txt','w')
f.close()
f = open(todayDataFolder+'\\Files_'+dateWithoutPeriods+'_Counts.txt','w')
f.close()
