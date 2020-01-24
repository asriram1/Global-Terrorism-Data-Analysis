"""Appendix A- Pre-Processing to produce a dataset with the relevant attributes, focused for the United States, on single targets, & successful terror attacks. """

import sqlite3
file_name = input('What is the file name?: ')
infile = open(file_name, 'r')
db = sqlite3.connect(file_name)
cursor = db.cursor()

results_file = input('What is the results file name?:')**
outfile = open(results_file, 'w')

command = '''   SELECT iyear, attacktype1_txt,  targtype1_txt, gname, weapons_txt
                FROM i_GTD   *
                WHERE country_txt= 'United States' AND multiple = 0 AND success = 1 '''

cursor.execute(command)

count = 0
for row in cursor:
    print(row, file = outfile)
    count = count +1

db.commit()
db.close()
outfile.close()
