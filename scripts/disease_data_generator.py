filename = input()
mfilename = input()
out_filename = input()
f_size = int(input())
features = [[] for _ in range(f_size)]
f_file = open(filename)
m_file = open(mfilename)
out_file = open(out_filename, "w")
features_name = []
f_pointer = []
disease_name = []
m_names = m_file.readlines()
m_size = len(m_names)
count = 0

print(m_size)
print(m_names)

while True:
    name = input()
    if name == "exit":
       break
    else:
        disease_name.append(name)
print("passou")
for i in range(0, f_size):
    features_name.append(input())
    f_pointer.append(0)
print("passou")

for line in f_file.readlines():
    line = line.replace("\n", "")
    values = line.split("\t")
    for i in range(0, f_size):
        features[i].append(values[i])

print(len(features[0]))
print("passou")


for i in range(0, len(features[0])/m_size):
    f_count = i%f_size
    for j in range(0, m_size):
        line = count + ";" + m_names[j] + ";" + features_name[f_count] + ";" + features[f_count][f_pointer[f_count]] + ";" + disease_name[f_count] + "\n"
        out_file.write(line)
        f_pointer[f_count] += 1
        count += 1
               


