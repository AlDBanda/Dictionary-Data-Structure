#Dict items are key value pairs enclosed in curly brackets
#Dict is ordered as of Python 3.7
#Dict is mutable
#Dict keys a re unique, cannot have duplicates
#Elements can be of different data types

'''
Dict Attributes
'''
#print(dir(dict))
#print(help(dict.popitem))



'''
Creating Python Dictionary
'''

#dict_example = {}
#dict_example = {'name': 'Alfred', 'age':35}
#dict_example = dict([(1, 'car',), (2, 'bicycle')])
#print(dict_example)
#convert Touple to a dictionary, wrap it with round brackets



'''
Access Dictionary Values
'''

#student = {'name': 'Alfred', 'age':35}
#print(student['age'])
#print(student.get('name'))
#print(student.keys()) #shows keys in dict
#print(student.values())#shows values in dict
 
#students = [{'name': 'Alfred', 'age':35},#{'name': 'Disa', 'age':30}] 
#print(students[1]['name'])
#index 0, first list, index 1
#for i in range(len(students)) :
#   print(students[i]['name'])

#You can use a for Loop as above as its easier than writing in the index manually



'''
Changing Dictionary Elements
'''
#student = {'name': 'Alfred', 'age': 35}
#student['age'] = 37
#print(student)

#==============================

#student = {'name': 'Alfred', 'age': 35}
#student.update({'name': 'Jenny', 'age':30})
#print(student) 
#Using the update method

#===============================

#student = {'name': 'Alfred', 'age': 35}
#student.setdefault('name', 'Steve')
#student.setdefault('subject', 'Python')
#print(student)
#If a default already exists it wont do anything

'''
Remove Element from Dictionary
'''
#student = {'name': 'Alfred', 'age': 35}
#student.pop('name')
#print(student)
#Pops the value name

#==============================

#student = {'name': 'Alfred', 'age': 35}
#student.popitem()
#print(student)
#Removes item to the right

#==============================
#student = {'name': 'Alfred', 'age': 35}
#student.clear()
#print(student)
#Removes everything

#================================

#student = {'name': 'Alfred', 'age': 35}
#del student
#print(student)

'''
Dictionary Membership Test
'''

#student = {'name': 'Alfred', 'age': 35}

#print('name' in student)

#Testing for keys in above