# Branch

> Branch란 간단하게 말하자면 개발의 편의를 위하여 원본파일을 건들지 않고 복사하여 진행하는 일종의 평행 개발공간이다.

- 그림을 보면 이해가 더 쉬울 것이다.

![branch 그림](http://woowabros.github.io/img/2017-10-30/git-flow_overall_graph.png)



## 간단한 Branch 실습

#### 1. Branch 만들기

- **Branch** 만드는 방법은 쉽다. `git branch 브렌치` 이런 식으로 만든다.

  ```bash
  $ git branch 브렌치
  ```

  - 코드 치는 순간 브렌치가 생긴다.

---

#### 2. Branch로 이동

- 방금 만든 **Branch**로 이동하는 방법 또한 쉽다. `git checkout 브렌치` 이렇게 이동할 수 있다.

  ```bash
  $ git checkout 브렌치
  ```

  - 코드 치는 순간 언급한 브렌치로 이동한다.

---

#### 3. Branch commit

> 위에서 말 했다시피 Branch는 다른 공간이다. 그래서 commit과 push도 할 때 다른 공간에서 이루어진다.

- master 말고 다른 **Branch**에서 작업한 작업물을 commit할 수도 있다.

- 방법은 master에서 commit할 때와 똑같다.

  ```bash
  $ git add 
  $ git commit -m "메세지"
  ```

  - 이러면 commit 된다.

---

#### 4. Branch push

- master 말고 다른 **Branch**도 원격 저장소에 push할 수 있다.

- 방법은 master를 push할 때와 같은데, 뒤에 **Branch** 이름만 push할 **Branch** 이름을 써주면 된다.

  ```bash
  $ git push origin 브렌치
  ```

  - 이렇게 치고 엔터를 누르면 push되고, 원격 저장소에 가서 push한 **Branch**를 확인할 수 있다.

---

#### 5. Branch merge

- 새로 만든 **Branch**는 별도로 작업하는 공간이었다.

- 여기서 작업한 내용물이 Good idea일 경우, 최종 결과물이 있는(?) 모든 이들과 공유하는 공간인 master에 올려야 할 것이다.

- 이를 수행하는 방법이 또 있다. `git merge 브렌치` 이런 코드이다.

  ```bash
  $ git checkout master  # 일단 master로 이동
  $ git merge 브렌치
  ```

  - 이렇게 하면 master는 내 **Branch**에서 수정한 내용들이 반영된다.
  - 하지만 이러면 master는 제대로 수정되어 신버전이지만 내 **Branch**는 수정되어 있긴하지만 구버전이다.
  - 이를 해결하려면 내 **Branch**에서도 master를 merge시켜야 한다.

  ```bash
  $ git checkout 브렌치   # 내 브렌치로 이동
  $ git merge master
  ```

  - 이렇게 하면 내 **Branch**도 수정된 신버전이 된다.ㅎㅎ

- 이해가 안 될 수도 있다. 그래서 그림을 첨부해본다.

![branch1](https://user-images.githubusercontent.com/49020354/71080118-ddb82080-21cf-11ea-9f78-cc338e9b843d.PNG)

- bugFix가 내 **Branch**라고 생각하고 봐라.
- 그리고 *(별표)표시 있는 **Branch**가 현재 내가 있는 **Branch**이다.
- 여기서 merge를 하면 이렇게 된다.

![branch2](https://user-images.githubusercontent.com/49020354/71080150-f0caf080-21cf-11ea-9706-b34b178163fd.PNG)

- 위에서 말한대로 합쳐진 커밋(신버전)을 master만 가리키고있다.
- 수정되긴 했지만 구버전인 c2를 bugFix(내 **Branch**)가 가리키고 있다.
- 여기서 위에 언급한대로 내 **Branch**로 이동하여 master에 merge하면 어떻게 되는지 보자.

![branch3](https://user-images.githubusercontent.com/49020354/71080157-f45e7780-21cf-11ea-8824-3c79708bd317.PNG)

- 이렇게 수정된 신버전 커밋을 내 **Branch**도 가리키게 된다!

> 이걸 봐도 뭔 소린지 모를 수도 있다. 그럴 땐 [branch 실습 사이트](https://learngitbranching.js.org/?locale=ko) 여기에 가서 연습할 수 있다.

---

- 일단 오늘 해 본 것은 여기까지이다.
- 내일 다른 기능들을 실습해보고 올릴 예정이다.