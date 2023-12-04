
d = {'Name': 'Ram',
      'Age': '19', 
      'Country': 'India'
      }
# get
print(d.get('Name'))
print(d.get('Age'))

#keys
print("In dictionary keys : ", list(d.keys()))

# value
print("In dictionary value : ", list(d.values()))

# update
d2 = {'Name': 'Neha', 'Age': '22'}
d.update(d2)
print("Updated dictionary is ",d)

# pop
d.pop('Age')
print("Pop Age in dic : ",d)

# clear
d.clear()
print("Clear dictionary : ",d)