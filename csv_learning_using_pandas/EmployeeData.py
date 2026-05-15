import pandas as pd
from collections import Counter


csv_file = pd.read_csv('acbb2271e66c10a5b73aacf82ca82784\employees.csv')

csv_file['EMPLOYEE_ID'] = csv_file['EMPLOYEE_ID'].astype(str).str.strip()
csv_file['MANAGER_ID'] = csv_file['MANAGER_ID'].astype(str).str.strip()
"""
#print all emplpyees under a cerain manager
is_manager = csv_file['EMPLOYEE_ID'].isin(csv_file['MANAGER_ID'])

#Print the rows where this condition is true
# --print(csv_file[is_manager])
manager_ids = csv_file.loc[is_manager, 'EMPLOYEE_ID']
#print all the employees under a certain manager
is_under_manager = csv_file['MANAGER_ID'].isin(manager_ids)
"""
#merge works as a sql join where I do a left join to pull
#all managers and what their employees id's are
merged = csv_file.merge(
    csv_file[['EMPLOYEE_ID','FIRST_NAME']],
    left_on='MANAGER_ID',
    right_on='EMPLOYEE_ID',
    suffixes=('_employee', '_manager'),
    how='left'
)
#result to be able to visualize merged data and manipulate it
result = merged[['FIRST_NAME_employee', 'FIRST_NAME_manager']]
print(result)
#here I created a list to easily pull the managers and their employees counts
manager = []
for index, row in result.iterrows():
    if isinstance(row['FIRST_NAME_manager'],str):
        manager.append(row['FIRST_NAME_manager'])
    else:
        manager.append(f"{row['FIRST_NAME_employee']} is CEO")

c = Counter(manager)
for manager_name, count in c.items():
    if manager_name.endswith("CEO"):
        print(manager_name)
    elif count == 1:
        print(f"{manager_name} has 1 employee")
    else:
        print(f"{manager_name} has {count} employees")
#now I have to print all department salaries combined
#groupby scans DEPARTMENT_ID and groups the rows together based on the unique ids
# all employees working in each department are put into a dept "bucket"
# once the buckets are created pandas ignores other columns and only looks at salaries then sums 
department_salaries = csv_file.groupby('DEPARTMENT_ID')['SALARY'].sum()

print(department_salaries)

