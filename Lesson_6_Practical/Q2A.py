namelist = {"S1234567A": "Mary Tan",
            "S2340986T": "Steve Lim",
            "S6734278E": "Yeo Ming Ming",
            "G7878439K": "Aaron Smith"
            }
# Add an element to the dictionary
namelist["T9956223G"] = "Tan Shan Shan"

# Iterate over the dictionary and print the value associate with key
for key in namelist:
    print(key, namelist[key])

# Search for name
record = namelist.get("G7278253K", "Record not found!")
print(record)
