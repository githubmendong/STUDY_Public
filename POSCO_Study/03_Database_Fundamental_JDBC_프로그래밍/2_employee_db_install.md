## employees db install(restore)

알춥파일 경로 찾기
```shell
cd d: 

sftp webmaster@192.168.254.35
````

압축 옮기기
```shell
put employees.zip
````

다시 root 환경으로 넘어와서 webmaster폴더에 있는 zip파일 가져오기
```shell
 mv /home/webmaster/employees_db.zip .
```


압축, 압축풀기 다운로드 / 압축 풀기
```shell
yum install -y zip
yum install -y unzip
unzip employees_db.zip
```

1.  백업 db 압축 풀기
```sh
# unzip employees_db.zip
# ls employees_db
```

2.  employees 데이터베이스 생성 및 hr 계정 생성 및 권한 주기
```sh
# mysql -u root -p
Enter password:
MariaDB [(none)]> create database employees;
MariaDB [(none)]> show databases;
MariaDB [(none)]> create user 'hr'@'192.168.%' identified by 'hr';
MariaDB [(none)]> grant all privileges on employees.* to 'hr'@'192.168.%'; 
MariaDB [(none)]> flush privileges;
MariaDB [(none)]> flush privileges;
MariaDB [(none)]> flush privileges;
```

3.  restore
```sh
# cd employees_db
# mysql -u root -D employees -p < employees.sql
Enter password:
```

마무리

![img.png](img.png)