FROM php:7.2-apache

COPY ./flag /root
COPY ./readflag /
COPY ./html/ /var/www/html/
COPY ./php.ini /usr/local/etc/php/php.ini
COPY ./readflag /readsecret

RUN chmod 755 /var/www/html && chown -R root:www-data /var/www/html && chmod 400 /root/flag && chmod 4111 /readflag && chmod +x /root/flag.sh && chmod 4111 /readsecret
