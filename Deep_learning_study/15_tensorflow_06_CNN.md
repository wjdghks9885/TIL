# CNN(Convolutional Neural Network)

> 이미지 분석에 활용 되는 딥러닝 모델이다.

<img src="https://user-images.githubusercontent.com/49020354/77286551-d47ea880-6d16-11ea-9077-7900b19c4e48.PNG" style="zoom:70%;" />

- CNN의 기본 구조

<br>

- CNN의 시작은 고양이 실험에서 시작되었다.
  - 고양이에게 어떤 형태의 그림을 보여줬을 때, 그림을 읽어들이는 뉴런들이 동시에 다 동작하는 것이 아니라 어떤 형태의 그림 또 어떤 부분의 그림들에 대해서만 반응 한다는 것을 알게 되었다.
  - 부분마다 다르게 입력받는 것이었다.
  - 이를 이용하여 알고리즘을 개발하였고, 성능도 꽤 좋았다.

<br>

- 이 모델이 이미지를 처리하는 방법에 대해서 알아보자.
- 한번에 이미지 전체를 학습하는 것이 아니라 필터를 이용해 이미지의 일부분만 먼저 처리한다.

![캡1](https://user-images.githubusercontent.com/49020354/77038648-a12ad980-69f7-11ea-841c-39bba0fb4c74.PNG)

- 이렇게 32x32의 이미지가 있을 때, 5x5(필터 사이즈는 자유)의 필터로 이미지의 일부분을 먼저 보는 것이다.
- 필터는 궁극적으로 한 값을 만들어낸다.
- 필터가 어떻게 5x5 총 25개의 값을 하나의 값으로 만들어낼까?

![캡2](https://user-images.githubusercontent.com/49020354/77039227-d84dba80-69f8-11ea-8a15-e7e55f57b9ce.PNG)

- 이런식으로 계속 봐왔던 `Wx+b`의 형태로 하나의 값을 도출해낸다.
  - W가 필터, x는 이미지의 픽셀 값.
- 이렇게 필터가 이미지의 부분들을 돌아다니면서 값들을 도출해낸다.

<img src="https://user-images.githubusercontent.com/49020354/77039927-4ba3fc00-69fa-11ea-96e4-03175c2d203c.PNG" style="zoom:50%;" /> <img src="https://user-images.githubusercontent.com/49020354/77039933-4e065600-69fa-11ea-8b41-5ad1cca77faf.PNG" style="zoom:50%;" /> <img src="https://user-images.githubusercontent.com/49020354/77039951-58285480-69fa-11ea-8cfa-f6a5c3f7ae0b.PNG" style="zoom:50%;" /> <img src="https://user-images.githubusercontent.com/49020354/77039960-5a8aae80-69fa-11ea-8f21-238590e6dc76.PNG" style="zoom:50%;" />

<img src="https://user-images.githubusercontent.com/49020354/77039966-5ced0880-69fa-11ea-8a3c-e959749a2881.PNG" style="zoom:80%;" />

- 이렇게 필터를 옮겨가면서 계산한다. (그림은 옆으로만 갔지만 아래로도 간다.)
- 7x7의 이미지에 3x3필터를 한 칸씩 이동하며 적용했으니 output은 5x5가 나올것이다.
  - 여기서 한 칸씩 이동하는 것을 "stride의 크기가 1이다."라고 한다.
- 만약 두 칸씩 이동한다면 stride는 2이고, output은 3x3이 될 것이다.

<img src="https://user-images.githubusercontent.com/49020354/77040409-39768d80-69fb-11ea-9b6d-2437469a7e02.PNG" style="zoom:80%;" />

- 이렇게 말이다.

- 그리고 output의 shape이 어떻게 될지 쉽게 계산하는 방법도 있다.

<img src="https://user-images.githubusercontent.com/49020354/77043222-67120580-6a00-11ea-89d7-48348290dfb4.PNG" style="zoom:80%;" />

- ((이미지shape - 필터shape) / stride) + 1 이다.

<br>

### padding

- padding(패딩)이란 이미지의 주변에 값이 0인 픽셀들을 만들어주는 것이다.

<img src="https://user-images.githubusercontent.com/49020354/77283916-d2b1e680-6d10-11ea-85bf-ef5af942d487.PNG" style="zoom:80%;" />

- 이렇게 하는데에는 2가지 이유가 있다.
  - 하나는 이미지가 급격하게 작아지는 것을 방지하는 이유이다.
  - 또 하나는 모서리 부분을 네트워크에 어떻게든 알려주고 싶어서이다.
- padding을 할 때, 일반적으로 원래 input 사이즈와 output사이즈가 같게 만들어준다.

<br>

### convolution layer

- CNN에서 convolution layer를 지날 때 output 이미지 크기는 filter의 크기와 stride에 따라 결정된다.
  - 하지만 크기를 제외한 나머지 차원의 shape은 filter의 개수로 결정된다.

<img src="https://user-images.githubusercontent.com/49020354/77285028-6f758380-6d13-11ea-902d-26584039bb52.PNG" style="zoom:80%;" />

- 이렇게 6개의 filter를 사용하여 6개(?)의 이미지가 나오게 된다.
  - 다르게 말하면 "filter의 개수 == node의 개수" 이렇게 말할 수도 있다.
  - "이 층에서 filter를 6개를 지난다." == "이 층의 node의 개수는 6개이다."
- 그리고 convolution layer도 여러 개를 사용할 수 있다.
- 또, 한 층에 5x5x3 filter가 6개 있다면 그 층에서 조정되면 weight 값은 5 x 5 x 3 x 6 = 450개가 된다.
- 일반적인 딥러닝 모델과 똑같이 convolution layer에서는 ReLU 사용.

<br>

### max pooling(pooling layer)

> pooling중에서 max값을 뽑아내는 것이 max pooling인데, 보통 max pooling을 사용하기 때문에 max pooling이라 적었다.

- filter처럼 이동하면서 이미지를 보게 되는데, 2x2 filter로 max pooling 한다면 4칸 중에 가장 큰 값만 뽑아내서 1칸으로 만들어준다.(4칸 -> 1칸)

<img src="https://user-images.githubusercontent.com/49020354/77286361-689c4000-6d16-11ea-9697-c19d684364fa.PNG" style="zoom:80%;" />

- 이런식으로 진행한다. ~~(보통 filter의 크기와 동일하게 stride 진행)~~
  - sampling이라고 볼 수 있다.
  - 이미지 크기를 작게 만들어준다.
- 보통 convolution layer 다음에 배치

<br>

### fully connected layer

- convolutional layer들을 다 거치고 나면 마지막에는 일반적인 neural net과 같이 fully connected layer를 거치게 된다.
  - 여기서는 또 일반적인 모델처럼, 분류 문제라면 sigmoid나 softmax를 사용한다.

---

<br>

### CNN 활용 예

> 사진으로 맛만 보자..

- LeNet-5

![](https://user-images.githubusercontent.com/49020354/77289757-efa0e680-6d1d-11ea-903e-d0bd0b9c3c3b.PNG)

<br>

- AlexNet

![](https://user-images.githubusercontent.com/49020354/77289762-f3cd0400-6d1d-11ea-94dc-d36d997b6a52.PNG)

---

![](https://user-images.githubusercontent.com/49020354/77289770-f7608b00-6d1d-11ea-80d6-ecf5cfd76397.PNG)

---

![](https://user-images.githubusercontent.com/49020354/77289783-faf41200-6d1d-11ea-90bc-89068cfd55a0.PNG)

![](https://user-images.githubusercontent.com/49020354/77289787-fdef0280-6d1d-11ea-87ed-3e53da16c212.PNG)

Normalization layer는 옛날에 썼었는데 요즘에는 사용하지 않는다.

<br>

- GoogLeNet

![](https://user-images.githubusercontent.com/49020354/77289790-00e9f300-6d1e-11ea-9764-026434e123c8.PNG)

<br>

- ResNet

![](https://user-images.githubusercontent.com/49020354/77289797-03e4e380-6d1e-11ea-8a41-a2585f5f0faf.PNG)

---

![](https://user-images.githubusercontent.com/49020354/77289802-06473d80-6d1e-11ea-9903-73164e3f9921.PNG)

층이 엄청 많다..!

![](https://user-images.githubusercontent.com/49020354/77289805-09422e00-6d1e-11ea-9539-7d2cbd2cbe65.PNG)

---

![](https://user-images.githubusercontent.com/49020354/77289807-0ba48800-6d1e-11ea-9289-f547f90ca012.PNG)

---

![](https://user-images.githubusercontent.com/49020354/77289811-0e06e200-6d1e-11ea-9cec-f8be46af9040.PNG)

<br>

- Sentence Classification

![](https://user-images.githubusercontent.com/49020354/77289816-10693c00-6d1e-11ea-9746-f918ff94a40a.PNG)

<br>

- AlphaGo

![](https://user-images.githubusercontent.com/49020354/77289819-12cb9600-6d1e-11ea-989a-5f018c86b04b.PNG)

---

![](https://user-images.githubusercontent.com/49020354/77289824-15c68680-6d1e-11ea-98bf-f868ffe0845d.PNG)

