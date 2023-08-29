# 💻 RDBMS


>- [1_mariadb-계정-db-만들기.md](1_mariadb-%B0%E8%C1%A4-db-%B8%B8%B5%E9%B1%E2.md)
>- [2_employee_db_install.md](2_employee_db_install.md)
>- [💻 8월 29일 실습.md](%3F%208%BF%F9%2029%C0%CF%20%BD%C7%BD%C0.md)
<br>

# 과제
```sh
- | -- maradb-practice
  - | --sql-practices
  - | --sql-practices
  - | --model
  - | --jdbc-practices
    - | --pom.xml
    - | --src
```
<br>

# 데이터베이스

- 여러 응용 시스템(프로그램)들의 통합된 정보들을 저장하여 운영할 수 있는 공용(share) 데이터의 집합
- 효율적으로 저장, 검색, 갱신할 수 있도록 데이터 집합들끼리 연관시키고 조직화되어야 한다.

# 데이터베이스의 특성

- 실시간 접근성(Real-time Accessability)
- 계속적인 변화(Continuous Evolution)
- 동시 공유성(Concurrent Sharing)
- 내용 참조(Content Reference)

# 데이터베이스 관리 시스템(DBMS)

- 데이터베이스를 관리하는 소프트웨어
- 여러 응용 소프트웨어(프로그램) 또는 시스템이 동시에 데이터베이스에 접근하여 사용할 수 있게 한다.
- 필수 기능: 정의 기능, 조작 기능, 제어 기능

# DBMS의 장점

- 데이터 중복이 최소화
- 데이터의 일관성 및 무결성 유지
- 데이터 보안 보장

# DBMS의 단점

- 운영비가 비싸다
- 백업 및 복구에 대한 관리가 복잡
- 부분적 데이터베이스 손실이 전체 시스템을 정지

# 추가로 알아두면 좋을 내용

- 파일 시스템과의 비교: 데이터베이스는 파일 시스템의 데이터 종속성, 중복성 문제를 보완한다.
- 데이터베이스 관리 시스템의 종류: Oracle, SQL Server, MySQL, DB2 등의 상용 또는 공개 DBMS가 있다.

# 관련된 주요 단어와 그 의미

- 데이터베이스: 여러 응용 시스템(프로그램)들의 통합된 정보들을 저장하여 운영할 수 있는 공용(share) 데이터의 집합
- 데이터베이스 관리 시스템(DBMS): 데이터베이스를 관리하는 소프트웨어
- 정의 기능: 데이터베이스의 논리적, 물리적 구조를 정의하는 기능
- 조작 기능: 데이터를 검색, 삭제, 갱신, 삽입, 삭제하는 기능
- 제어 기능: 데이터베이스의 내용 정확성과 안전성을 유지하도록 제어하는 기능
- 데이터 종속성: 데이터가 다른 데이터와 상호 의존적인 관계를 가지는 것

# 관계형 데이터 베이스
![img_1.png](..%2F..%2FSource_Data%2Fimage_Data%2F01%2Fimg_1.png)

![img_2.png](..%2F..%2FSource_Data%2Fimage_Data%2F01%2Fimg_2.png)

![img_3.png](..%2F..%2FSource_Data%2Fimage_Data%2F01%2Fimg_3.png)








<br> 