import csv

#with open('IPL_2018.csv') as f:
#d = csv.reader(f)
#  #for r in d:
#  print(r)
#  d_list = list(d)

#match_runs = []
#for r in d_list[1:]:
#  print("Total runs scored by", r[0], "in IPL 2018 are", r[4])
#  match_runs.append(int(r[4]))
#print(d_list)
#print("Total runs scored by all the players in matches are", sum(match_runs))
"""
with open("IPL_2018.csv") as f:
  d = csv.reader(f)
  d_list = list(d)

sixers = []
for r in d_list[1:]:
  sixers.append(int(r[12]))

print(sum(sixers))
print(sixers)
"""

with open("terserah.csv", "w") as f:
  csv_writer = csv.writer(f)
  h = ("Name", "Class", "City")
  d = (
    ("Bob", "9", "Jakarta"),
    ("Larry", "6", "Serang"),
    ("Harry", "7", "Surabaya"),
  )
  csv_writer.writerow(h)
  for r in d:
    csv_writer.writerow(r)
