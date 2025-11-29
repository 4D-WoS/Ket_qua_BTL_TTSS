import matplotlib.pyplot as plt

threads = [2, 3, 4, 5, 6, 8, 10, 12, 14, 16]
# Dữ liệu từ ảnh 10^8
speedup = [1.719829, 1.926210, 2.049160, 2.239778, 
           2.239778, 2.293102, 2.239778, 2.188865, 
           2.140239, 2.140227]

plt.figure(figsize=(8, 5))
plt.plot(threads, speedup, marker='o', color='r')
plt.xlabel("Number of Threads")
plt.ylabel("Speedup")
plt.title("Speedup vs Number of Threads (N = 100,000,000)")
plt.grid(True)
plt.xticks(threads)
plt.show()