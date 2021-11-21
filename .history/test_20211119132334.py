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

    no_space.append(file.split("(")[-1].split(")")[0].replace("  ", "%20-%20").replace(" ", "%20"))

sorted(mdfiles, key=lambda x: int(x.split("[")[1].split(".")[0]))

with open("dir.txt", 'w', encoding='utf8') as f:
    for line in mdfiles:
        f.write("- " + line)
        f.write("\n")
        f.write("\n")
    f.close()