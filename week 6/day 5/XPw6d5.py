import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sample = json.loads(sampleJson)

print(sample['company']['employee']['payble']['salary'])

# 2


with open('file.json', 'w') as f:
   sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
   json.dump(sampleJson, f, indent=2, sort_keys=True)

