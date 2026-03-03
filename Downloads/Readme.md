# YOLOv1–v12: Paper Links, Official Code, and Key Notes (English Translation)

> This document is an English translation of the attached file, keeping the original structure (numbering, bold emphasis, and link text). fileciteturn0file0

---

Joseph Redmon’s <span style="color:#0000FF"><strong>YOLOv1</strong></span> paper is a landmark study that changed the paradigm of real-time object detection.

## 1. Download the <span style="color:#0000FF"><strong>YOLOv1</strong></span> Paper (arXiv)

- **Title:** You Only Look Once: Unified, Real-Time Object Detection  
- **Authors:** Joseph Redmon, Santosh Divvala, Ross Girshick, Ali Farhadi  
- **Download link:** https://arxiv.org/abs/1506.02640

## 2. Official Source Code and Project Page

- **Official Darknet repository (C-based):** https://github.com/pjreddie/darknet  
  This is the source code of Darknet, the original framework directly maintained by Joseph Redmon, the creator of YOLO.

- **Official project website:** https://pjreddie.com/darknet/yolo/  
  This is Joseph Redmon’s official site where you can find the weights files and setup instructions for <span style="color:#0000FF"><strong>YOLOv1</strong></span> through v3.

## 3. PyTorch Implementation

Nowadays, instead of modifying the original C code directly, many people analyze PyTorch implementations. One of the most widely used implementations is:

- **PyTorch YOLOv1:**  
  https://github.com/aladdinpersson/Machine-Learning-Collection/tree/master/ML/Pytorch/object_detection/YOLOv1

Through these links, you can examine in detail the single-stage detection structure, which is the core algorithm of <span style="color:#0000FF"><strong>YOLOv1</strong></span>.

---

<span style="color:#0B57D0"><strong>YOLOv2 (YOLO9000)</strong></span> is a paper presented at CVPR 2017. True to the subtitle “Better, Faster, Stronger,” it greatly improved both speed and accuracy, and also demonstrated the ability to detect more than 9,000 object categories.

## 1. Download the <span style="color:#0B57D0"><strong>YOLOv2 (YOLO9000)</strong></span> Paper

- **Title:** YOLO9000: Better, Faster, Stronger  
- **Authors:** Joseph Redmon, Ali Farhadi  
- **Paper link (arXiv):** https://arxiv.org/abs/1612.08242  
- **Paper link (CVPR Open Access):**  
  https://openaccess.thecvf.com/content_cvpr_2017/html/Redmon_YOLO9000_Better_Faster_CVPR_2017_paper.html

## 2. Official Source Code and Project Page

- **Official Darknet repository (C-based):** https://github.com/pjreddie/darknet  
  As with <span style="color:#0000FF"><strong>YOLOv1</strong></span>, it is implemented within Joseph Redmon’s Darknet framework. You can check model settings via `cfg/yolo9000.cfg` or `cfg/yolov2.cfg`.

- **Official project website:** https://pjreddie.com/darknet/yolov2/  
  An official site that provides pre-trained weights used in the paper and instructions for testing.

## 3. Major Improvements

- **Better:** Introduced Batch Normalization, used a High Resolution Classifier, and leveraged Anchor Boxes.  
- **Faster:** Proposed a new backbone network, Darknet-19.  
- **Stronger:** Using a WordTree-based hierarchical classification, it learns detection data (COCO) together with classification data (ImageNet), enabling recognition of more than 9,000 classes.

---

<span style="color:#0B57D0"><strong>YOLOv3</strong></span> is a paper released in 2018 by Joseph Redmon and Ali Farhadi. It inherits the strengths of the earlier YOLO series, while introducing a deeper network, Darknet-53, and multi-scale prediction to dramatically boost performance.

## 1. Download the <span style="color:#0B57D0"><strong>YOLOv3</strong></span> Paper

- **Title:** YOLOv3: An Incremental Improvement  
- **Authors:** Joseph Redmon, Ali Farhadi  
- **Paper link (arXiv):** https://arxiv.org/abs/1804.02767  
- **Paper link (official website PDF):** https://pjreddie.com/media/files/papers/YOLOv3.pdf

## 2. Source Code and Weights Links

- **Official Darknet repository (C-based):** https://github.com/pjreddie/darknet  
  The official implementation of <span style="color:#0B57D0"><strong>YOLOv3</strong></span>. You can check the architecture via `cfg/yolov3.cfg`.

- **Official project page:** https://pjreddie.com/darknet/yolo/  
  Where you can download the pre-trained weights (.weights) for <span style="color:#0B57D0"><strong>YOLOv3</strong></span>.

