filename = input()
mfilename = input()
dfilename = input()
out_filename = input()
f_size = int(input())
features = [[] for _ in range(f_size)]
f_file = open(filename)
m_file = open(mfilename)
d_file = open(dfilename)
out_file = open(out_filename, "w")
features_name = []
f_pointer = []
disease_name = []
m_names = []
count = 0

for line in m_file:
    m_names.append(line.replace("\n", ""))

m_size = len(m_names)

disease_name = d_file.readlines()

'''
while True:
    name = input()
    if name == "exit":
       break
    else:
        disease_name.append(name)
'''

for i in range(0, f_size):
    features_name.append(input())
    f_pointer.append(0)

for line in f_file.readlines():
    line = line.replace("\n", "")
    values = line.split("\t")
    for i in range(0, f_size):
        features[i].append(values[i])

d_count = 0
for i in range(0, int(len(features[0])/m_size) * f_size):
    f_count = i%f_size
    for j in range(0, m_size):
        line = str(count) + ";" + m_names[j] + ";" + features_name[f_count] + ";" + features[f_count][f_pointer[f_count]] + ";" + disease_name[d_count]
        print(line)
        out_file.write(line)
        f_pointer[f_count] += 1
        count += 1
    if f_count == f_size - 1:
        d_count += 1
        
f_file.close()
m_file.close()
out_file.close()
               


