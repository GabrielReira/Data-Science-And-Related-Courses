# Add total col as sum of individuals and family_members
homelessness['total']=homelessness['family_members']+homelessness['individuals']

# Add p_individuals col as proportion of total that are individuals
homelessness['p_individuals']=homelessness['individuals']/homelessness['total']

# See the result
print(homelessness.head())