- **PyTorch implementation (recommended):** https://github.com/ultralytics/yolov3  
  Ultralytics’ PyTorch-based <span style="color:#0B57D0"><strong>YOLOv3</strong></span> code, widely used today.

## 3. Core Technical Changes in <span style="color:#0B57D0"><strong>YOLOv3</strong></span>

- **Bounding box prediction:** Uses logistic regression to predict the objectness score for each bounding box.  
- **Class prediction:** Uses independent logistic classifiers instead of softmax, enabling multi-label classification (e.g., detecting *Woman* and *Person* simultaneously).  
- **Predictions across scales:** Extracts features at three different scales in an FPN-like manner, greatly improving small-object detection.

---

<span style="color:#0B57D0"><strong>YOLOv4</strong></span> was published in 2020 by Alexey Bochkovskiy and others. It is the first model officially continued by the community after Joseph Redmon’s departure. The paper consolidates numerous “Bag of Freebies” (methods that increase training cost but keep inference speed) and “Bag of Specials” (methods that slightly sacrifice inference speed to substantially improve accuracy) to achieve an optimal balance of speed and accuracy.

## 1. Download the <span style="color:#0B57D0"><strong>YOLOv4</strong></span> Paper

- **Title:** YOLOv4: Optimal Speed and Accuracy of Object Detection  
- **Authors:** Alexey Bochkovskiy, Chien-Yao Wang, Hong-Yuan Mark Liao  
- **Paper link (arXiv):** https://arxiv.org/abs/2004.10934

## 2. Source Code and Project Pages

- **Official Darknet repository (C/CUDA-based):** https://github.com/AlexeyAB/darknet  
  The official version maintained by AlexeyAB, inherited from Joseph Redmon’s Darknet. All experimental results of <span style="color:#0B57D0"><strong>YOLOv4</strong></span> are based on this code.

- **Official weights file:** `yolov4.weights` (245MB)

- **PyTorch implementation:** https://github.com/Tianxiaomo/pytorch-YOLOv4  
  A popular repository that converts Darknet weights for use in PyTorch.

## 3. Core Technologies in <span style="color:#0B57D0"><strong>YOLOv4</strong></span>

- **Architecture:** CSPDarknet53 (Backbone), SPP (Neck), PANet (Path Aggregation), YOLOv3-Head.  
- **Bag of Freebies (BoF):** Mosaic augmentation, DropBlock regularization, CIoU loss, Cross-mini-Batch Normalization (CmBN).  
- **Bag of Specials (BoS):** Mish activation, SAM (Spatial Attention Module), DIoU-NMS.  

In particular, the introduction of CSPNet into <span style="color:#0B57D0"><strong>YOLOv4</strong></span> became a key driver of performance gains.

---

<span style="color:#0B57D0"><strong>YOLOv5</strong></span> was released in 2020 by Glenn Jocher (Ultralytics). Rather than an academic paper in arXiv format, it has evolved mainly through its GitHub repository and documentation. Thanks to excellent usability and a flexible PyTorch-based design, it remains one of the most widely used models in industry.

## 1. <span style="color:#0B57D0"><strong>YOLOv5</strong></span> Paper / Documentation Links

<span style="color:#0B57D0"><strong>YOLOv5</strong></span> does not have a formally published academic paper; instead, official Ultralytics documentation and analysis materials serve that role.

- **Official documentation:** https://docs.ultralytics.com/models/yolov5/  
- **Official release notes (including v7.0):** https://github.com/ultralytics/yolov5/releases

## 2. Official Source Code and Project Page

- **Official GitHub repository:** https://github.com/ultralytics/yolov5  
  Includes the latest version up to v7.0 (supports instance segmentation). You can install it directly with `pip install yolov5`.

- **Pre-trained weights:**  
  From the repository’s Release Assets page, you can download all model files from YOLOv5n (Nano) to YOLOv5x (Extra Large).

## 3. Core Features of <span style="color:#0B57D0"><strong>YOLOv5</strong></span>

- **PyTorch native:** Fully implemented in PyTorch, moving completely away from the Darknet (C) base and maximizing accessibility for deep learning researchers.  
- **C3 module:** Introduces the C3 (Cross Stage Partial bottleneck with 3 convolutions) module, a simplification of Bottleneck CSP to improve computational efficiency.  
- **Auto-learning bounding box anchors:** Automatically optimizes anchor box sizes based on dataset statistics.  
- **Model scaling:** Distributed in five sizes—Nano (n), Small (s), Medium (m), Large (l), Extra Large (x)—allowing selection according to hardware constraints.

