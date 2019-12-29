# Pandas에 숨어있는 꿀 함수 발견

## 그것은 바로 `transform`

> 바로 data frame에 사용하진 않고 groupby 후에 사용한다.

```python
import pandas as pd
# 데이터 프레임이 있다는 가정 하에

df.groupby('col1')['col2'].mean().reset_index()
```

- 이 코드와

```python
df.groupby('col1')['col2'].transform('mean')
```

- 이 코드는 얼핏보면 같은 기능을 하는 코드인 것처럼 보인다.
- 맞다. 두 코드 모두 col1의 데이터 카테고리 별로 col2의 평균을 계산해주는 코드이다.
- 하지만 결과물이 다르다.
- 첫번째 코드는 대표값들만 data frame 형식으로 반환된다.
- 두번째 코드는 데이터 프레임의 길이에 맞춰서 Series로 반환된다.

---

- 결과물과 상세 내용이 궁금하다면 [여기](https://github.com/wjdghks9885/TIL/blob/master/my_code/pandas_transform.ipynb)를 클릭해서 출력 결과까지 같이 볼 수 있다!