FROM daocloud.io/python:3.5

WORKDIR /usr/src/app
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN echo 'Asia/Shanghai' >/etc/timezone
COPY requirements.txt ./
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "purchase:app", "-c", "./gunicorn.conf.py"]
