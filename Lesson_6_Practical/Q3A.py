# One solution using dictionary key - vehicle registration
# value - registered owner name and registration date
vehicleList = {"SJA1234T": ["Tan Mei Mei", "13 Sep 2008"],
                "SA007": ["James Bond", "07 Jul 2007"]
               }
value = vehicleList.get("SA007")
print(value)

vehicleList["SJA1234T"] = ["Tan Mei Mei", "13 Sep 2020"]
print(vehicleList.get("SJA1234T"))

value = vehicleList.get("SA007")
print(value[0])
