import matplotlib.pyplot as plt

threads = [2, 3, 4, 5, 6, 8, 10, 12, 14, 16]
# Dữ liệu từ ảnh 2x10^7
speedup = [1.670358, 1.670322, 1.413368, 1.413368, 
           1.531139, 1.837382, 1.837382, 2.041519, 
           2.041573, 1.837382]

plt.figure(figsize=(8, 5))
plt.plot(threads, speedup, marker='o', color='b')
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.title("Speedup vs Number of Threads (N = 20,000,000)")
plt.grid(True)
plt.xticks(threads) # Đảm bảo hiện đủ các mốc thread
plt.show()