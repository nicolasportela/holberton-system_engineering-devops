# Issue: Nginx limit to open files is low. Solution: ulimit must be increased (-n flag for open files)
exec { 'sed -i s/15/4096/g /etc/default/nginx':
provider => 'shell'
}
