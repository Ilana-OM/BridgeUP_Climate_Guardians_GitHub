#import libraries
import os
#check working directory
#Create path to data folder
dataPath = '/Users/ilanaocampo/Desktop/2020_BridgeUP_Internships/Data'

if __name__=="__main__":
#when file is run on teminal its called main
	pass

else:
	print("when it is imported",os.getcwd())
	os.chdir(dataPath)
	print(os.getcwd())