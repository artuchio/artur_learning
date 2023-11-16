# json_string = '''
# {
#   "people": [
#     {
#       "name": "Jack Sumers",
#       "phone": "555-555-555",
#       "emails": ["jack.sumers@example.com", "jacksumers@work-place.com"],
#       "has_licence": false
#     },
#     {
#       "name": "Mary Smith",
#       "phone": "777-777-777",
#       "emails": null,
#       "has_licence": true
#     }
#   ]
# }'''
import json
# data = json.loads(json_string)
# data['people'].append({
#     'name': 'Robert Brown',
#     'phone': '222-555-5555',
#     'emails': 'robert@gmeail.com',
#     'has_licence': True
# })
# print(data)
# print(type(data))
# new_json = json.dumps(data, indent=2)
# print(new_json)
# print(type(new_json))

# with open('123_data.json', 'r') as file:
#     data = json.load(file)
#     print(data)
#     print(type(data))
#
# data['people'].append({
#     'name': 'Robert Brown',
#     'phone': '222-555-5555',
#     'emails': 'robert@gmeail.com',
#     'has_licence': True
#     })
# with open('123_data_edited.json', 'w') as file:
#     json.dump(data, file, indent=2)

import csv
# x = [1, 2, 3, 4, 5]
# x = iter(x)
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))

# for i in x:
#     print(i)
#
# for i in x:
#     print(i ** 2)

with open('009_LessonCSV.csv','r') as file:
    csv_reader = csv.reader(file)
    # # print(list(csv_reader))
    # headers = next(csv_reader)
    # for line in csv_reader:
    #     print(line)
    #
    #     # print(headers)
    #     for name, dob, city in csv_reader:
    #         print(name, dob, city)

#     with open('test_copy.csv', 'w') as wfile:
#         csv_writer = csv.writer(wfile,
#                                 lineterminator='\n',
#                                 delimiter=',',
#                                 # quotechar='*'
#                                 quoting=csv.QUOTE_ALL
#                                 )
#
#         for line in csv_reader:
#             csv_writer.writerow(line)
# with open('test_copy.csv', 'r') as new_file:
#     csv_reader = csv.reader(new_file, delimiter=',', skipinitialspace=True)
#
#     for line in csv_reader:
#         print(line)

with open('009_LessonCSV.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

    # for line in csv_reader:
    #     print(line)

    with open('009_LessonCSV.csv', 'w') as wfile:
        names = ["Name", "Date of birth", "Town"]
        csv_writer = csv.DictWriter(wfile, lineterminator='\n', fieldnames=names)
        csv_writer.writeheader()
    for line in csv_reader:
        csv_writer.writerow(line)