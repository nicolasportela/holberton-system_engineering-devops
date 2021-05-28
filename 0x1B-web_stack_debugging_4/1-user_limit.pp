# setting user holberton limits
exec { 'sed -i s/4/100000/g /etc/security/limits.conf && sed -i s/5/100000/g /etc/security/limits.conf:
provider => 'shell'
}
