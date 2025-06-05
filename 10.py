import fileinput
filepath = 'data/test.txt'
table = []
sum = 0
class route():
    def __init__(self, start):
        self.start = start
        self.score = 0

for line in fileinput.input(filepath, inplace = False):
    table.append(list(map(int,line.rstrip())))

routes = []
for i in range(0,len(table)):
    for j in range(0,len(table[0])):
        if table[i][j] == 0:
            routes.append(route([i,j]))



def mapRoute(i,j):

    return

for t in table:
    print(''.join(map(str, t)))

print("")

for r in routes:
    print(r.start)
        