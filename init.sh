sudo rm -rf /etc/nginx/sites-enabled/default
sudo ln -sf /home/box/web/etc/stepic191.conf  /etc/nginx/sites-enabled/stepic191.conf
sudo /etc/init.d/nginx restart