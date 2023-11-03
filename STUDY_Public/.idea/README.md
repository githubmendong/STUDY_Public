# 📎 큰제목

## 조금작은 제목
  - 자기 자신을 호출하는 함수
 

### 문자열의 길이 계산
![image](https://user-images.githubusercontent.com/50076031/123888109-bd088380-d98d-11eb-8345-ce1b7461b0f6.png)



```java
// x: 루트노드, k: 찾는 값
TREE-SEARCH(x, k)
1. if x == NIL or k == key[x]
2.     then return x
3. if k < key[x]
4.     then return TREE-SEARCH(left[x], k)
5.     else return TREE-SEARCH(right[x], k)

시간 복잡도: O(h), h = 트리의 높이
```





### References
- https://readerr.tistory.com/35  
- https://www.youtube.com/channel/UC-cOmaeWLm7Ii7erMQNatvA
- https://www.youtube.com/watch?v=8vDDJm5EewM