---

<span style="color:#0B57D0"><strong>YOLOv6</strong></span> was presented in 2022 by the vision team of Meituan (a Chinese delivery platform company). Rather than focusing on academic novelty, it was designed to maximize real inference speed and efficiency in industrial deployment.

## 1. Download the <span style="color:#0B57D0"><strong>YOLOv6</strong></span> Paper

- **Title:** YOLOv6: A Single-Stage Object Detection Framework for Industrial Applications  
- **Authors:** Chuyi Li, Liunian Li, Hongliang Jiang, et al. (Meituan Vision Labs)  
- **Paper link (arXiv):** https://arxiv.org/abs/2209.02976  
- **Latest version (v3.0) technical report:** https://arxiv.org/abs/2301.05586  
  (In v3.0, the network structure was significantly improved, including Bi-directional Concatenation.)

## 2. Official Source Code and Project Page

- **Official GitHub repository:** https://github.com/meituan/YOLOv6  
  The official repository managed directly by the Meituan team; implemented in PyTorch.

- **Weights:**  
  From the repository’s Release section, you can download the latest v3.0 weights from YOLOv6-N (Nano) to YOLOv6-L (Large).

## 3. Core Technologies in <span style="color:#0B57D0"><strong>YOLOv6</strong></span>

- **RepVGG backbone:** Actively uses re-parameterization, learning with multi-path structure during training, then converting to a single-path structure at inference for higher speed.  
- **Decoupled head:** Separates classification and regression predictions to improve accuracy.  
- **Quantization friendly:** Applies designs optimized for hardware acceleration and INT8 quantization for industrial deployment.  
- **SimOTA:** Optimizes the dynamic label assignment strategy proposed in YOLOX, improving training speed.

---

<span style="color:#0B57D0"><strong>YOLOv7</strong></span> was presented at CVPR 2022 and was created through collaboration between Chien-Yao Wang and Alexey Bochkovskiy (authors of <span style="color:#0B57D0"><strong>YOLOv4</strong></span>). With the concept of “Trainable Bag-of-Freebies,” it maximized training efficiency and set a new SOTA (State-of-the-Art) among real-time detectors at the time.

## 1. Download the <span style="color:#0B57D0"><strong>YOLOv7</strong></span> Paper

- **Title:** YOLOv7: Trainable Bag-of-Freebies Sets New State-of-the-Art for Real-Time Object Detectors  
- **Authors:** Chien-Yao Wang, Alexey Bochkovskiy, Hong-Yuan Mark Liao  
- **Paper link (arXiv):** https://arxiv.org/abs/2207.02696  
- **Paper link (CVPR Open Access):**  
  https://openaccess.thecvf.com/content/CVPR2023/html/Wang_YOLOv7_Trainable_Bag-of-Freebies_Sets_New_State-of-the-Art_for_Real-Time_Object_CVPR_2023_paper.html

## 2. Official Source Code and Project Page

- **Official GitHub repository:** https://github.com/WongKinYiu/yolov7  
  An official, highly trusted PyTorch implementation used widely in research and industry.

- **Official weights:**  
  From the repository’s Release page, you can download all model files from YOLOv7-tiny to YOLOv7-E6E.

## 3. Key Innovations of <span style="color:#0B57D0"><strong>YOLOv7</strong></span>

- **E-ELAN (Extended Efficient Layer Aggregation Network):** An architecture designed to optimize gradient paths so that the network can learn more effectively.  
- **Model scaling for concatenation-based models:** Proposes a new scaling method that adjusts model size by balancing parameters and computation, rather than simply increasing depth or width.  
- **Planned re-parameterized convolution:** Optimizes re-parameterization techniques (like RepVGG) to improve performance without sacrificing inference speed.  
- **Coarse-to-fine lead head label assignment:** Introduces a new label assignment strategy using auxiliary heads and a lead head.

---

<span style="color:#0B57D0"><strong>YOLOv8</strong></span> was released in 2023 by Ultralytics (Glenn Jocher), building on the success of <span style="color:#0B57D0"><strong>YOLOv5</strong></span>. It evolved into a unified framework that is not limited to a single architecture, supporting detection, segmentation, pose estimation, tracking, and classification.

## 1. <span style="color:#0B57D0"><strong>YOLOv8</strong></span> Documentation Links

