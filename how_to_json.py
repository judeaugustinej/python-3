import json

json_string = '{"first_name":"Jude","last_name":"job"}'
parsed_json = json.loads(json_string)

print("""The json_string = {} ,the parsed_json = {}\\
parsed_json['first_name']= {}, parsed_json['last_name'] = {}""".format(json_string,
                                                                parsed_json,
                                                                parsed_json['first_name'],
                                                                parsed_json['last_name']))
                                                                
                                                                
#--Output--
"""
The json_string = {"first_name":"Jude","last_name":"job"} ,the parsed_json = {'last_name': 'job', 'first_name': 'Jude'}\
 parsed_json['first_name']= Jude, parsed_json['last_name'] = job
"""
                                                              

