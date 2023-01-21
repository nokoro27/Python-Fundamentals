#Nested Dictionaries & Lists 

##Update Values in Dictionaires and Lists 
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


## To change the value 10 in x to 15
x[1][0] = 15

##Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last-name'] = 'Bryant'

##In the sports_dictionary, change 'Messi' to 'Andres' 
sports_directory['soccer'][0] = 'Andres'

##Change the value 20 in z to 30 
z[0]['y'] = 30


##Iterate Through a List of Dictionaries 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for item in some_list:
        for key, value in item.items():
            print(f'{key} - {value}')

iterateDictionary(students)

#Get Values From a List of Dictionaries 
def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])

iterateDictionary2('first_name', students)

##Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f'{key} : {len(value)}')
        for item in value:
            print(item)

