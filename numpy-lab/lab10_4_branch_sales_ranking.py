"""Load branch sales from a TSV file and rank branches by total sales."""

import numpy as np
from pathlib import Path
data = np.loadtxt(Path(__file__).parent / "sales.tsv", delimiter="\t", dtype=int)

sales = data[:,1:]
branches = data[:,0]
sumsales = np.sum(sales, axis=1)
comb = np.stack((branches, sumsales), axis=1)
sort = comb[comb[:, 1].argsort()[::-1]]

print("Branch\tSales")
for i in range(len(sort)):
    print("%d\t%d" % (sort[i,0], sort[i, 1]))
