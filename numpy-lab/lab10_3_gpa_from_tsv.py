"""Load student grades from a TSV file and compute each student's weighted GPA."""

import numpy as np
from pathlib import Path
data = np.loadtxt(Path(__file__).parent / "grades.tsv", delimiter="\t", dtype=float)

def gpa(x1,x2,x3,x4,x5,x6):
    return ((x1+x4+x5+x6)*3 + x2*2 + x3)/(15)

sid = data[:,0]
sc = data[:,1:]

print("Student ID\tGPA")
for i in range(len(sid)):
    print("%d\t%.2f" % (sid[i], gpa(sc[i][0], sc[i][1], sc[i][2], sc[i][3], sc[i][4], sc[i][5])))
