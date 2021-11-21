with open("dir.txt", encoding='utf8') as f:
    lines = f.read().splitlines()
    f.close()

mdfiles = []
for line in lines:
    if line.endswith('.md)'):
        # print(line)
        mdfiles.append(line)

no_space = []
for file in mdfiles:
    num = int(file.split("[")[1].split(".")[0])
    print(num)
    http_part = file.split("(")[-1].split(")")[0].replace("  ", "%20-%20").replace(" ", "%20")
    name_part = file.split("(")[0]
    no_space.append(name_part + http_part)

sorted(mdfiles, key=lambda x: int(x.split("[")[1].split(".")[0]))

with open("dir.txt", 'w', encoding='utf8') as f:
    for line in mdfiles:
        f.write("- " + line)
        f.write("\n")
        f.write("\n")
    f.close()