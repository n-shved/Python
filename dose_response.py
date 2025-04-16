#Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Select the file for analysis
file = input("What file would you like to analyse?: ")

#Read the .csv file into a DataFrame, check it has been loaded properly, and check for null values
df = pd.read_csv("C:\\Users\\nikit\\temp\\" + file + ".csv", header=None)
print(df.head())
print('\n')
print(df.shape)
print('\n')
print(df.info())

#Splice the original DataFrame to make two new ones--one for min. inhibition signal--DMSO,
#and one for max. inhibition signal--reference compound
dmso = pd.concat([df.iloc[8:16, 0], df.iloc[:8, 11], df.iloc[8:16, 12], df.iloc[:8, 23]])
print(dmso.head())

ref = pd.concat([df.iloc[:8, 0], df.iloc[8:16, 11], df.iloc[:8, 12], df.iloc[8:16, 23]])
print(ref.head())


#Calculate necessary values for assessing assay robustness.
#For this, z-prime (Z') needs to be >0.5, no criteria for signal-to-background ratio (S:B), but >3.0 is considered good
std_dmso = dmso.std()
std_ref = ref.std()
mean_dmso = dmso.mean()
mean_ref = ref.mean()
max_min = mean_dmso - mean_ref
z_prime = 1 - ((3 * std_dmso + 3 * std_ref)/(max_min))
s_b = mean_dmso / mean_ref

#Reset DMSO and Ref DataFrame indicies, combine into one DataFrame,
#and plot a boxplot to visually confirm max and min inhibition signals are significantly different
dmso = dmso.reset_index(drop=True)
ref = ref.reset_index(drop=True)
dmso_ref = pd.DataFrame({
    'DMSO':dmso,
    'Ref':ref
})

sns.boxplot(data=dmso_ref)
plt.show()

#Drop the max and min inhibtion values from the original DataFrame to retain only the sample wells
drc = df.drop([0, 11, 12, 23], axis=1)

concs_uM = [100, 31.646, 15.823, 10.549, 7.911, 6.329, 5.274, 4.521, 3.956, 0,
            100, 31.646, 15.823, 10.549, 7.911, 6.329, 5.274, 4.521, 3.956, 0]

#Create a list of compound id's
#This can also be automated by reading in data from an excel/csv file containing compound names,
#however, compound names have to be anonimised in this repository
comps = ['comp1', 'comp2', 'comp3', 'comp4',
         'comp5', 'comp6', 'comp7', 'comp8',
         'comp9', 'comp10', 'comp11', 'comp12',
         'comp13', 'comp14', 'comp15', 'control']

new_drc = pd.DataFrame()

for i in range(len(comps)):
        new_drc[i] = drc.iloc[i, :]
new_drc.columns = comps

print(mean_ref)

#Calculate % inhibition for each sample well
for col in new_drc.columns:
    new_drc[col] = 100 * (1 - (new_drc[col] - mean_ref)/(max_min))

new_drc['Conc (uM)'] = concs_uM
print(new_drc)

sns.scatterplot(data=new_drc, x='Conc (uM)', y='control')
plt.xscale('log')
plt.show()
