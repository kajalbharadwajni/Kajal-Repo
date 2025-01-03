
c.execute("SELECT * FROM patient")
data = c.fetchall()
for info in data:
        print(f"Patient ID: {info[0]}, NAME: {info[1]}, AGE: {info[2]}, DISEASE :- {info[3]}, ATTENTING DOCTOR :- {info[4]}, WARD NUMBER :- {info[5]} ")
        
conn.commit()
conn.close()



