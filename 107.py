import matplotlib.pyplot as plt

threads = [2, 3, 4, 5, 6, 8, 10, 12, 14, 16]
speedup = [1.683238, 1.683238, 1.683238, 1.442792,
           1.683238, 2.019950, 1.442743, 1.683238,
           1.442882, 2.019950]

plt.figure(figsize=(8, 5))
plt.plot(threads, speedup, marker='o')
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.title("Speedup vs Number of Threads (OpenMP)")
plt.grid(True)

plt.show()
