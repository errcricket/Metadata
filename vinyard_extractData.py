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
#	fileLine = fileLine.replace('_','',1)

	return fileLine

path = '/home/erin/Soil/Metadata/'
project_link = '<a target="_blank" href="http://metagenomics.anl.gov/metagenomics.cgi?page=MetagenomeOverview&metagenome='
metadata_link= '<a target="_blank" href="http://metagenomics.anl.gov/metagenomics.cgi?page=DownloadMetagenome&action=download_md&filename=mgm'

#outputPath = path + 'Vinyard_Project_Metadata.csv'
#outputFile_meta = open(outputPath, 'w')
#outputFile_meta.write('#ID\tname\t_environment\tfeature\tmaterial\tsampleBiome\t' + \
#	'organization\tPI_firstname\tPI_lastname\tPI_email\tPI_organization_url\t_NCBI\tcollectionDate\t' + \
#	'collectionTimeZone\tLatitude\tLongitude\tLocation\tsampleCountry\t' + \
#	'sampleContinent\tdepth\ttemperature\tpH\tsalinity\t' + \
#	'sequencingMethod\tdataType\tpubMedID\tProjectLink\tMetatdataLink\tdescription\tDescription\tsamp_collect_device\tEnvironment\n')


dataList = []
longitudeList = [] #this list is to keep track of redundant values

#fileList = ['4520300.3.txt', '4520301.3.txt', '4520302.3.txt', '4520303.3.txt', '4520304.3.txt', '4520305.3.txt', '4520306.3.txt', '4520307.3.txt', '4520308.3.txt', '4520309.3.txt', '4520310.3.txt', '4520311.3.txt', '4520312.3.txt', '4520313.3.txt', '4520314.3.txt', '4520315.3.txt', '4520316.3.txt', '4520317.3.txt', '4520318.3.txt', '4520319.3.txt', '4520320.3.txt', '4520321.3.txt', '4520322.3.txt', '4520323.3.txt', '4520324.3.txt', '4520325.3.txt', '4520326.3.txt', '4520327.3.txt', '4520328.3.txt', '4520329.3.txt', '4520330.3.txt', '4520331.3.txt', '4520332.3.txt', '4520333.3.txt', '4520334.3.txt', '4520335.3.txt', '4520336.3.txt', '4520337.3.txt', '4520338.3.txt', '4520339.3.txt', '4520340.3.txt', '4520341.3.txt', '4520342.3.txt', '4520343.3.txt', '4520344.3.txt', '4520345.3.txt', '4520346.3.txt', '4520347.3.txt', '4520348.3.txt', '4520349.3.txt', '4520350.3.txt', '4520351.3.txt', '4520352.3.txt', '4520353.3.txt', '4520354.3.txt', '4520355.3.txt', '4520356.3.txt', '4520357.3.txt', '4520358.3.txt', '4520359.3.txt', '4520360.3.txt', '4520361.3.txt', '4520362.3.txt', '4520363.3.txt', '4520364.3.txt', '4520365.3.txt', '4520366.3.txt', '4520367.3.txt', '4520368.3.txt', '4520369.3.txt', '4520370.3.txt', '4520371.3.txt', '4520372.3.txt', '4520373.3.txt', '4520374.3.txt', '4520375.3.txt', '4520376.3.txt', '4520377.3.txt', '4520378.3.txt', '4520379.3.txt', '4520380.3.txt', '4520381.3.txt', '4520382.3.txt', '4520383.3.txt', '4520384.3.txt', '4520385.3.txt', '4520386.3.txt', '4520387.3.txt', '4520388.3.txt', '4520389.3.txt', '4520390.3.txt', '4520391.3.txt', '4520392.3.txt', '4520393.3.txt']

fileList = ['4520391.3.txt']
#Project = ['project_name', 'mgrast_id', 'PIlastname', 'PI_organization', 'PI_firstname', 'project_description', 'PI_email']
#Sample = ['sample_name', 'mgrast_id', 'country', 'longitude', 'location', 'elevation', 'collection_date', 'feature', 'collection_time', 'env_package', 'latitude', 'continent', 'biome', 'collection_timezone', 'material', 'temperature']
#Library = ['library_name', 'mgrast_id', 'metagenome_id', 'seq_meth', 'metagenome_name']
#Environmental = ['mgrast_id', 'plant_body_site', 'env_package', 'infra_specific_name', 'infra_specific_rank', 'host_taxid', 'host_common_name']

Project={'project_name':'NA', 'mgrast_id':'NA', 'PIlastname':'NA', 'PI_organization':'NA', 'PI_firstname':'NA', 'project_description':'NA', 'PI_email':'NA'}
Sample={'sample_name':'NA', 'mgrast_id':'NA', 'country':'NA', 'longitude':'NA', 'location':'NA', 'elevation':'NA', 'collection_date':'NA', 'feature':'NA', 'collection_time':'NA', 'env_package':'NA', 'latitude':'NA', 'continent':'NA', 'biome':'NA', 'collection_timezone':'NA', 'material':'NA', 'temperature':'NA'}
Library={'library_name':'NA', 'mgrast_id':'NA', 'metagenome_id':'NA', 'seq_meth':'NA', 'metagenome_name':'NA'}
Environmental={'mgrast_id':'NA', 'plant_body_site':'NA', 'env_package':'NA', 'infra_specific_name':'NA', 'infra_specific_rank':'NA', 'host_taxid':'NA', 'host_common_name':'NA'}
  
