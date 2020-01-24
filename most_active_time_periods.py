"""Appendix D- Time Period When Terror Groups Were Most Active"""

import sqlite3
file_name = input('What is the file name?: ')
infile = open(file_name, 'r')
db = sqlite3.connect(file_name)
cursor = db.cursor()

results_file = input('What is the results file name?:')
outfile = open(results_file, 'w')

command = '''SELECT gname, iyear, COUNT(*)
FROM GTD_FINAL
WHERE country_txt = 'United States'
AND success = 1
AND multiple = 0
GROUP BY gname, iyear ;'''

cursor.execute(command)

count = 0
for row in cursor:
    print(row, file = outfile)
    count = count +1

db.commit()
db.close()
outfile.close()
