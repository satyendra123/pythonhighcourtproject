# pythonhighcourtproject
python high court project with p10 display

1) i want to connect 10 mysql database which sends their data to master computer mysql database. to make it work properlly what will i do is.
   1st of form i will make the master computer apache server to work as a server and can connect with the ip. so we will open the xamp go to the apache>config>apache(httpd.conf) file ke andar jaha par #Listen 80 likha hoga usko # se comment karke us line ke niche wali line par  Listen 192.168.1.50:80 likh denge. aur yad rahe ki apne system ki ip bhi same yahi honi chahiye jo humne apache server ke httpd.conf file me likha tha.

2) 2nd step is that we will go apache>config>apache(httpd-xampp.conf) file me jayenge aur jaha par require local likha hoga usko hum change kar denge require all grated se kuch is tarah se
                                                 Alias /phpmyadmin "C:/xampp/phpMyAdmin/"
                                            <Directory "C:/xampp/phpMyAdmin">
                                                  AllowOverride AuthConfig
                                                  Require all granted
                                                  ErrorDocument 403 /error/XAMPP_FORBIDDEN.html.var
                                            </Directory>

3) in the 3rd part what will we do is we will open the windows firewall> inbound rules > New Rule > Port > specific local ports enter 80, 8080, 443 in name write anything like housys. after doing all these things our setup is ready.

4) in the fourth part connect your server computer to a switch through a lan cable. and connect another computer with it which works as a client. the client ip is also in the series of 1 like 192.168.1.100 something like that. now we can test it. we will open the xamp with http://localhost/phpmyadmin/ instead of this we will
write http://192.168.1.100/phpmyadmin. if i open this what we will see in the client pc same sql is running which is running on the master PC.
