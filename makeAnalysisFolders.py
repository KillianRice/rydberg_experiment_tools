import os
import datetime
import shutil

#get date and create timestamps
dateWithPeriods = datetime.datetime.today().strftime('%Y.%m.%d')
dateWithoutPeriods = datetime.datetime.today().strftime('%Y%m%d')

#ask for base name and isotope
baseName = input('Enter base name: ')
isotope = input('Enter Isotope: ')
while isotope not in ['84','86','87','88']:
    isotope = input('Please select valid isotope: ')

#base folder should be wherever you are storing your data
baseFolder = 'E:\\Data\\'
path_to_notepad = '"C:\\Program Files (x86)\\Notepad++\\notepad++.exe"'
repository_url = 'https://github.com/KillianRice/rydberg_analysis.git'

#change to the base folder
os.chdir(baseFolder)

#verify that there is a folder for the isotope you selected, if not
#make one
try:
    os.chdir(baseFolder+'\\Analysis\\'+isotope+'Sr')
except:
    os.mkdir(baseFolder+'\\Analysis\\'+isotope+'Sr')

try:
    os.chdir(baseFolder+'\\Raw_Data\\'+isotope+'Sr')
except:
    os.mkdir(baseFolder+'\\Raw_Data\\'+isotope+'Sr')

analysisFolder = baseFolder+'\\Analysis\\'+isotope+'Sr'
dataFolder = baseFolder+'\\Raw_Data\\'+isotope+'Sr'

#create the directories that will contain the data and analysis
try:
	os.listdir(analysisFolder+'\\'+dateWithPeriods+'_'+baseName)
except:
	os.mkdir(analysisFolder+'\\'+dateWithPeriods+'_'+baseName)
try:
	os.listdir(dataFolder+'\\'+dateWithPeriods)
except:
    os.mkdir(dataFolder+'\\'+dateWithPeriods)

todayAnalysisFolder = analysisFolder+'\\'+dateWithPeriods+'_'+baseName
todayDataFolder = dataFolder+'\\'+dateWithPeriods

#clone most up to date version of analysis code
os.system('git clone ' + repository_url + ' ' + todayAnalysisFolder)

#create the master batch files
master_batch_atom = todayDataFolder + '\\Files_' + dateWithoutPeriods + '.txt.'
f = open(master_batch_atom,'w+')
f.close()
f = open(todayDataFolder+'\\Files_'+dateWithoutPeriods+'_Bg.txt','w+')
f.close()
f = open(todayDataFolder+'\\Files_'+dateWithoutPeriods+'_Counts.txt','w+')
f.close()

#open the master batch file for convenience
os.system('START /B ' + path_to_notepad + ' ' + master_batch_atom)
