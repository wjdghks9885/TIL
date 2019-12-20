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

#### 3. Branch reset

- commit한(변경한) 내용을 되돌리는 방법이다.

- `git reset` 은 이전의 commit을 가리키게 한다.

- 애초에 commit 하지 않은 것처럼 예전 commit으로 **Branch**를 옮긴다.

- 그래서 협업할 때 맘대로 `reset` 했다가는 기록도 남지 않아서 망할 수가 있다.

  ```bash
  $ git reset HEAD
  ```

  - 이렇게 하면 `reset`된다!

---

#### 4. Branch revert

- 위에서 언급한 *reset*과 비슷한 맥락이지만 다르다!

- *reset*은 이전의 commit을 가리키지만 `revert`는 변경 전의 내용을 담은 새로운 커밋이 생긴다.

- *reset*은 기록을 남기지 않지만 `revert`는 기록을 남긴다.

- 남은 기록은 push하면 협업하는 다른 사람에게도 보인다.

- 그래서 되돌린 내용을 공유하기 위해서는 `revert`를 써야한다!

  ```bash
  $ git revert HEAD
  ```

  - 이렇게 하면 `revert`된다!

---

### Branch의 기본적(?)인 내용들을 어느정도 다뤄봤다.

- 아직은 취직도 안했고, 협업할 때도 git을 사용해본적이 없어서 **Branch**를 많이 다뤄보진 않았지만 이번에 공부하면서 조금은 알게된 것 같다.
- 앞으로 회사에서 일을 하게 되면 git을 많이 사용할 것 같은데, 그래서 기본적인 부분들은 할 줄 알아야 한다고 생각한다.
- github에 올리고 내리고 하는 것은 계속 진행할 것이고,  이번 내용 막판에 말투가 은근 딱딱해진 것 같아 부드럽게 끝내야겠다. ㅎ
- **TIL**을 매일 올리려 노력 중이지만 꽤 힘들다,,
- 프로젝트도 있고, 토익도 있고(?)
- 2020년 1월 초만 지나면 앞으로 꾸준히 올릴거다.ㅎㅎ