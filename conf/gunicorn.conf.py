import multiprocessing
import uvicorn

workers = multiprocessing.cpu_count() + 1
bind = '0.0.0.0:8000'
worker_class = 'uvicorn.workers.UvicornWorker'