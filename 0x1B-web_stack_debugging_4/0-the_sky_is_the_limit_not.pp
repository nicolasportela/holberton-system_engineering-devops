# Issue: Nginx limit to open files is low. Solution: ulimit must be increased (-n flag for open files)
exec { 'sed -i s/.*ULIMIT.*/ULIMIT="-n 4096"/ /etc/default/nginx':
provider => 'shell'
}
