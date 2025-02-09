#initalise dictionary
test_dict={"Codingal":2,"is":2,"best":5,"for":2,"Coding":3}
#printing original dictionary
print("The original dictionary"+str (test_dict))
#initialise value
k=2
#Using loop
#Selective key values in dictionary
res=0
for key in test_dict:
    if test_dict[key]==k:
        res = res + 1
#printing result
print("Frequency of K is:"+str(res))       