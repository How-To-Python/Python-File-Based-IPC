# 📖 File Based Interprocess Communication (IPC) 

**File-based IPC is a method where two or more processes communicate by reading and writing to a shared file. One process writes data to the file, and another process reads it to receive updates.**

### 🐦‍🔥 Pros
- Simple to implement
- No socket/network setup needed
- Human-readable state (can manually edit JSON)

### ⚠️ Cons
- Not real-time (polling delay)
- File I/O overhead
- Potential race conditions if both processes write simultaneously
- Not suitable for high-frequency updates
 

### Demonstrations
- [File Based IPC Basic Demo](./Demo1/DEMO1.md)
    - Rerender Updates
- [File Based IPC Enhanced Demo](./Demo2/DEMO2.md)
    - Live Updates
- [More about IPC](./Notebooks/InterprocessCommunication.ipynb)

**Note**: *This demo repository is for educational purposes to understand IPC concepts. For production use, consider more robust IPC mechanisms like message queues, sockets, or dedicated IPC libraries.*