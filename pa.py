import urllib2 
Response=urllib2.urlopen("http://www.verycd.com");
Html=Response.read();
print Html;