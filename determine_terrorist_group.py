"""Appendix C- Program using user input for year, attack_type, target_type & weapon_type to produce name/s of terrorist group/s corresponding to the inputs"""

import sqlite3
file_name = input('What is the file name?: ')
infile = open(file_name, 'r')
db = sqlite3.connect(file_name)
cursor = db.cursor()

results_file = input('What is the results file name?:')
outfile = open(results_file, 'w')

target_year= int(input(“Select the year in which the attack took place? ”))
target_attack = input(“What type of an attack took place? ”)
target_targ = input(“What was the target attacked? “) 
target_weapon = input (“What was the weapon used in this attack?”) 

command = '''  SELECT gname
               FROM GTD_FINAL
               WHERE iyear= ? AND attacktype1_txt = ? AND targtype1_txt = ? AND weaptype1_txt = ? ; '''
               
cursor.execute(command, [target_year, target_attack, target_targ, target_weapon] )

count = 0
for row in cursor:
    print(row, file = outfile)
    count = count +1

db.commit()
db.close()
outfile.close()
