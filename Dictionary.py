 #Dictionary are mutable

dist = {
     "name": "Rajat",
     "age": 20,
     "cgpa": 4.0,
     "marks": [12,15,15]
   

}
dist["age"] =21
print(dist)

null_info={}
null_info["name"] = "Zenbook 14"
print (null_info)


#Nested Distionary
student_info = {
     "name" : "Rahul Kumaer",
     "subjects" : {
          "physics":85, 
          "Maths" :95,
          "Chemistery" :68
     }
}
print(student_info["subjects"]["physics"])

#Methods In Dictionary
info = {
     "name" : "Rahul Kumaer",
     "subjects" : {
          "physics":85, 
          "Maths" :95,
          "Chemistery" :68
     }
}
print(info.keys()) # Returns all the keys but not the nested key
print(len(info))

print(info.values()) # Provides all the values stored 

print(info.items())# Returns all (key,value) pairs as tuple

print(info.get("name")) # Returns the kry according to the value


info.update({"City" : "Kathmandu"}) # Helps to update new key and value
print(info)


#Store the folling word meaning in a python dictionary

dictionary = {
     "cat": "a small animal",
     "table": ["a piece of furniture", "List of facts and figures"]
}
print(dictionary)