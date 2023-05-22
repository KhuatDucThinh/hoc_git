from queue import Queue

q = Queue(maxsize=5)  # Tạo một Queue với giới hạn tối đa là 5 phần tử
q.put(1)
q.put(2)
q.put(3)
print(q.get())  # In ra phần tử đầu tiên của Queue (1)

