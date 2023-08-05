import os, string, random, hashlib, psutil, time
from multiprocessing import Process, Event, Queue




__all__=['get_random_string', 'get_md5', 'monitor_usage']
def get_random_string(l=10):
    letters = string.digits + string.ascii_letters
    return ''.join(random.choice(letters) for i in range(l))


def get_md5(txt):
    md5hash = hashlib.md5(str(txt).encode('utf-8'))
    return md5hash.hexdigest()

def monitor_usage(sample_interval, func, *args, **kwargs):
    def sample_func(process, sample_interval, stop_event, queue):
        while not stop_event.is_set():
            time.sleep(sample_interval)
            cpu_percent = process.cpu_percent()
            mem_info = process.memory_info()
            mem_usage = mem_info.rss / 1024 / 1024
            if queue.full():
                queue.get()
            queue.put((cpu_percent, mem_usage))

    pid = os.getpid()
    p = psutil.Process(pid)
    init_cpu_percent = p.cpu_percent()
    mem_info = p.memory_info()
    init_mem_usage = mem_info.rss / 1024 / 1024

    stop_event = Event()
    queue = Queue(maxsize=1000)
    proc = Process(target=sample_func, args=(p, sample_interval, stop_event, queue))
    proc.start()
    ret = func(*args, **kwargs)
    stop_event.set()
    proc.join()
    cpus = []
    memories = []
    for i in range(queue.qsize()):
        cpu_percent, mem_usage = queue.get()
        mem_usage -= init_mem_usage
        cpus.append(cpu_percent)
        memories.append(mem_usage)
    stat = {'max_cpu_usage': max(cpus), 'max_mem_usage': max(memories), 
            'avg_cpu_usage': sum(cpus)/len(cpus), 'avg_mem_usage': sum(memories)/len(memories)}
    return ret, stat

