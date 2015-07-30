import urllib2

for line in urllib2.urlopen('http://geefu.io'):
    print line
