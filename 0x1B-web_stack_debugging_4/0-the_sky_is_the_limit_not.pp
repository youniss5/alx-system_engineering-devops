#increase Nginx server handling 

#ULIMIT increase
exec { 'fix--for-nginx':
# increase the ULIMIT
  command => 'bin/sed -i "s/15/4096/" /etc/default/nginx',
#Path
  path    => '/usr/local/bin/:/bin/'
} ->

# (Nginx) Restart.
exec { 'nginx-restart':
#Restart
  command => 'etc/init.d/nginx restart',
#Path
  path    => '/etc/init.d/'
}
