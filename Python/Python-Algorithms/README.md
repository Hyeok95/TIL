# Python Algorithm

## 1. 분할정복법

* 문제를 소문제로 분할
* 각각의 소문제를 해결
* 소문제의 해결결과를 이용해 전체문제를 해결.

(분할정복법은 어렵지만 수학적 문제해결 능력이 가장 중요하므로 노트와 펜을 들고 생각하면 쉬움!)

## 2. 완전탐색 알고리즘

* 그냥 완전히 다 탐색하는것
1. 문제의 가능한 경우의 수를 모두 시도해 본다.
2. 문제가 주어지면 무조건 완전탐색법으로 먼저 시도해본다..
3. 실제 답을 구할 수 있는지 적용한다.

방법)

* 반복,조건문을 활용해 모두 테스트하는 방법.
* 순열
* 재귀 호출
* 비트마스크(2진수 표현)
* BFS, DFS 이용.


## 3. 우선순위 큐
* 최대 힙 <br>
각 노드의 키 값이 그 자식의 키 값보다 작지 않은 트리 <br>
(부모 노드는 자식 노드보다 작지만 않으면 된다. + 완전이진트리이다.)

* 최소 힙 <br>
각 노드의 키 값이 그 자식의 키값보다 크지 않은 트리 <br>
(부모 노드는 자식 노드보다 크지만 않으면 된다. + 완전이진트리이다.)

```python
import heapq #모듈 사용
```

## 4. DFS, BFS
* DFS : 깊이 우선 탐색이며, 최대한 깊이 내려간 뒤, 더 이상 깊이 갈 곳이 없을 경우 옆으로 이동
* BFS : 너비 우선 탐색이며, 최대한 넓게 이동한 다음, 더 이상 갈 수 없을 때 아래로 이동

## 5. 기타
* itertool : combinations(조합), permutations(순열)을 사용
* Counter : 주어진 단어에서 가장 많이 등장하는 알페벳과 그 알파벳의 개수를 구하는 함수는 다음과 같이 마치 사전을 이용하듯이 작성(dictionary를 안써도 됨)
* extend() : append와 동일하게 array끝의 추가하지만 자료형이 아닌 것도 추가할 수 있음
