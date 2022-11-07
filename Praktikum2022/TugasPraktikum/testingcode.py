x = []
q = 2
while q<252:
    q+=4
    x.append(f"200.100.10.{q}")


with open("readme2.txt", "w") as f:
    for i in x:
        f.write(f"{i}\n")