def setword(dictionary, fileLine): #strip word (searchWord) from file (fileLine) & return the new line
	for k in dictionary.keys():
		if fileLine.startswith(k): 
			fileLine = removeInput(fileLine, k)
			dictionary[k] = fileLine
		
	return dictionary[k] 

for files in fileList:
	files = '/data/erin/Soil/Metadata/' + files
	with open(files, 'r') as inputFile:
		lines = inputFile.readlines()
		
		for line in lines:
			if line.startswith('Project'):
				line = removeInput(line, 'Project')
				setword(Project, line)
#				for p in Project.keys():
#					if line.startswith(p): 
#						line = removeInput(line, p)
#						Project[p] = line

			if line.startswith('Sample'):
				line = removeInput(line, 'Sample')
				setword(Sample, line)
#				for s in Sample.keys():
#					if line.startswith(s): 
#						line = removeInput(line, s)
#						Sample[s] = line

			if line.startswith('Library: metagenome'):
				line = removeInput(line, 'Library: metagenome')
				setword(Library, line)

#				for l in Library.keys():
#					if line.startswith(l): 
#						line = removeInput(line, l)
#						Library[l] = line
#
			if line.startswith('Enviromental Package: plant-associated'):
				line = removeInput(line, 'Enviromental Package: plant-associated')
				setword(Environmental, line)

#				for e in Environmental.keys():
#					if line.startswith(e): 
#						line = removeInput(line, e)
#						Environmental[e] = line
#

