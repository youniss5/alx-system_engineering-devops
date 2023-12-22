#!/usr/bin/pup
# install flask from pip3
package { 'flask':
	ensure   => '2.5.0',
	provider => 'pip3',
}
