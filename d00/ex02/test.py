from tinyStatistician import TinyStatistician

a = [1, 2, 3, 4, 5, 6 ,7, 8, 9]
b = []
for i in range(1, 101):
    b.append(i)
print(b)
print(TinyStatistician().mean(a))
print(TinyStatistician().median(b))
print(TinyStatistician().quartile(b, 50))
print(TinyStatistician().var(b))
print(TinyStatistician().std(b))