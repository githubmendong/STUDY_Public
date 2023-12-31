#poscodx #spring #05spring 
2023 09 19


## AOP (Aspect-Oriented Programming)
AOP는 관점(Aspect) 지향 프로그래밍으로 관점을 어디에 두냐에 따라 보는 프로그래밍이다.
> 관점이란, 부가기능과 그 적용처를 정의하고 합쳐서 모듈로 만든 것.

![](..%2F..%2Fassiset/Pasted%20image%2020230919104650.png)

## AOP 의 목적
OOP와 이르미비슷하여 상반된 개념같지만, 관점지향 프로그래밍은 객체지향 프로그래밍을 보완하기 위해 쓰인다. 기존 객체(Object) 지향은 목적에 따라 클래스를 만들고 객체를 만들었다. 따라서 핵심 비즈니스 로직이든, 기능들을 어떻게 바라볼지에 따라 정의가 부족한점도 있다.
![](../../../assiset/Pasted%20image%2020230919103045.png)
## AOP 적용방식
* 컴파일 시점 적용
* 클래스 로딩 시점 적용
* 런타임 시점 적용 

## Spring AOP

Spring AOP는 **런타임 시점**에 적용하는 방식을 사용한다.
컴파일 시점과 클래스 로딩 시점에 적용하려면 별도의 컴파일러와 클래스로더 조작기를 정하고 사용 및 유지하는 과정이 어렵기 때문.


## AOP 용어 및 개념

![](..%2F..%2Fassiset/Pasted%20image%2020230919104010.png)
- **Aspect**
    - 공통 기능
    - 어드바이스 + 포인트컷을 모듈화한 애플리케이션의 횡단 기능
- **Join Point**
    - 애플리케이션 실행 흐름에서의 특정 포인트 (ex. 클래스 초기화, 메서드 호출, 예외 발생 등)
    - 한 마디로 AOP를 적용할 수 있는 모든 지점 (스프링에서는 메서드 실행 지점으로 제한)
- **Advice**
    - 조인포인트에서 실행되는 코드 즉 부가기능 그 자체
    - 에스팩트를 언제 핵심 코드에 적용할지 정의

| Type            | 설명                                                     |
| --------------- | -------------------------------------------------------- |
| Before          | 조인포인트 실행 이전에 실행, 일반적으로 리턴타입 void    |
| After returning | 조인포인트 완료후 실행 (ex. 메서드가 예외없이 실행될 때) |
| After Throwing  | 메서드가 예외를 던지는 경우 실행                         |
| After (finally) | 조인포인트의 동작과 관계없이 실행                        |
| Around          | 메서드 호출 전후에 수행 가장 강력한 어드바이스이다.      |

**수행 ,** (조인포인트 실행 여부 선택, 반환 값 변환, 예외 변환, try~catch~finally 구문 처리 가능 등)

- Pointcut
    - 조인포인트 중 어드바이스가 적용될 지점을 선별하는 기능
    - 주로 AspectJ 표현식으로 지정

- Target
    - 핵심 기능을 담은 모듈 (=부가 기능 부여 대상)
    - 어드바이스를 받는 객체이고, 포인트컷으로 결정된다
- Advisor
    - 스프링 AOP에서만 쓰는 용어로, 하나의 어드바이스와 하나의 포인트컷으로 

![](..%2F..%2Fassiset/Pasted%20image%2020230919104640.png)

### AOP가 필요한 상황
* 모든 메소드 호출 시간을 측정할때
* 공통 관심 사항 (cross-cutting concern) vs 핵심 관심 사항(core concern)
* 회원 가입 시간, 회원 조회 시간을 측정하고 싶을 때

![](..%2F..%2FassisetPasted%20image%2020230919095321.png)



