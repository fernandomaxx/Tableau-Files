file_list = []
class_list = []
m_list = []
disease_list = []
f_pointer = []
path_config = "configs/" + input() + ".txt"
out_file = open("out/"input(), "w")
config = open(path_config)
out_file.write(config.readline())
path_files = config.readlines()

for path in path_files:
    file_list.append(open(path.replace("\n", "")))

for line in file_list[0]:
    m_list.append(line.replace("\n", ""))

for line in file_list[1]:
    disease_list.append(line.replace("\n", ""))

for line in file_list[2]:
    class_list.append(line.replace("\n", ""))
    f_pointer.append(0)

class_size = len(class_list)
m_size = len(m_list)
path = path_files[1].replace("paths.txt\n", "")
class_values = [[] for _ in range(class_size)]

for i in disease_list:
    for line in open(path + i + ".txt").readlines() :
        line = line.replace("\n", "")
        values = line.split("\t")
        for i in range(0, class_size):
            class_values[i].append(values[i])

d_count = 0
count = 0
for i in range(0, int(len(class_values[0])/m_size) * class_size):
    f_count = i%class_size
    for j in range(0, m_size):
        line = str(count) + ";" + m_list[j] + ";" + class_list[f_count] + ";" + class_values[f_count][f_pointer[f_count]] + ";" + disease_list[d_count] + "\n"
        out_file.write(line)
        f_pointer[f_count] += 1
        count += 1
    if f_count == class_size - 1:
        d_count += 1

out_file.close()
               


