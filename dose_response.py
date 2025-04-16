import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

file = input("What file would you like to analyse?: ")

df = pd.read_csv("C:\\Users\\nikit\\temp\\" + file + ".csv", header=None)
print(df.head())
print('\n')
print(df.shape)
print('\n')
print(df.info())

dmso = pd.concat([df.iloc[8:16, 0], df.iloc[:8, 11], df.iloc[8:16, 12], df.iloc[:8, 23]])
print(dmso.head())

ref = pd.concat([df.iloc[:8, 0], df.iloc[8:16, 11], df.iloc[:8, 12], df.iloc[8:16, 23]])
print(ref.head())

std_dmso = dmso.std()
std_ref = ref.std()
mean_dmso = dmso.mean()
mean_ref = ref.mean()
max_min = mean_dmso - mean_ref
z_prime = 1 - ((3 * std_dmso + 3 * std_ref)/(max_min))
s_b = mean_dmso / mean_ref


dmso = dmso.reset_index(drop=True)
ref = ref.reset_index(drop=True)
dmso_ref = pd.DataFrame({
    'DMSO':dmso,
    'Ref':ref
})

#sns.boxplot(data=dmso_ref)
#plt.show()

drc = df.drop([0, 11, 12, 23], axis=1)

concs_uM = [100, 31.646, 15.823, 10.549, 7.911, 6.329, 5.274, 4.521, 3.956, 0,
            100, 31.646, 15.823, 10.549, 7.911, 6.329, 5.274, 4.521, 3.956, 0]

comps = ['comp1', 'comp2', 'comp3', 'comp4',
         'comp5', 'comp6', 'comp7', 'comp8',
         'comp9', 'comp10', 'comp11', 'comp12',
         'comp13', 'comp14', 'comp15', 'control']

new_drc = pd.DataFrame()

for i in range(len(comps)):
        new_drc[i] = drc.iloc[i, :]
new_drc.columns = comps

print(mean_ref)

for col in new_drc.columns:
    new_drc[col] = 100 * (1 - (new_drc[col] - mean_ref)/(max_min))

new_drc['Conc (uM)'] = concs_uM
print(new_drc)

sns.scatterplot(data=new_drc, x='Conc (uM)', y='control')
plt.xscale('log')
plt.show()