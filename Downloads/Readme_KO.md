# YOLOv1–v12: 논문 링크, 공식적인 코드 및 키 노트 (한글)

> 본 문서는 ...

---

## YOLOv1

Joseph Redmon이 발표한 <span style="color:#0000FF"><strong>YOLOv1</strong></span> 논문은 실시간 객체 탐지 분야의 패러다임을 바꾼 중요한
연구입니다.

### 1. YOLOv1 논문 다운로드 (arXiv)

- <strong>제목: </strong>You Only Look Once: Unified, Real-Time Object Detection
- <strong>저자: </strong>Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi
- <strong>다운로드 링크: </strong><span style="color:#0B57D0">[https://arxiv.org/abs/1506.02640](https://arxiv.org/abs/1506.02640)</span>

### 2. 공식 소스코드 및 프로젝트 페이지

- <strong>공식 Darknet 저장소 (C언어 기반): </strong><span style="color:#0B57D0">[https://github.com/pjreddie/darknet](https://github.com/pjreddie/darknet)</span>
<br>YOLO의 창시자인 Joseph Redmon이 직접 관리하던 원본 프레임워크인 <strong>Darknet</strong>의 소스코드입니다.
- <strong>공식 프로젝트 웹사이트: </strong><span style="color:#0B57D0">[https://pjreddie.com/darknet/yolo/](https://pjreddie.com/darknet/yolo/)</span>
<br>YOLOv1부터 v3까지의 가중치(weights) 파일과 설정법을 확인할 수 있는 Joseph Redmon의 공식 홈페이지입니다.

### 3. 파이토치(PyTorch) 구현체 
현재는 원본 C 코드를 직접 수정하기보다 PyTorch로 구현된 코드를 분석하는 경우가 많습니다. 가장 널리 쓰이는 구현체 중 하나는 다음과 같습니다.

- <strong>PyTorch YOLOv1: </strong>
<span style="color:#0B57D0">[https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLOv1](https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLOv1)</span>

이 링크들을 통해 YOLOv1의 핵심 알고리즘인 단일 단계 탐지(Single-stage detection) 구조를 상세히 파악하실 수 있습니다.

---

## YOLOv2

<span style="color:#0000FF"><strong>YOLOv2(YOLO9000)</strong></span>는 2017년 CVPR에서 발표된 논문으로, "Better, Faster, Stronger"라는 부제에
걸맞게 속도와 정확도를 대폭 개선했을 뿐만 아니라, 9,000종 이상의 객체를 탐지할 수 있는 능력을
보여주었습니다.

### 1. YOLOv2 (YOLO9000) 논문 다운로드

- <strong>제목: </strong>YOLO9000: Better, Faster, Stronger
- <strong>저자: </strong>Joseph Redmon, Ali Farhadi
- <strong>논문 링크 (arXiv): </strong><span style="color:#0B57D0">[https://arxiv.org/abs/1612.08242](https://arxiv.org/abs/1612.08242)</span>
- <strong>논문 링크 (CVPR Open Access): </strong>
<span style="color:#0B57D0">[https://openaccess.thecvf.com/content_cvpr_2017/html/Redmon_YOLO9000_Better_Faster_CVPR_2017_paper.html](https://openaccess.thecvf.com/content_cvpr_2017/html/Redmon_YOLO9000_Better_Faster_CVPR_2017_paper.html)</span>

### 2. 공식 소스코드 및 프로젝트 페이지

- <strong>공식 Darknet 저장소 (C언어 기반): </strong><span style="color:#0B57D0">[https://github.com/pjreddie/darknet](https://github.com/pjreddie/darknet)</span>
<br>YOLOv1과 마찬가지로, Joseph Redmon의 <strong>Darknet </strong>프레임워크 내에 구현되어 있습니다.
`cfg/yolo9000.cfg` 또는 `cfg/yolov2.cfg` 파일을 통해 모델 설정을 확인할 수 있습니다.
- <strong>공식 프로젝트 웹사이트: </strong><span style="color:#0B57D0">[https://pjreddie.com/darknet/yolov2/](https://pjreddie.com/darknet/yolov2/)</span>
<br>논문에서 사용된 미리 학습된 가중치(Weights) 파일과 테스트 방법을 안내하는 공식 사이트입니다.

### 3. 주요 개선 사항 

- <strong>Better: </strong>Batch Normalization 도입, High Resolution Classifier 사용, Anchor Boxes 활용.
- <strong>Faster: </strong>새로운 Backbone망인 <strong>Darknet-19</strong>제안.
- <strong>Stronger: </strong>WordTree 구조를 활용한 계층적 분류를 통해 Detection 데이터(COCO)와 Classification
데이터(ImageNet)를 함께 학습시켜 9,000개 이상의 클래스 인식 가능.

---

## YOLOv3
<span style="color:#0000FF"><strong>YOLOv3</strong></span>는 2018년 Joseph Redmon과 Ali Farhadi가 발표한 논문으로, 기존 YOLO 시리즈의 장점을
계승하면서도 <strong>Darknet-53</strong>이라는 더 깊은 신경망과 <strong>다중 스케일 예측(Multi-scale prediction)</strong>을
도입하여 성능을 비약적으로 끌어올린 모델입니다.

### 1. YOLOv3 논문 다운로드

- <strong>제목: </strong>YOLOv3: An Incremental Improvement
- <strong>저자: </strong>Joseph Redmon, Ali Farhadi
- <strong>논문 링크 (arXiv): </strong><span style="color:#0B57D0">[https://arxiv.org/abs/1804.02767](https://arxiv.org/abs/1804.02767)</span>
- <strong>논문 링크 (공식 웹사이트 PDF): </strong><span style="color:#0B57D0">[https://pjreddie.com/media/files/papers/YOLOv3.pdf](https://pjreddie.com/media/files/papers/YOLOv3.pdf)</span>

### 2. 소스코드 및 가중치(Weights) 링크

- <strong>공식 Darknet 저장소 (C언어 기반): </strong><span style="color:#0B57D0">[https://github.com/pjreddie/darknet](https://github.com/pjreddie/darknet)</span>
<br>YOLOv3의 공식 구현체입니다. `cfg/yolov3.cfg` 파일을 통해 구조를 확인할 수 있습니다.
- <strong>공식 프로젝트 페이지: </strong><span style="color:#0B57D0">[https://pjreddie.com/darknet/yolo/](https://pjreddie.com/darknet/yolo/)</span>
<br>YOLOv3의 Pre-trained 가중치 파일(.weights)을 다운로드할 수 있는 곳입니다.
- <strong>PyTorch 구현체 (추천): </strong><span style="color:#0B57D0">[https://github.com/ultralytics/yolov3](https://github.com/ultralytics/yolov3)</span>
<br>현재 가장 대중적으로 쓰이는 Ultralytics의 PyTorch 기반 YOLOv3 코드입니다.

### 3. YOLOv3의 핵심 기술적 변화

- <strong>Bounding Box Prediction: </strong>로지스틱 회귀를 사용하여 각 경계 상자의 객체 점수를 예측합니다.
- <strong>Class Prediction: </strong>Softmax 대신 독립적인 <strong>Logistic Classifiers</strong>를 사용하여 다중 레이블 분류(예:
Woman과 Person 동시 탐지)가 가능해졌습니다.
- <strong>Predictions Across Scales: </strong>FPN(Feature Pyramid Network)과 유사한 방식으로 3가지 다른
스케일(크기)에서 특징을 추출하여 작은 물체 탐지 능력을 대폭 개선했습니다.

---

## YOLOv4

<span style="color:#0000FF"><strong>YOLOv4</strong></span>는 2020년 Alexey Bochkovskiy 등에 의해 발표되었으며, 기존 YOLO 시리즈의 저자인 Joseph
Redmon이 떠난 후 커뮤니티에 의해 공식적으로 계승된 첫 번째 모델입니다. 이 논문은 수많은 <strong>'Bag of </strong>
<strong>Freebies'</strong>(학습 비용만 증가시키고 추론 속도는 유지하는 기법)와 <strong>'Bag of Specials'</strong>(추론 속도를 약간
희생하여 정확도를 대폭 높이는 기법)를 집대성하여 최적의 속도와 정확도를 달성했습니다.

### 1. YOLOv4 논문 다운로드

- <strong>제목: </strong>YOLOv4: Optimal Speed and Accuracy of Object Detection
- <strong>저자: </strong>Alexey Bochkovskiy, Chien-Yao Wang, Hong-Yuan Mark Liao
- <strong>논문 링크 (arXiv): </strong><span style="color:#0B57D0">[https://arxiv.org/abs/2004.10934](https://arxiv.org/abs/2004.10934)</span>

### 2. 소스코드 및 프로젝트 페이지

- <strong>공식 Darknet 저장소 (C언어/CUDA 기반): </strong><span style="color:#0B57D0">[https://github.com/AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)</span>
Joseph Redmon의 Darknet을 이어받아 AlexeyAB가 유지보수하는 공식 버전입니다. YOLOv4의 모든
실험 결과가 이 코드를 기반으로 합니다.
- <strong>공식 가중치(Weights) 파일: </strong><span style="color:#0B57D0">`yolov4.weights` (245MB)</span>
- <strong>PyTorch 구현체: </strong><span style="color:#0B57D0">[https://github.com/Tianxiaomo/pytorch-YOLOv4](https://github.com/Tianxiaomo/pytorch-YOLOv4)</span>
Darknet 가중치를 PyTorch로 변환하여 사용할 수 있는 대중적인 저장소입니다.

### 3. YOLOv4의 핵심 기술 

- <strong>Architecture: </strong>CSPDarknet53(Backbone), SPP(Neck), PANet(Path Aggregation), YOLOv3-Head
구성.
- <strong>Bag of Freebies (BoF): </strong>Mosaic 데이터 증강, DropBlock 규제화, CIoU Loss, Cross-mini-Batch
Normalization(CmBN).
- <strong>Bag of Specials (BoS): </strong>Mish 활성화 함수, SAM(Spatial Attention Module), DIoU-NMS.

특히 <strong>CSPNet </strong>구조가 YOLOv4에 도입되면서 성능 향상의 핵심이 되었습니다.

---

## YOLOv5

<span style="color:#0000FF"><strong>YOLOv5</strong></span>는 2020년 Glenn Jocher(Ultralytics)에 의해 공개되었으며, 학술적 논문 형식의 아카이브(arXiv)
문서보다는 GitHub 저장소와 기술 문서(Documentation)를 중심으로 발전하였습니다. 뛰어난 사용
편의성과 파이토치(PyTorch) 기반의 유연한 구조 덕분에 현재까지도 산업계에서 가장 널리 쓰이는 모델
중 하나입니다.

### 1. YOLOv5 논문 및 기술 문서 링크
YOLOv5는 정식 출판된 학술 논문 대신, Ultralytics 팀이 작성한 공식 문서와 분석 자료가 그 역할을
대신합니다.
- <strong>공식 기술 문서 (Documentation): </strong><span style="color:#0B57D0">[https://docs.ultralytics.com/models/yolov5/](https://docs.ultralytics.com/models/yolov5/)</span>
- <strong>공식 릴리스 노트 (v7.0 포함): </strong><span style="color:#0B57D0">[https://github.com/ultralytics/yolov5/releases](https://github.com/ultralytics/yolov5/releases)</span>

### 2. 공식 소스코드 및 프로젝트 페이지

- <strong>공식 GitHub 저장소: </strong><span style="color:#0B57D0">[https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)</span>
<br>최신 버전인 v7.0(Instance Segmentation 지원)까지 포함되어 있으며, pip install yolov5를 통해 바로
설치가 가능합니다.
- <strong>Pre-trained 가중치: </strong>저장소 내의 <span style="color:#0B57D0">Release Asset </span>페이지에서 YOLOv5n(Nano)부터 YOLOv5x(Extra
Large)까지 모든 모델 파일을 받을 수 있습니다.

### 3. YOLOv5의 핵심 특징
- <strong>PyTorch Native: </strong>기존 Darknet(C언어) 기반에서 완전히 벗어나 PyTorch로 구현되어 딥러닝 연구자들의
접근성을 극대화했습니다.
- <strong>C3 Module: </strong>Bottleneck CSP를 단순화한 <strong>C3(Cross Stage Partial bottleneck with 3 convolutions) </strong>
모듈을 도입하여 연산 효율성을 높였습니다.
- <strong>Auto-Learning Bounding Box Anchors: </strong>학습 데이터셋의 통계를 바탕으로 앵커 박스 크기를 자동으로
최적화하는 기능을 제공합니다.
- <strong>Model Scaling: </strong>입력을 조절하여 Nano(n), Small(s), Medium(m), Large(l), Extra Large(x)의 5가지
크기로 배포되어 하드웨어 환경에 맞는 선택이 가능합니다.

---

## YOLOv6

<span style="color:#0000FF"><strong>YOLOv6</strong></span>는 2022년 중국의 배달 플랫폼 기업인 <strong>메이투안(Meituan)</strong>의 비전 팀에 의해 발표되었습니다. 이
모델은 학술적 연구보다는 '<strong>산업 현장(Industrial Applications)</strong>'에서의 실제 추론 속도와 효율성을
극대화하는 데 초점을 맞추어 설계되었습니다.

### 1. YOLOv6 논문 다운로드

- <strong>제목: </strong>YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications
- <strong>저자: </strong>Chuyi Li, Liunian Li, Hongliang Jiang, et al. (Meituan Vision Labs)
- <strong>논문 링크 (arXiv): </strong><span style="color:#0B57D0">[https://arxiv.org/abs/2209.02976](https://arxiv.org/abs/2209.02976)</span>
- <strong>최신 버전 (v3.0) 기술 보고서: </strong><span style="color:#0B57D0">[https://arxiv.org/abs/2301.05586](https://arxiv.org/abs/2301.05586)</span>
<br>(v3.0에서는 Bi-directional Concatenation 등 네트워크 구조가 대폭 개선되었습니다.)

### 2. 공식 소스코드 및 프로젝트 페이지

- <strong>공식 GitHub 저장소: </strong><span style="color:#0B57D0">[https://github.com/meituan/YOLOv6](https://github.com/meituan/YOLOv6)</span>
메이투안 팀에서 직접 관리하는 공식 레포지토리이며, PyTorch 기반으로 구현되어 있습니다.
<strong>가중치(Weights) 파일: </strong>저장소의 <span style="color:#0B57D0">Release </span>섹션에서 YOLOv6-N(Nano)부터 YOLOv6-L(Large)까지의 최신 v3.0 가중치를 다운로드할 수 있습니다.

### 3. YOLOv6의 핵심 기술 
- <strong>RepVGG Backbone: </strong>추론 시에는 단일 경로(Single-path) 구조로 변환되어 속도를 높이고, 학습 시에는
다중 경로로 학습하는 <strong>Re-parameterization</strong>기법을 적극 도입했습니다.
- <strong>Decoupled Head: </strong>분류(Classification)와 회귀(Regression) 예측을 분리하여 처리함으로써 정확도를
높였습니다.
- <strong>Quantization Friendly: </strong>산업용 배포를 위해 하드웨어 가속 및 양자화(INT8)에 최적화된 설계를
적용했습니다.
- <strong>SimOTA: </strong>YOLOX에서 제안된 동적 레이블 할당 전략을 최적화하여 학습 속도를 개선했습니다.

---

## YOLOv7

<span style="color:#0000FF"><strong>YOLOv7</strong></span>은 2022년 CVPR에서 발표되었으며, YOLOv4의 저자인 Chien-Yao Wang과 Alexey
Bochkovskiy가 다시 합작하여 만든 모델입니다. "Trainable Bag-of-Freebies"라는 개념을 통해 학습
효율을 극대화하고, 당시 현존하는 모든 실시간 객체 탐지기의 성능을 뛰어넘는 새로운
SOTA(State-of-the-Art)를 기록했습니다.

### 1. YOLOv7 논문 다운로드

- <strong>제목: </strong>YOLOv7: Trainable Bag-of-Freebies Sets New State-of-the-Art for Real-Time Object
Detectors
- <strong>저자: </strong>Chien-Yao Wang, Alexey Bochkovskiy, Hong-Yuan Mark Liao
- <strong>논문 링크 (arXiv): </strong><span style="color:#0B57D0">[https://arxiv.org/abs/2207.02696](https://arxiv.org/abs/2207.02696)</span>
- <strong>논문 링크 (CVPR Open Access): </strong>
<span style="color:#0B57D0">[https://openaccess.thecvf.com/content/CVPR2023/html/Wang_YOLOv7_Trainable_Bag-of-Freebies_Sets_New_State-of-the-Art_for_Real-Time_Object_CVPR_2023_paper.html](https://openaccess.thecvf.com/content/CVPR2023/html/Wang_YOLOv7_Trainable_Bag-of-Freebies_Sets_New_State-of-the-Art_for_Real-Time_Object_CVPR_2023_paper.html)</span>

### 2. 공식 소스코드 및 프로젝트 페이지

- <strong>공식 GitHub 저장소: </strong><span style="color:#0B57D0">[https://github.com/WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7)</span>
<br>PyTorch 기반으로 구현되어 있으며, 연구 및 산업 현장에서 가장 신뢰받는 공식 코드입니다.
- <strong>공식 가중치(Weights) 파일: </strong>저장소의 <span style="color:#0B57D0">Release </span>페이지에서 YOLOv7-tiny부터 YOLOv7-E6E까지 모든
모델 파일을 받을 수 있습니다.

### 3. YOLOv7의 핵심 혁신
- <strong>E-ELAN (Extended Efficient Layer Aggregation Network): </strong>그라디언트 경로를 최적화하여 네트워크가
더 효과적으로 학습할 수 있도록 설계된 아키텍처입니다.
- <strong>Model Scaling for Concatenation-based Models: </strong>단순히 깊이나 너비를 키우는 것이 아니라,
파라미터와 연산량의 균형을 맞추며 모델 크기를 조절하는 새로운 스케일링 기법을 제안했습니다.
- <strong>Planned Re-parameterized Convolution: </strong>RepVGG와 같은 재매개변수화 기법을 최적화하여 추론
속도를 희생하지 않고 성능을 높였습니다.
- <strong>Coarse-to-Fine Lead Head Label Assignment: </strong>보조 헤드(Auxiliary head)와 리드 헤드(Lead head)를
활용한 새로운 레이블 할당 전략을 도입했습니다.

---

## YOLOv8

<span style="color:#0000FF"><strong>YOLOv8</strong></span>은 2023년 <strong>Ultralytics(Glenn Jocher)</strong>에 의해 발표된 모델로, 이전 버전인 YOLOv5의 성공을
바탕으로 설계되었습니다. YOLOv8은 특정 아키텍처에 국한되지 않고 객체 탐지(Detection),
세그먼테이션(Segmentation), 자세 추정(Pose Estimation), 추적(Tracking), 분류(Classification)를 모두
지원하는 <strong>통합 프레임워크</strong>로 진화했습니다.

### 1. YOLOv8 논문 및 기술 문서 링크
YOLOv5와 마찬가지로, YOLOv8 역시 정식 arXiv 논문보다는 공식 문서와 오픈소스 커뮤니티의 기술
리포트를 중심으로 배포되었습니다.
- <strong>공식 기술 문서 (Documentation): </strong><span style="color:#0B57D0">[https://docs.ultralytics.com/models/yolov8/](https://docs.ultralytics.com/models/yolov8/)</span>
- <strong>Ultralytics 공식 블로그 (핵심 요약): </strong><span style="color:#0B57D0">[https://www.ultralytics.com/blog/ultralytics-yolov8-is-here](https://www.ultralytics.com/blog/ultralytics-yolov8-is-here)</span>

### 2. 공식 소스코드 및 프로젝트 페이지

- <strong>공식 GitHub 저장소: </strong><span style="color:#0B57D0">[https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)</span>
<br>YOLOv8은 ultralytics라는 통합 패키지로 관리됩니다. pip install ultralytics 명령어로 쉽게 설치하여
사용할 수 있습니다.
- <strong>가중치(Weights) 및 모델 체크포인트: </strong><span style="color:#0B57D0">[https://github.com/ultralytics/assets/releases](https://github.com/ultralytics/assets/releases)</span>
<br>YOLOv8n부터 YOLOv8x까지 다양한 크기의 가중치 파일을 제공합니다.

### 3. YOLOv8의 핵심 기술적 혁신 

- <strong>Anchor-Free Detection: </strong>YOLOv5까지 유지되던 앵커 기반 방식을 버리고 <strong>앵커 프리(Anchor-Free) </strong>
방식을 도입하여 객체의 중심을 직접 예측함으로써 일반화 성능을 높였습니다.
- <strong>C2f Module: </strong>YOLOv5의 C3 모듈을 개선한 <strong>C2f (Cross-Stage Partial Bottleneck with 2 Convolutions) </strong>모듈을 사용하여 특징 추출 능력을 강화하면서도 경량성을 유지했습니다.
- <strong>Decoupled Head: </strong>분류와 회귀를 별도의 브랜치에서 처리하는 구조를 채택하여 수렴 속도와 정확도를 향상시켰습니다.
- <strong>New Loss Functions: </strong>회귀 손실을 위해 <strong>CIoU</strong>와 <strong>DFL(Distribution Focal Loss)</strong>을 결합하여 경계 상자 예측의 정밀도를 높였습니다.

---

## YOLOv9

<span style="color:#0000FF"><strong>YOLOv9</strong></span>은 2024년 2월 Chien-Yao Wang(YOLOv4, v7의 저자) 등에 의해 발표되었으며, 정보 손실
문제를 해결하기 위해 <strong>PGI(Programmable Gradient Information)</strong>와 <strong>GELAN(Generalized ELAN) </strong>
아카텍처를 도입하여 큰 주목을 받았습니다.

### 1. YOLOv9 논문 다운로드

- <strong>제목: </strong>YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information
- <strong>저자: </strong>Chien-Yao Wang, I-Hau Yeh, Hong-Yuan Mark Liao
- <strong>논문 링크 (arXiv): </strong><span style="color:#0B57D0">[https://arxiv.org/abs/2402.13616](https://arxiv.org/abs/2402.13616)</span>

### 2. 공식 소스코드 및 프로젝트 페이지

- <strong>공식 GitHub 저장소: </strong><span style="color:#0B57D0">[https://github.com/WongKinYiu/yolov9](https://github.com/WongKinYiu/yolov9)</span>
<br>PyTorch 기반의 공식 구현체이며, 최신 연구 결과가 지속적으로 업데이트됩니다.
- <strong>가중치(Weights) 파일: </strong>저장소의 <span style="color:#0B57D0">Release </span>섹션에서 YOLOv9-S, M, C, E 모델별 학습된 가중치를
다운로드할 수 있습니다.

### 3. YOLOv9의 핵심 혁신 

- <strong>Information Bottleneck 해결: </strong>딥러닝 네트워크가 깊어질수록 입력 데이터의 정보가 소실되는 문제를
지적하고 이를 해결하기 위한 이론적 토대를 마련했습니다.
- <strong>PGI (Programmable Gradient Information): </strong>보조 가역 분기(Auxiliary Reversible Branch)를 통해
타겟 데이터에 도달하기 위한 완전한 정보를 유지하며, 이를 통해 메인 브랜치가 더 정확한 그라디언트를
얻을 수 있도록 돕습니다.
- <strong>GELAN (Generalized Efficient Layer Aggregation Network): </strong>기존 ELAN을 일반화하여 연산 효율과
정확도의 균형을 극대화한 새로운 아키텍처입니다.
- <strong>성능: </strong>YOLOv9은 이전 버전인 YOLOv8보다 파라미터 수는 적으면서도 더 높은 mAP를 기록하며
효율성을 입증했습니다.

---

## YOLOv10

<span style="color:#0000FF"><strong>YOLOv10</strong></span>은 2024년 5월 칭화 대학교(Tsinghua University) 연구팀에 의해 발표되었으며, YOLO
시리즈의 고질적인 병목 현상이었던 <strong>NMS(Non-Maximum Suppression)</strong>를 제거하여 완전한 <strong>엔드 투 </strong>
<strong>엔드(End-to-End) </strong>실시간 객체 탐지를 구현한 모델입니다.

### 1. YOLOv10 논문 다운로드

- <strong>제목: </strong>YOLOv10: Real-Time End-to-End Object Detection
- <strong>저자: </strong>Ao Wang, Hui Chen, Liwu Wei, Zhiqiang Bin, et al.
- <strong>논문 링크 (arXiv): </strong><span style="color:#0B57D0">[https://arxiv.org/abs/2405.14458](https://arxiv.org/abs/2405.14458)</span>

### 2. 공식 소스코드 및 프로젝트 페이지

- <strong>공식 GitHub 저장소: </strong><span style="color:#0B57D0">[https://github.com/THU-MIG/yolov10](https://github.com/THU-MIG/yolov10)</span>
<br>칭화대학교 멀티미디어 인텔리전스 그룹(MIG)에서 관리하는 공식 저장소입니다.
- <strong>Hugging Face 데모: </strong><span style="color:#0B57D0">[https://huggingface.co/spaces/jameslahm/yolov10](https://huggingface.co/spaces/jameslahm/yolov10)</span>
<br>웹상에서 직접 이미지를 업로드하여 YOLOv10의 성능을 테스트해 볼 수 있습니다.

### 3. YOLOv10의 핵심 혁신 

- <strong>NMS-Free Training:</strong>중복된 예측 상자를 제거하는 NMS 과정은 추론 속도를 늦추는 원인이었습니다.
YOLOv10은 <strong>Consistent Dual Assignment</strong>전략을 도입하여 NMS 없이도 정확한 결과를 도출하며 추론
지연 시간을 대폭 줄였습니다.
- <strong>Holistic Model Design:</strong>연산 효율을 극대화하기 위해 효율적인 부분 셀프 어텐션(Partial Self-Attention,
PSA)과 공간-채널 분리 합성곱 등을 결합한 포괄적 설계를 적용했습니다.
- <strong>Efficiency-Accuracy Bound:</strong>성능 손실 없이 파라미터 수와 계산량을 최적화하여, 이전 버전들보다
월등히 적은 자원으로도 높은 정확도를 보여줍니다.

---

## YOLOv11

<span style="color:#0000FF"><strong>YOLOv11</strong></span>은 2024년 9월 <strong>Ultralytics(Glenn Jocher)</strong>에 의해 공개되었습니다. 이전 버전인 YOLOv8,
v10의 성공을 계승하면서도 아키텍처를 전면적으로 재설계하여, 더 적은 파라미터로 더 높은 정확도와
속도를 달성하는 데 성공한 모델입니다.

### 1. YOLO11 기술 문서 및 가이드
YOLO11 역시 Ultralytics의 정책에 따라 전통적인 arXiv 논문 형태보다는 실용적인 <strong>기술 문서와 블로그 리포트</strong>를 통해 상세 사양이 공개되었습니다.
- <strong>공식 기술 문서 (Documentation): </strong><span style="color:#0B57D0">[https://docs.ultralytics.com/models/yolo11/](https://docs.ultralytics.com/models/yolo11/)</span>
- <strong>Ultralytics 공식 블로그 (YOLO11 출시 공고): </strong>
<span style="color:#0B57D0">[https://www.ultralytics.com/blog/ultralytics-yolo11-has-arrived-redefining-performance-and-versatility](https://www.ultralytics.com/blog/ultralytics-yolo11-has-arrived-redefining-performance-and-versatility)</span>

### 2. 공식 소스코드 및 프로젝트 페이지

- <strong>공식 GitHub 저장소: </strong><span style="color:#0B57D0">[https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)</span>
YOLOv8과 마찬가지로, `ultralytics` 통합 라이브러리에 포함되어 있습니다. 최신 버전을 설치(`pip install
ultralytics --upgrade`)하면 바로 YOLO11 모델을 사용할 수 있습니다.
- <strong>Pre-trained 가중치 (Assets): </strong><span style="color:#0B57D0">[https://github.com/ultralytics/assets/releases](https://github.com/ultralytics/assets/releases)</span>
YOLO11n, 11s, 11m, 11l, 11x 등 각 모델의 `.pt` 파일을 다운로드할 수 있습니다.

### 3. YOLO11의 핵심 기술적 혁신 

- <strong>C3k2 Module: </strong>기존의 C2f 모듈을 개선한 <strong>C3k2(Cross-Stage Partial Bottleneck with 3 convolutions and 2 kernels)</strong>를 도입하여, 연산 효율을 극대화하면서 특징 추출 능력을 세밀하게 조정했습니다.
- <strong>C2PSA (C2f with Partial Self-Attention): </strong>네트워크 상단에 <strong>부분 셀프 어텐션 </strong>레이어를 통합하여, 연산
비용을 통제하면서도 전역적인 맥락(Global Context)을 파악하는 능력을 높였습니다.
- <strong>Optimized Architecture: </strong>YOLOv8 대비 파라미터 수를 약 22% 줄였음에도 불구하고 mAP 성능은
향상되어, 임베디드 장치에서의 실시간 성능이 극대화되었습니다.
- <strong>Multi-task Versatility: </strong>탐지(Detection)뿐만 아니라 세그먼테이션, 자세 추정, OBB(Oriented Bounding
Boxes), 분류에 최적화된 설계를 공유합니다.

---

## YOLOv12

가장 최신 모델인 <span style="color:#0000FF"><strong>YOLOv12</strong></span>는 2025년 2월에 발표되었으며, 기존의 CNN 중심 구조에서 벗어나 <strong>어텐션 </strong>
<strong>중심(Attention-Centric) </strong>설계로 패러다임을 전환한 기념비적인 모델입니다. 특히 "<strong>실시간 성능을 </strong>
<strong>유지하면서 셀프 어텐션의 이점을 극대화</strong>"했다는 점에서 학계의 큰 관심을 받고 있습니다.
<strong>1. YOLOv12 논문 다운로드</strong>
<strong>제목: </strong>YOLOv12: Attention-Centric Real-Time Object Detectors
<strong>저자: </strong>Yunjie Tian, Ge Zheng, 외 (University of Chinese Academy of Sciences 및 여러 연구 기관)
<strong>논문 링크 (arXiv): </strong><span style="color:#0B57D0">[https://arxiv.org/abs/2502.12524](https://arxiv.org/abs/2502.12524)</span>
<strong>2. 공식 소스코드 및 프로젝트 페이지</strong>
<strong>공식 GitHub 저장소: </strong><span style="color:#0B57D0">[https://github.com/sanyuan-ai/YOLOv12](https://github.com/sanyuan-ai/YOLOv12)</span>
<strong>관련 가중치(Weights): </strong>저장소의 Release 섹션에서 YOLOv12-N(Nano)부터 YOLOv12-X(Extra
Large)까지의 사전 학습된 모델을 제공합니다.
<strong>3. YOLOv12의 핵심 혁신 </strong>
<strong>Area Attention: </strong>표준 어텐션의 O(N2)복잡도 문제를 해결하기 위해, 인접 영역에 집중하는 Area
Attention을 도입하여 계산 효율성을 획득했습니다.
<strong>R-ELAN (Residual Efficient Layer Aggregation Network): </strong>YOLOv7/v9의 ELAN 구조를 계승하되,
어텐션 레이어의 학습 안정성을 위해 잔차(Residual) 연결을 최적화했습니다.
<strong>FlashAD (Flash Attention Detector): </strong>추론 속도를 극대화하기 위해 FlashAttention 기법을 실시간 객체
탐지기에 맞게 튜닝하여 적용했습니다.
<strong>성능 지표: </strong>YOLOv12-N 기준, 이전 최신 모델보다 약 20% 적은 연산량으로도 동등하거나 더 높은
정확도를 보여줍니다.
