FROM python:3.9-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY config/nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
COPY requirements.txt config/start-server.sh manage.py /opt/app/
# COPY .pip_cache /opt/app/pip_cache/
COPY api /opt/app/api/
COPY base /opt/app/base/
WORKDIR /opt/app
# RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /opt/app

EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
