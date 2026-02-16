import json
json_string = '''
{
    "id":1,
    "title":"The Great Gatsby"
}

'''

book = json.loads(json_string)
print(book['title'])

json_output = json.dumps(book, indent=4)
print("\nModified JSON:")
print(json_output)