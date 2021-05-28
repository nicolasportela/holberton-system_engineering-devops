# setting user holberton limits
exec { 'sed -i s/nofile/nofile 100000/g /etc/security/limits.conf':
provider => 'shell'
}