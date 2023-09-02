jumbled_superheroes=['DocToR_sTRAngE','sPidERmaN','MoON_KnigHT','caPTAIN_aMERIca','hULK']
indices=[]
for i in jumbled_superheroes:
    index=jumbled_superheroes.index(i)
    indices.append(index)
print(indices)
decoded_names=[]
for item in jumbled_superheroes:
    a=item.lower().replace('_',' ')
    decoded_names.append(a)
print(list(decoded_names))    

lambda_length=lambda decoded_names:len(decoded_names)
print("length of given list is ", lambda_length(decoded_names))

name_lengths=list(map(lambda_length,decoded_names))
print(name_lengths)

indices.sort(key=lambda x:name_lengths[x])
print(indices)
new_list=[decoded_names[i] for i in indices]

print("Phase 5 kickoff list:")
for count,i in enumerate(new_list):
    x=i.title()
    print("{}. {}".format(count+1,x))



                   