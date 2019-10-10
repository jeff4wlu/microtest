
#!/usr/bin/python 
# -*- coding: utf-8 -*-

import multiprocessing



workers = multiprocessing.cpu_count() * 2 + 1    # 定义同时开启的处理请求的进程数量，根据网站流量适当调整
worker_class = "gevent"   # 采用gevent库，支持异步处理请求，提高吞吐量
bind = "0.0.0.0:8000"    # 监听IP放宽，以便于Docker之间、Docker和宿主机之间的通信

proc_name = 'purchase'
errorlog = '/usr/src/app/log/gunicorn.log'
