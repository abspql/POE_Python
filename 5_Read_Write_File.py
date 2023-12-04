output_file = open("outputFile.txt", "w") 

with open("inputFile.txt", "r") as scan: 
	output_file.write(scan.read()) 


output_file.close()
