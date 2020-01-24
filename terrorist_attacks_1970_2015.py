"""Appendix B- Total Number of Attacks by all the Terrorist Groups between 1970 & 2015"""

import sqlite3
file_name = input('What is the file name?: ')
infile = open(file_name, 'r')
db = sqlite3.connect(file_name)
cursor = db.cursor()

results_file = input('What is the results file name?:')
outfile = open(results_file, 'w')

command = '''   SELECT gname, COUNT(*)
                FROM GTD_FINAL  
                GROUP BY gname;'''

cursor.execute(command)

count = 0
for row in cursor:
    print(row, file = outfile)
    count = count +1

db.commit()
db.close()
outfile.close()
