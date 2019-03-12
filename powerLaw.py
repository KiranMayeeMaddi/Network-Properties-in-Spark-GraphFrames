import sys
import pandas as pd
import powerlaw

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = pd.read_csv(filename)
    results = powerlaw.Fit(f['count'])
    print(results.power_law.alpha)

