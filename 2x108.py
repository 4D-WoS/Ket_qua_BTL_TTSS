import matplotlib.pyplot as plt

threads = [2, 3, 4, 5, 6, 8, 10, 12, 14, 16]
# Dữ liệu từ ảnh 2x10^8
speedup = [1.598171, 2.013696, 2.165264, 2.341499, 
           2.426139, 2.369051, 2.212854, 2.237440, 
           2.314594, 2.237440]

plt.figure(figsize=(8, 5))
plt.plot(threads, speedup, marker='o', color='m')
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.title("Speedup vs Number of Threads (N = 200,000,000)")
plt.grid(True)
plt.xticks(threads)
plt.show()