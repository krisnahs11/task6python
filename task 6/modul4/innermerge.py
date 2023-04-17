import pandas as pd 
nama= ['berti','ryndes','desi']
uts=[95,90,80]
jurusan= ['IF','SI','KA']
df3 = pd.DataFrame({'nama':nama,'UTS':uts,'Jurusan':jurusan})


nama= ['berti','ryndes','Arin']
tugas=[95,90,85]
jurusan= ['IF','SI','IF']
df4 = pd.DataFrame({'nama':nama,'tugas':tugas,'Jurusan':jurusan})
df3.merge(df4)