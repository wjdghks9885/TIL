# Branch 추가 기능

#### 1. Branch 삭제

- 만든 **Branch**를 삭제할 수 있다.

- `git branch -d 브렌치` 이렇게 삭제 가능.

- `-d` 대신 `-D`를 쓰면 묻지도 따지지도 않고 삭제해버린다.~~ㄷㄷ~~

  ```bash
  $ git branch -d 브렌치
  ```


---

#### 2. Branch rebase

> rebase란 이 전 글인 06_Branch_1에 있는 merge와 비슷하다. 작업물 내용을 합친다는 느낌보다는 따로 작업한 이력(commit)들을 합치는 느낌이다.

- log를 볼 때 한결 깔끔하게 보인다.

- 내가 만든 **Branch**를 master **Branch** 위에 **rebase** 시키고 싶을 때 `git rebase master` 이렇게 치면 된다.

  ```bash
  $ git rebase master   # 이 때 내 위치는 내가 만든 브렌치에 있어야한다.
  ```

- 하지만 이러면 master는 여전히 원래 있던 commit을 가리키고 있다.

- master도 최신 commit을 가리키게 하기위해 master로 이동해서 **rebase** 해줘야한다.

  ```bash
  $ git checkout master
  $ git rebase 브렌치
  ```

- 전혀 무슨말인지 모를 수 있다.

- 그래서 사진을 준비했다.

![branch4](https://user-images.githubusercontent.com/49020354/71081578-d6dedd00-21d2-11ea-804b-e7a50f458243.PNG)

- 이렇게 master와 따로 작업하고 따로 commit 후, bugFix라는 내가 만든 **Branch**에서
  - `git rebase master`를 치면

![branchh5](https://user-images.githubusercontent.com/49020354/71081583-db0afa80-21d2-11ea-8df7-a279b67a1604.PNG)

- 이렇게 된다.
- 이 후 `git checkout master`를 쳐서 master **Branch**로 이동한 후 `git rebase 브렌치`(여기선 브렌치 == bugFix)를 치면

![branch7](https://user-images.githubusercontent.com/49020354/71081591-dfcfae80-21d2-11ea-836b-e45fdce53960.PNG)

- 이렇게 같은 곳을 가리키게 된다!

---

#### 3. Branch revert

~~공부 후 추가 예정~~