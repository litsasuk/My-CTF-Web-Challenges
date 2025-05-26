FROM php:7.4-apache

COPY ./flag /root
COPY ./readflag /
COPY ./html/ /var/www/html/
COPY ./php.ini /usr/local/etc/php/php.ini

RUN chmod 755 /var/www/html && chown -R root:www-data /var/www/html && chmod 400 /root/flag && chmod 4111 /readflag
