units = {'B': 0, 'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4}
a = list(units.keys())
print(
    a[a.index('B') + 1]
)
