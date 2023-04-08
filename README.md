# wnflbsign
福利吧签到脚本
拉库地址：

ql repo https://github.com/twthblzhm/wnflbsigng.git


任务定时：
0 0 2,6 * * *
上面的意思是每天2点和6点各运行一次签到（防止漏签），也可以自行修改
0 0 3 * * *   
这个是每天3点触发

环境变量：
需要添加两个环境变量，新建变量时名称直接添加即可，不要加符号
FUBA
FUBAUN
然后，值然添加
FUBA的值是填写cookie
FUBAUN的值填写论坛里的用户名，判断是否登录成功，cookie是否失效
