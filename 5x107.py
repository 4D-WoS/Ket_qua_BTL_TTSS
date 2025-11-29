import matplotlib.pyplot as plt

threads = [2, 3, 4, 5, 6, 8, 10, 12, 14, 16]
# Dữ liệu từ ảnh 5x10^7
speedup = [1.885018, 1.885018, 2.035808, 2.212843, 
           2.212843, 2.035808, 2.120648, 2.313445, 
           2.120648, 2.120648]

plt.figure(figsize=(8, 5))
plt.plot(threads, speedup, marker='o', color='g')
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.title("Speedup vs Number of Threads (N = 50,000,000)")
plt.grid(True)
plt.xticks(threads)
plt.show()