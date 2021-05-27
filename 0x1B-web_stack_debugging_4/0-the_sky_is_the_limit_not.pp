# added option -l to make ApacheBench accept variable document length
exec { 'ab -c 100 -n 2000 -l localhost/':
provider => 'shell'
}
