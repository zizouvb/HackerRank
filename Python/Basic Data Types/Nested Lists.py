students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name,score])
students.sort(key = lambda l : (l[1], l[0]))
snd_min_score = sorted(list(set([score for name,score in students])))[1]
for name,score in filter(lambda l:l[1]==snd_min_score,students):
    print(name)
