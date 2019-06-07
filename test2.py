import json
import csv
import glob

outputFile = open("data.csv", "w", newline="", encoding="utf-8")# opening the csv file 

outputWriter = csv.writer(outputFile)# creating a writer for csv file

folder_name = "verified"
needs_header = True

if needs_header == True:
    header_row = []
    header_row.append("name")
    header_row.append("email")
    header_row.append("cat_person_fav_name")
    header_row.append("cat_club_fav_name")
    header_row.append("cat_business_fav_name")
    header_row.append("contest")

    outputWriter.writerow(header_row)       

for filename in glob.iglob(folder_name+"/**/*.json"):

    sourceFile = open(filename, "r")# openning the json file 
    json_data = json.load(sourceFile) # loading the json file

    # looping through all of the attributes 
    
    row_array = [
        json_data["name"],
        json_data["email"],
        json_data["cat_person_fav_name"],
        json_data["cat_club_fav_name"],
        json_data["cat_business_fav_name"],
        "contest" in json_data,
    ]
                
    print(row_array)
    outputWriter.writerow(row_array)
    sourceFile.close()
    
outputFile.close()
    
