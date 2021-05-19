# fix a filename extension
exec { 'sed -i s/phpp/php/g /var/www/html/wp-settings.php':
provider => 'shell'
}
