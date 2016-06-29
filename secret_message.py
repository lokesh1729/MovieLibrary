import os
def rename_files():
	file_list = os.listdir("/home/lokesh1729/MovieLibrary/prank/prank")
	#print(file_list);
	print("Current Working Directory"+os.getcwd())
	os.chdir("/home/lokesh1729/MovieLibrary/prank/prank")
	for file_name in file_list:
		print("Old_Name"+file_name)
		os.rename(file_name,file_name.translate(None,"0123456789"))
		print("New_Name"+file_name)
	print(file_list)
rename_files()
	
