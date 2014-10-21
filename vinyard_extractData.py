'''
Author:	E. Reichenerger
Date:	10.21.2014

Purpose: Given a folder containing files from  from MG-Rast, extract the metatdata from the metatdata files (vinyard specific)

e.g. 4440281.3, http://metagenomics.anl.gov/metagenomics.cgi?page=MetagenomeOverview&metagenome=4440281.3
'''

import sys
import os 
import glob 
import sys
import re #regular expressions
import pdb
  
def removeInput(fileLine, searchWord): #strip word (searchWord) from file (fileLine) & return the new line
	fileLine = fileLine.replace(searchWord, '')
	fileLine = fileLine.replace('\n', '')
	fileLine = str(fileLine.lstrip(' '))
	fileLine = str(fileLine.rstrip(' '))
	fileLine = ' '.join(fileLine.split())
	fileLine = str(fileLine.lstrip(' '))
	fileLine = fileLine.replace(' ', '_')
	fileLine = str(fileLine.lstrip('_'))
	fileLine = str(fileLine.rstrip('_'))

	return fileLine
  
def createHeader(dictionary, stringName): #this creates the header line in output file
	for d in dictionary.keys():
		stringName = stringName + d + '\t'

	return stringName

def setword(dictionary, fileLine): #assigns values to dictionary keys
	for k in dictionary.keys():
		if fileLine.startswith(k): 
			fileLine = removeInput(fileLine, k)
			dictionary[k] = fileLine
		
	return dictionary[k] 
 
def createString(dictionary, stringName): #this creates the header line in output file
	for d in dictionary.keys():
		stringName = stringName + dictionary[d] + '\t'

	return stringName

path = '/home/erin/Soil/Metadata/'
project_link = '<a target="_blank" href="http://metagenomics.anl.gov/metagenomics.cgi?page=MetagenomeOverview&metagenome='
metadata_link= '<a target="_blank" href="http://metagenomics.anl.gov/metagenomics.cgi?page=DownloadMetagenome&action=download_md&filename=mgm'

fileList = ['4520300.3.txt', '4520301.3.txt', '4520302.3.txt', '4520303.3.txt', '4520304.3.txt', '4520305.3.txt', '4520306.3.txt', '4520307.3.txt', '4520308.3.txt', '4520309.3.txt', '4520310.3.txt', '4520311.3.txt', '4520312.3.txt', '4520313.3.txt', '4520314.3.txt', '4520315.3.txt', '4520316.3.txt', '4520317.3.txt', '4520318.3.txt', '4520319.3.txt', '4520320.3.txt', '4520321.3.txt', '4520322.3.txt', '4520323.3.txt', '4520324.3.txt', '4520325.3.txt', '4520326.3.txt', '4520327.3.txt', '4520328.3.txt', '4520329.3.txt', '4520330.3.txt', '4520331.3.txt', '4520332.3.txt', '4520333.3.txt', '4520334.3.txt', '4520335.3.txt', '4520336.3.txt', '4520337.3.txt', '4520338.3.txt', '4520339.3.txt', '4520340.3.txt', '4520341.3.txt', '4520342.3.txt', '4520343.3.txt', '4520344.3.txt', '4520345.3.txt', '4520346.3.txt', '4520347.3.txt', '4520348.3.txt', '4520349.3.txt', '4520350.3.txt', '4520351.3.txt', '4520352.3.txt', '4520353.3.txt', '4520354.3.txt', '4520355.3.txt', '4520356.3.txt', '4520357.3.txt', '4520358.3.txt', '4520359.3.txt', '4520360.3.txt', '4520361.3.txt', '4520362.3.txt', '4520363.3.txt', '4520364.3.txt', '4520365.3.txt', '4520366.3.txt', '4520367.3.txt', '4520368.3.txt', '4520369.3.txt', '4520370.3.txt', '4520371.3.txt', '4520372.3.txt', '4520373.3.txt', '4520374.3.txt', '4520375.3.txt', '4520376.3.txt', '4520377.3.txt', '4520378.3.txt', '4520379.3.txt', '4520380.3.txt', '4520381.3.txt', '4520382.3.txt', '4520383.3.txt', '4520384.3.txt', '4520385.3.txt', '4520386.3.txt', '4520387.3.txt', '4520388.3.txt', '4520389.3.txt', '4520390.3.txt', '4520391.3.txt', '4520392.3.txt', '4520393.3.txt']

Project={'project_name':'NA', 'mgrast_id':'NA', 'PI_lastname':'NA', 'PI_organization':'NA', 'PI_firstname':'NA', 'project_description':'NA', 'PI_email':'NA'}
Sample={'sample_name':'NA', 'mgrast_id':'NA', 'country':'NA', 'longitude':'NA', 'location':'NA', 'elevation':'NA', 'collection_date':'NA', 'feature':'NA', 'collection_time':'NA', 'env_package':'NA', 'latitude':'NA', 'continent':'NA', 'biome':'NA', 'collection_timezone':'NA', 'material':'NA', 'temperature':'NA'}
Library={'library_name':'NA', 'mgrast_id':'NA', 'metagenome_id':'NA', 'seq_meth':'NA', 'metagenome_name':'NA'}
Environmental={'mgrast_id':'NA', 'plant_body_site':'NA', 'env_package':'NA', 'infra_specific_name':'NA', 'infra_specific_rank':'NA', 'host_taxid':'NA', 'host_common_name':'NA'}

headerString = ''

headerString = createHeader(Project, headerString)
headerString = createHeader(Sample, headerString)
headerString = createHeader(Library, headerString)
headerString = createHeader(Environmental, headerString)
headerString = headerString + 'project_link' + '\t' + 'metadata_link' + '\n'

#outputPath = path + 'Vinyard_Project_Metadata.csv'
outputPath = 'Vinyard_Project_Metadata.csv'
outputFile = open(outputPath, 'w')
outputFile.write(headerString)

for files in fileList:
	files = '/data/erin/Soil/Metadata/' + files
	with open(files, 'r') as inputFile:
		lines = inputFile.readlines()
		
		for line in lines:
			if line.startswith('Project'):
				line = removeInput(line, 'Project')
				setword(Project, line)

			if line.startswith('Sample'):
				line = removeInput(line, 'Sample')
				setword(Sample, line)

			if line.startswith('Library: metagenome'):
				line = removeInput(line, 'Library: metagenome')
				setword(Library, line)

			if line.startswith('Enviromental Package: plant-associated'):
				line = removeInput(line, 'Enviromental Package: plant-associated')
				setword(Environmental, line)
		
		metadataString = ''
		metadataString = createString(Project, metadataString)
		metadataString = createString(Sample, metadataString)
		metadataString = createString(Library, metadataString)
		metadataString = createString(Environmental, metadataString)
		metadataString = metadataString + project_link + Library['metagenome_id'] + '">ProjectLink</a>\t' + metadata_link + Library['metagenome_id'] + '.metadata.txt">MetadataLink</a>\n'

		outputFile.write(metadataString)

outputFile.close()
