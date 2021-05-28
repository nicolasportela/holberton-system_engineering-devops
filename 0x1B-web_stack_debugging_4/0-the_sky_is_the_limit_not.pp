# Issue: Nginx limit to open files is low. Solution: ulimit must be increased (-n flag for open files)
exec { 'sed -i s/ULIMIT="-n 15"/ULIMIT="-n 4096"/g /etc/default/nginx && sudo service nginx restart && sudo service nginx reload':
provider => 'shell'
}
