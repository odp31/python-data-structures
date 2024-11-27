my_dict = {"name": "Alice", "age": 30, "city": "new york"}

# accessing values 
print(my_dict["name"]) #output; alice

# adding new key-value pair
my_dict["job"] = "Engineer"

# removing a key-value pair 
del my_dict["age"]

# iterating over key-value pairs
for key, value in my_dict.items():
  print(key, value) 
