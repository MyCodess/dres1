
# #--I- assign-start-value ONLY if var1 was NOT defined already!:
try: f1_counter1
except NameError: f1_counter1 = 10
else: f1_counter1 += 1   # #--increment by each loading/import:

# #-- say hello by  each loading/import:
print("f1.py says Hello! f1_counter1: ", f1_counter1)
