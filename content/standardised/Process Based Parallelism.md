---
aliases: 
category: DS
date modified: 27-07-2025
tags:
  - system
---
## What Is Process-Based Parallelism?

Process-based parallelism refers to the practice of running code ==concurrently== using multiple independent processes, each with its own Python interpreter and memory space. This contrasts with [[thread-based parallelism]], where threads share memory and state.

In Python, this approach is typically implemented using the `multiprocessing` ([[Multiprocessing]]) module or `concurrent.futures.ProcessPoolExecutor`.

### Why Use Processes Instead of Threads?

| Threads                                        | Processes                           |
| ---------------------------------------------- | ----------------------------------- |
| Share memory                                   | Independent memory space            |
| Best for I/O-bound tasks                       | Best for CPU-bound tasks (like OCR) |
| GIL (Global Interpreter Lock) limits CPU usage | Bypasses GIL (real parallelism)     |
| Lightweight, faster to start                   | Heavier, more isolation             |

Your case (OCR via `easyocr`) is CPU-bound, since image decoding and deep learning inference take significant CPU/GPU time, and it benefits from real parallelism — thus, processes are ideal.
### Technical Details

* `ProcessPoolExecutor` (from `concurrent.futures`) allows easy mapping of functions to multiple processes.
* Each image is passed to a worker process as a path.
* Each worker instantiates its own `easyocr.Reader` (this is key — `Reader` is not thread-safe or shareable across processes).
* The main process aggregates the results and writes to disk.

### Basic Function Signature in This Pattern

This function will be run by many processes in parallel.
### Advantages for You

* Scale to multiple cores automatically.
* No need for locks or shared memory handling.
* Each image is processed in isolation — no interference.
* Simple to retry if something fails (can rerun the notebook and it picks up unprocessed files).
### Practical Caveats

* You cannot share global objects like `easyocr.Reader` or open file handles across processes.
* Startup time is higher due to process creation and model loading per worker.
* Jupyter Notebook environments may be finicky with multiprocessing; safer to run this as a script.
