# Github push & pull

> 다른 컴퓨터로 작업하거나 협업을 하기 위해 필요한 기능이다.

- **항상 작업이 끝나면 저장은 Github에 해둔다고 생각해야 한다!**



## 1. clone

> Github 원격 저장소를 복제해오는 기능이다.

- `git clone` 으로 **복제**할 수 있다.

- **복제**를 해야 다른 컴퓨터에서도 같은 원격 저장소에 push할 수 있다.

- **복제**는 처음에 한번만 한다.

  ```bash
  $ git clone https://github.com/wjdghks9885/TIL.git
  ```

  

## 2. push

> 01_Github_TIL.md 에서도 말했지만 add, commit 후 최종적으로 Github 원격 저장소에 push하는 기능이다.

- `git push` 로 **push**할 수 있다.

- **push**를 해야 Github 원격 저장소에 올라간다.

  ```bash
  $ git push origin master
  ```

  

## 3. pull

> 현재 원격 저장소에 있는 내용을 pull해오는 기능이다.

- `git pull` 로 **pull**할 수 있다.

- **pull**을 하지 않고 로컬에서 작업을 할 경우 안좋은 일들이 발생할 확률이 매우 높다.

- 컴퓨터를 켜고 어떤 작업을 하기 전에 무조건 **pull**부터 해라!!!

  ```bash
  $ git pull origin master
  ```



## 4. 그 외 코드들

### (1) 폴더 생성 : `mkdir`

- 현재 디렉토리에 폴더를 생성한다.

  ```bash
  $ mkdir 폴더명
  ```

  

### (2) 파일 생성 : `touch`

- 현재 디렉토리에 파일을 생성한다.

  ```bash
  $ touch 파일명.파일확장자
  ```

  

### (3) log 디테일

- `git log --oneline` : 로그들을 한 줄씩만 보여준다.(핵심 내용만)
- `git log -1` : 마지막 로그만 보여준다.



## 5. Github 기능들

### (1) Fork

- 다른 사람의 원격 저장소를 내 원격 저장소로 가져온다.
- 마치 페이스북 공유하기 같은 느낌이다..
- 가져온 내용들은 내 원격 저장소 내에서는 바꿀 수 있다.



### (2) Issues

- 게시판이다.



### (3) Pull request

- 위에서 설명한 Fork와 연관이 있는 기능이다.
- Fork한 후 내 원격 저장소에서 내용을 바꾸었을 때, Fork해 온 원래 저장소 주인에게 내가 바꾼 내용을 알려주고, 이렇게 바꿔보는 것은 어떻냐라고 요청하는 기능이다.