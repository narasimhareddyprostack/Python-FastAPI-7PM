import json
emp_json_str='''
            [
            {"eid":101,"ename":"Rahul","avail":true,"discount":null},
            {"eid":102,"ename":"Sonia","avail":false},
            {"eid":103,"ename":"Priyanka","avail":true},
            {"eid":104,"ename":"Modi","avail":false},
            {"eid":105,"ename":"Amith","avail":true}

            ]

            '''

employees=json.loads(emp_json_str)
print(employees)
'''
[{'eid': 101, 'ename': 'Rahul', 'avail': True, 'discount': None}, 
{'eid': 102, 'ename': 'Sonia', 'avail': False},
{'eid': 103, 'ename': 'Priyanka', 'avail': True}, 
{'eid': 104, 'ename': 'Modi', 'avail': False}, 
{'eid': 105, 'ename': 'Amith', 'avail': True}]

'''