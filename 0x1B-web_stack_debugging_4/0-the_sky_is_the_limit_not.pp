# Issue: Nginx limit to open files is low. Solution: ulimit must be increased (-n flag for open files)
exec { 'sed -i s/15/30000/g /etc/default/nginx':
provider => 'shell'
}