Like <span style="color:#0B57D0"><strong>YOLOv5</strong></span>, <span style="color:#0B57D0"><strong>YOLOv8</strong></span> was released mainly through official documentation and community technical reports rather than a formal arXiv paper.

- **Official documentation:** https://docs.ultralytics.com/models/yolov8/  
- **Ultralytics official blog (key summary):** https://www.ultralytics.com/blog/ultralytics-yolov8-is-here

## 2. Official Source Code and Project Page

- **Official GitHub repository:** https://github.com/ultralytics/ultralytics  
  <span style="color:#0B57D0"><strong>YOLOv8</strong></span> is managed under the unified `ultralytics` package. You can install it easily via `pip install ultralytics`.

- **Weights and model checkpoints:** https://github.com/ultralytics/assets/releases  
  Provides weights from YOLOv8n through YOLOv8x.

## 3. Core Technical Innovations in <span style="color:#0B57D0"><strong>YOLOv8</strong></span>

- **Anchor-free detection:** Switches from anchor-based detection (used up to <span style="color:#0B57D0"><strong>YOLOv5</strong></span>) to anchor-free detection, predicting object centers directly to improve generalization.  
- **C2f module:** Uses the C2f (Cross-Stage Partial Bottleneck with 2 Convolutions) module, improving feature extraction while keeping the model lightweight.  
- **Decoupled head:** Uses separate branches for classification and regression to improve convergence speed and accuracy.  
- **New loss functions:** Combines CIoU and DFL (Distribution Focal Loss) for regression loss to improve bounding box precision.

---

<span style="color:#0B57D0"><strong>YOLOv9</strong></span> was released in February 2024 by Chien-Yao Wang (author of <span style="color:#0B57D0"><strong>YOLOv4</strong></span> and <span style="color:#0B57D0"><strong>YOLOv7</strong></span>) and others. It attracted major attention by introducing PGI (Programmable Gradient Information) and the GELAN (Generalized ELAN) architecture to address information loss.

## 1. Download the <span style="color:#0B57D0"><strong>YOLOv9</strong></span> Paper

- **Title:** YOLOv9: Learning What You Want to Learn Using Programmable Gradient Information  
- **Authors:** Chien-Yao Wang, I-Hau Yeh, Hong-Yuan Mark Liao  
- **Paper link (arXiv):** https://arxiv.org/abs/2402.13616

## 2. Official Source Code and Project Page

- **Official GitHub repository:** https://github.com/WongKinYiu/yolov9  
  Official PyTorch implementation, continuously updated with the latest research results.

- **Weights:**  
  From the repository’s Release section, you can download trained weights for YOLOv9-S, M, C, and E.

## 3. Key Innovations of <span style="color:#0B57D0"><strong>YOLOv9</strong></span>

- **Solving the information bottleneck:** Points out that input information can be lost as networks get deeper, and provides a theoretical foundation to address it.  
- **PGI (Programmable Gradient Information):** Uses an auxiliary reversible branch to preserve complete information to reach the target, helping the main branch obtain more accurate gradients.  
- **GELAN (Generalized Efficient Layer Aggregation Network):** A new architecture that generalizes ELAN to maximize the balance between efficiency and accuracy.  
- **Performance:** Demonstrates efficiency by achieving higher mAP than <span style="color:#0B57D0"><strong>YOLOv8</strong></span> with fewer parameters.

---

<span style="color:#0B57D0"><strong>YOLOv10</strong></span> was released in May 2024 by a Tsinghua University research team. It removes NMS (Non-Maximum Suppression), a long-standing bottleneck in the YOLO series, enabling fully end-to-end real-time object detection.

## 1. Download the <span style="color:#0B57D0"><strong>YOLOv10</strong></span> Paper

- **Title:** YOLOv10: Real-Time End-to-End Object Detection  
- **Authors:** Ao Wang, Hui Chen, Liwu Wei, Zhiqiang Bin, et al.  
- **Paper link (arXiv):** https://arxiv.org/abs/2405.14458

## 2. Official Source Code and Project Page

- **Official GitHub repository:** https://github.com/THU-MIG/yolov10  
  Official repository managed by Tsinghua University Multimedia Intelligence Group (MIG).

- **Hugging Face demo:** https://huggingface.co/spaces/jameslahm/yolov10  
  You can upload images on the web and test <span style="color:#0B57D0"><strong>YOLOv10</strong></span> performance directly.

## 3. Key Innovations of <span style="color:#0B57D0"><strong>YOLOv10</strong></span>

