todo 
2. implement "export_to_csv" method and test
3. change DBPASSWORD to Aberdeen 123, add guide on readme for shaun and add comments for use

Instructions for use

1. CSV file guidelines
- Make sure the **csv row format** for the students file is 'name,degree,score,experience'
- Ensure that experience is included in the options specified in the 'experience' column of 'students' table
- Also ensure that the 'field' column for the internship is a value specified in the 'field' column
- Please provide **two distinct** csv files, one for students records and one for internships

2. Upload & Download data via csv
- to upload data, make sure an instance of DatabasePopulator class is instantiated in the main file,
  then call '.upload_csv(file1, file2)' to populate and '.download_data' to dowload the 'students' and 'internships'
  tables in two seperate csv files.
- This should be enough to implement some sort of matching algorithm
