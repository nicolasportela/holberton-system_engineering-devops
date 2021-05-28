# Issue: Nginx limit to open files is low. Solution: ulimit must be increased (-n flag for open files)
exec { 'limit':
command => 'sed -i s/ULIMIT="-n 15"/ULIMIT="-n 4096"/g /etc/default/nginx',
path => '/etc/default/nginx'
}