- **NMS-free training:** Since NMS slows down inference by removing duplicate predicted boxes, <span style="color:#0B57D0"><strong>YOLOv10</strong></span> introduces a Consistent Dual Assignment strategy to produce accurate results without NMS, greatly reducing inference latency.  
- **Holistic model design:** Applies a comprehensive design combining Partial Self-Attention (PSA) and spatial-channel decoupled convolutions to maximize computational efficiency.  
- **Efficiency–accuracy bound:** Optimizes parameters and computation without performance loss, achieving high accuracy with far fewer resources than prior versions.

---

<span style="color:#0B57D0"><strong>YOLOv11 (YOLO11)</strong></span> was released in September 2024 by Ultralytics (Glenn Jocher). It inherits the success of <span style="color:#0B57D0"><strong>YOLOv8</strong></span> and <span style="color:#0B57D0"><strong>YOLOv10</strong></span> while redesigning the architecture to achieve higher accuracy and speed with fewer parameters.

## 1. <span style="color:#0B57D0"><strong>YOLO11</strong></span> Documentation and Guide

As with Ultralytics policy, <span style="color:#0B57D0"><strong>YOLO11</strong></span> is described in practical documentation and blog reports rather than a traditional arXiv paper.

- **Official documentation:** https://docs.ultralytics.com/models/yolo11/  
- **Ultralytics official blog (launch announcement):**  
  https://www.ultralytics.com/blog/ultralytics-yolo11-has-arrived-redefining-performance-and-versatility

## 2. Official Source Code and Project Page

- **Official GitHub repository:** https://github.com/ultralytics/ultralytics  
  Like <span style="color:#0B57D0"><strong>YOLOv8</strong></span>, it is included in the unified `ultralytics` library. You can use it immediately by installing the latest version (`pip install ultralytics --upgrade`).

- **Pre-trained weights (Assets):** https://github.com/ultralytics/assets/releases  
  You can download `.pt` files for YOLO11n, 11s, 11m, 11l, 11x, etc.

## 3. Core Technical Innovations in <span style="color:#0B57D0"><strong>YOLO11</strong></span>

- **C3k2 module:** Introduces C3k2 (Cross-Stage Partial Bottleneck with 3 convolutions and 2 kernels), improving on C2f to maximize computational efficiency while finely tuning feature extraction.  
- **C2PSA (C2f with Partial Self-Attention):** Integrates a partial self-attention layer near the top of the network to improve global context understanding while controlling computation cost.  
- **Optimized architecture:** Reduces parameters by about 22% compared to <span style="color:#0B57D0"><strong>YOLOv8</strong></span> while improving mAP, maximizing real-time performance on embedded devices.  
- **Multi-task versatility:** Shares an optimized design not only for detection but also for segmentation, pose estimation, OBB (Oriented Bounding Boxes), and classification.

---

The latest model, <span style="color:#0B57D0"><strong>YOLOv12</strong></span>, was released in February 2025. It is a milestone model that shifts the paradigm from CNN-centric designs to an attention-centric design. In particular, it has attracted major academic interest for “maximizing the benefits of self-attention while maintaining real-time performance.”

## 1. Download the <span style="color:#0B57D0"><strong>YOLOv12</strong></span> Paper

- **Title:** YOLOv12: Attention-Centric Real-Time Object Detectors  
- **Authors:** Yunjie Tian, Ge Zheng, et al. (University of Chinese Academy of Sciences and multiple research institutions)  
- **Paper link (arXiv):** https://arxiv.org/abs/2502.12524

## 2. Official Source Code and Project Page

- **Official GitHub repository:** https://github.com/sanyuan-ai/YOLOv12  
- **Related weights:** From the repository’s Release section, pre-trained models from YOLOv12-N (Nano) to YOLOv12-X (Extra Large) are provided.

## 3. Key Innovations of <span style="color:#0B57D0"><strong>YOLOv12</strong></span>

- **Area attention:** Introduces Area Attention to gain computational efficiency by focusing on neighboring regions, addressing the standard attention O(N²) complexity issue.  
- **R-ELAN (Residual Efficient Layer Aggregation Network):** Inherits the ELAN structure from <span style="color:#0B57D0"><strong>YOLOv7</strong></span>/<span style="color:#0B57D0"><strong>YOLOv9</strong></span>, while optimizing residual connections to stabilize attention-layer training.  
- **FlashAD (Flash Attention Detector):** Tunes and applies FlashAttention techniques to real-time detectors to maximize inference speed.  
- **Performance metric:** For YOLOv12-N, it achieves comparable or higher accuracy with about 20% fewer computations than the previous latest model.

---
