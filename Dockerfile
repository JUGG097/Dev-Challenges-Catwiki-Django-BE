FROM python:3.9-buster

RUN apt-get update && apt-get install nginx vim -y --no-install-recommends
COPY config/nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log
# RUN apt-get update
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
COPY requirements.txt config/start-server.sh manage.py /opt/app/
RUN chmod +x /opt/app/start-server.sh 
# COPY .pip_cache /opt/app/pip_cache/
COPY api /opt/app/api/
COPY base /opt/app/base/
WORKDIR /opt/app
# RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /opt/app

# Removes windows related spacing issues
RUN apt-get install -y dos2unix # Installs dos2unix Linux
RUN find . -type f -exec dos2unix {} \;

EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
# CMD gunicorn base.wsgi --user www-data --bind 0.0.0.0:8010 & nginx -g "daemon off;"
# ENTRYPOINT ["sh", "/opt/app/start-server.sh"]
# CMD python manage.py runserver