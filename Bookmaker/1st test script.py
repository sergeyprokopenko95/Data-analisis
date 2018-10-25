import matplotlib.pyplot as plt

plt.figure(0, figsize=(20, 20))
for i in range(100):
    print(i)
    plt.plot(i, i ** 2, 'o')
plt.show()