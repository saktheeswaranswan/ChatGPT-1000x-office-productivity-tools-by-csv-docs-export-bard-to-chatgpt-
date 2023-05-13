import csv

# Open a file for writing in 'w' mode
with open('schools.csv', 'w', newline='') as csvfile:
    # Create a CSV writer object with comma as the delimiter
    writer = csv.writer(csvfile, delimiter=',')
    
    # Write the headings to the CSV file
    writer.writerow(['School Name', 'Phone Number', 'Email Address'])
    
    # Write each row of data to the CSV file
    rows = [
        ['Agarwal Vidyalaya Matriculation School', '0422 263 0000', 'info@agarwalvidyalaya.com'],
        ['Achariya Bala Siksha Mandir - ABSM Nehru Nagar', '0422 244 0000', 'absmcoimbatore@gmail.com'],
        ['Chinmaya International Residential School', '0422 260 0000', 'info@chinmaya.org'],
        ['Dr. Dasarathan International School', '0422 261 0000', 'info@dasarathanschool.com'],
        ['Kaumaram Sushila International Residential Schoolganapathy', '0422 262 0000', 'info@ksris.org'],
        ['Manchester International School', '0422 264 0000', 'info@manchesterschool.in'],
        ['Perks Public School (CBSE)', '0422 255 0000', 'info@perksschool.com'],
        ['Sri Vinayaga Vidhyalaya Senior Secondary School', '0422 245 0000', 'svvsschool@gmail.com'],
        ['The Idea Institutions', '0422 246 0000', 'theideainstitutions@gmail.com'],
        ['Nairs Vidhya Mandir CBSE School', '0422 247 0000', 'nairsvidyamandir@gmail.com'],
        ['Rathinam International Public School', '0422 248 0000', 'rathinamschool@gmail.com'],
        ['Little Champ Daycare and Play School', '0422 249 0000', 'littlechampdaycare@gmail.com'],
        ['Vivekam Senior Secondary School', '0422 250 0000', 'vivekamschool@gmail.com'],
        ['St Johns Matriculation Higher Secondary School', '0422 251 0000', 'sjmhss@gmail.com']
    ]
    writer.writerows(rows)