print Project
print Sample
print Library
print Environmental
'''
			if line.startswith('Sample')
				line = removeInput(line, 'Sample')
			if line.startswith('Library: metagenome')
				line = removeInput(line, 'Library: metagenomes')
			if line.startswith('Environmental Package: plant-associated')
				line = removeInput(line, 'Environmental Package: plant-associated')
			dataList.append(line) #The datasets in the file(s)

for files in fileList:
	files = '/data/erin/Soil/MetaData/' + files
#for files in dataList:
	#####Project
	project_name = 'NA'
	project_description = 'NA'
	project_sampleFeature = 'NA'
	project_sampleBiome= 'NA'
	project_organization = 'NA'
	project_organization_url = 'NA'
	project_PI_firstName = 'NA'
	project_PI_lastName = 'NA'
	project_PI_email = 'NA'
	project_PI_organization_url = 'NA'
	project_NCBI = 'NA'
	project_pubMedID = 'NA'
	project_environment = 'NA'
	project_Description = 'NA'

	####Sample
	project_collectionDate = 'NA'
	project_collectionTimeZone = 'NA'
	project_sampleSize = 'NA'
	project_latitude = 'NA'
	project_longitude = 'NA'
	project_location = 'NA'
	project_sampleCountry = 'NA'
	project_sampleContinent = 'NA'
	project_elevation = 'NA'
	project_temperature = 'NA'
	project_pH = 'NA'
	project_salinity = 'NA'
	project_material = 'NA'
	project_samp_collect_device = 'NA'
	sample_name = 'NA'
	site = 'NA'
	host_taxid = 'NA'
	host_name = 'NA'
	name = 'NA'
	rank = 'NA'
	

	###Library: mimarks-survey seq_meth, Library: metagenome
	project_sequencingMethod = 'NA'
	project_dataType = 'NA'

	with open(files, 'r') as inputFile:
		dataList.append(line) #The datasets in the file(s)
	inputF = open(files, 'r')
	lines = inputF.readlines()

	for line in lines:
		#####Project
		if line.startswith('Project'):
			line = removeInput(line, 'Project')
			if line.startswith('project_name'):
				project_name = removeInput(line, 'project_name') 
			if line.startswith('project_description'):
				project_description = removeInput(line, 'project_description')
			if line.startswith('PI_organization') and line.startswith('PI_organization_url') == False and line.startswith('PI_organization_address') == False and line.startswith('PI_organization_country') == False:
				project_organization = removeInput(line, 'PI_organization')
			if line.startswith('PI_firstname'):
				project_PI_firstName = removeInput(line, 'PI_firstname')
			if line.startswith('PI_lastname'):
				project_PI_lastName = removeInput(line, 'PI_lastname')
			if line.startswith('PI_email'):
				project_PI_email = removeInput(line, 'PI_email') 

		####Sample
		if line.startswith('Sample'):
			line = removeInput(line, 'Sample')
			if line.startswith('sample_name'): #THIS IS NEW!!!!!!
				sample_name = removeInput(line, 'sample_name')
			if line.startswith('mgrast_id'): #THIS IS NEW!!!!!!
				mgrast_id = removeInput(line, 'mgrast_id')
			if line.startswith('feature'):
				project_feature = removeInput(line, 'feature')
			if line.startswith('biome'):
				project_sampleBiome = removeInput(line, 'biome')
			if line.startswith('collection_date'):
				project_collectionDate = removeInput(line, 'collection_date')
			if line.startswith('collection_timezone'):
				project_collectionTimeZone = removeInput(line, 'collection_timezone')
			if line.startswith('latitude'):
				project_latitude = removeInput(line, 'latitude')
			if line.startswith('longitude'):
				project_longitude = removeInput(line, 'longitude') 
				longitudeList.append(project_longitude)
			if line.startswith('location'):
				project_location = removeInput(line, 'location')
			if line.startswith('country'):
				project_sampleCountry = removeInput(line, 'country')
			if line.startswith('continent'):
				project_sampleContinent = removeInput(line, 'continent')
			if line.startswith('elevation'):
				project_elevation = removeInput(line, 'elevation')
			if line.startswith('temperature'):
				project_temperature = removeInput(line, 'temperature')
			if line.startswith('pH'):
				project_pH = removeInput(line, 'pH')
			if line.startswith('salinity') or line.startswith('misc_param') and project_salinity == 'NA':
				line = removeInput(line, 'misc_param')
				line = removeInput(line, 'salinity')
				project_salinity = line
			if line.startswith('material'):
				project_material = removeInput(line, 'material')
			if line.startswith('env_package'):
				project_environment = removeInput(line, 'env_package')

		####Environmental 
		if line.startswith('Enviromental'): 
			line = removeInput(line, 'Environmental\t')
			if line.startswith('Package'):
				line = removeInput(line, 'Package\t')
				if line.startswith('plant-associated'):
					line = removeInput(line, 'plant-associated\t')
					if line.startswith('plant_body_site'):
						line = removeInput(line, 'plant_body_site\t')
						site = line
					if line.startswith('host_taxid'):
						line = removeInput(line, 'host_taxid\t')
						host_taxid = line
					if line.startswith('host_common_name'):
						line = removeInput(line, 'host_common_name\t')
						host_name = line
					if line.startswith('infra_specific_name'):
						line = removeInput(line, 'infra_specific_name\t')
						name = line
					if line.startswith('infra_specific_rank'):
						line = removeInput(line, 'infra_specific_rank\t')
						rank = line
			if line.startswith('env_package'):
				project_environment = removeInput(line, 'env_package')

		####Library
		if line.startswith('Library:'): 
			line = removeInput(line, 'Library:')
			if line.startswith('metagenome'):
				line = removeInput(line, 'metagenome')		
				if line.startswith('pubmed_id'):
					project_pubMedID = removeInput(line, 'pubmed_id')
				if line.startswith('seq_meth'):
					project_sequencingMethod = removeInput(line, 'seq_meth')
				if line.startswith('project_dataType'):
					project_dataType = line
			if line.startswith('mimarks-survey'):
				line = removeInput(line, 'mimarks-survey')
				if line.startswith('pubmed_id'):
					project_pubMedID = removeInput(line, 'pubmed_id')
				if line.startswith('seq_meth'):
					project_sequencingMethod = removeInput(line, 'seq_meth')
				if line.startswith('project_dataType'):
					project_dataType = line

	files = files.replace(path, '')
	#files = files.replace('/data/erin/Ruti/TroisiemeCodon_Position/ENVIRONMENTS/MetaData/Current/', '')
####Files below are different in supplimentary materials (Dinsdale) from MG-Rast
	fileNotxt = files.replace('.txt', '')
	outputLink = str(project_link + fileNotxt + '">ProjectLink</a>\t' + metadata_link + fileNotxt + '.metadata.txt">MetadataLink</a>')
	outputFile_meta.write(fileNotxt + '\t' + project_name.lower() + '\t' + project_environment.lower() + '\t' + project_feature.lower() + '\t' + project_material.lower() + '\t' + \
		project_sampleBiome.lower() + '\t' + project_organization.lower() + '\t' + project_PI_firstName.upper() + '\t' + project_PI_lastName.upper() + '\t' + project_PI_email.lower() + '\t' + \
		project_PI_organization_url.lower() + '\t' + project_NCBI.lower() + '\t' + project_collectionDate + '\t' + project_collectionTimeZone + '\t' + \
		project_latitude + '\t' + project_longitude + '\t' + project_location + '\t' + project_sampleCountry + '\t' + project_sampleContinent + '\t' + \
		project_elevation + '\t' + project_temperature  + '\t' + project_pH + '\t' + project_salinity + '\t' + project_sequencingMethod + '\t' + \
		project_dataType + '\t' + project_pubMedID + '\t' + outputLink + '\t' + project_description.lower() + '\t' + project_Description.lower() + '\t' + project_samp_collect_device.lower() + '\n')

	inputF.close()
#print(longitudeList)
#print(len(longitudeList))
outputFile_meta.close()
#inputFile.close()
'''
