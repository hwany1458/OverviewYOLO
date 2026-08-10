# Official source code, model weights, and environments

This document points to upstream resources. OverviewYOLO does not redistribute third-party source trees, checkpoints, or datasets.

## Official implementation registry

| Version(s) | Upstream repository | Weight/config source | Framework family | License observed in current upstream | Reproduction note |
|---|---|---|---|---|---|
| YOLOv1–v3 | [pjreddie/darknet](https://github.com/pjreddie/darknet) | [pjreddie.com YOLO pages](https://pjreddie.com/darknet/yolo/) and repository links | C/CUDA Darknet | YOLO license states Darknet is public domain | Historical CUDA/compiler compatibility may require a container or maintained fork; architectural validation should use original cfg files |
| YOLOv4 | [AlexeyAB/darknet](https://github.com/AlexeyAB/darknet) | Repository release/README links | C/CUDA Darknet | Verify at pinned revision | Use the exact cfg/weights pair; distinguish regular, CSP, tiny, and scaled variants |
| YOLOv5 | [ultralytics/yolov5](https://github.com/ultralytics/yolov5) | [Releases](https://github.com/ultralytics/yolov5/releases) | PyTorch | AGPL-3.0; separate enterprise option advertised | Pin v7.0 or the exact manuscript source; do not replace with YOLOv5u |
| YOLOv6 | [meituan/YOLOv6](https://github.com/meituan/YOLOv6) | [Releases](https://github.com/meituan/YOLOv6/releases) and README links | PyTorch / TensorRT paths | GPL-3.0 | Record v1/v2/v3 generation, scale, P5/P6, precision, and TensorRT settings |
| YOLOv7 | [WongKinYiu/yolov7](https://github.com/WongKinYiu/yolov7) | [Release assets](https://github.com/WongKinYiu/yolov7/releases) | PyTorch | GPL-3.0 | Use the converted/deploy artifact appropriate to the paper table; identify tiny, standard, W6, E6, D6, or E6E |
| YOLOv8 | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | Model names in [YOLOv8 docs](https://docs.ultralytics.com/models/yolov8/) | Ultralytics/PyTorch | AGPL-3.0; separate enterprise option advertised | Record package version because docs and runtime are living sources |
| YOLOv9 | [WongKinYiu/yolov9](https://github.com/WongKinYiu/yolov9) | Repository README links | PyTorch | GPL-3.0 | Training and converted inference graphs differ; retain the artifact name |
| YOLOv10 | [THU-MIG/yolov10](https://github.com/THU-MIG/yolov10) | [Release assets](https://github.com/THU-MIG/yolov10/releases) | Ultralytics-derived PyTorch | AGPL-3.0 | Separate end-to-end latency from any traditional NMS path |
| YOLO11 | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | Model names in [YOLO11 docs](https://docs.ultralytics.com/models/yolo11/) | Ultralytics/PyTorch | AGPL-3.0; separate enterprise option advertised | Record package version, model scale, task, export format, and runtime |
| YOLOv12 | [sunsmarterjie/yolov12](https://github.com/sunsmarterjie/yolov12) | [Release assets](https://github.com/sunsmarterjie/yolov12/releases) | Ultralytics-derived PyTorch | AGPL-3.0 | Prefer the authors’ repository; identify base versus turbo and the release used |
| YOLOv13 | [iMoonLab/yolov13](https://github.com/iMoonLab/yolov13) | README model links | Ultralytics-derived PyTorch; optional FlashAttention | AGPL-3.0 | Pin a commit; record FlashAttention/CUDA/Torch versions and whether the reported path uses it |
| YOLO26 | [ultralytics/ultralytics](https://github.com/ultralytics/ultralytics) | Model names in [YOLO26 docs](https://docs.ultralytics.com/models/yolo26/) | Ultralytics/PyTorch | AGPL-3.0; separate enterprise option advertised | Record `end2end=True/False`; one-to-one and one-to-many outputs are not the same evaluation path |

## Why this repository does not vendor upstream code

The upstream projects use different frameworks, dependency generations, and licenses. Copying them into one repository would:

- obscure their revision history and license notices;
- create dependency conflicts;
- make a single environment appear reproducible when it is not;
- increase the risk of accidentally redistributing restricted model or dataset artifacts; and
- make future security and upstream corrections harder to track.

Use isolated environments and write the upstream commit SHA into each run manifest.

## Recommended environment groups

| Group | Models | Isolation strategy |
|---|---|---|
| `darknet-original` | YOLOv1–v3 | Legacy CUDA-compatible container or documented CPU build |
| `darknet-alexeyab` | YOLOv4 family | Separate container pinned to the chosen Darknet revision |
| `yolov5` | YOLOv5 | Official release tag in its own virtual environment/container |
| `yolov6` | YOLOv6 | Official requirements and TensorRT version in its own container |
| `yolov7` | YOLOv7 | Official repository environment; do not share with current Ultralytics |
| `ultralytics-v8` | YOLOv8 | Package/repository revision captured with the run |
| `yolov9` | YOLOv9 | Official repository environment |
| `yolov10` | YOLOv10 | Official repository release in its own environment |
| `ultralytics-v11` | YOLO11 | Versioned Ultralytics environment |
| `yolov12` | YOLOv12 | Authors’ fork in its own environment |
| `yolov13` | YOLOv13 | Authors’ fork with explicitly recorded FlashAttention configuration |
| `ultralytics-26` | YOLO26 | Version containing the paper-aligned checkpoints/training recipe |

Sharing one modern Ultralytics installation across YOLOv8, YOLO11, and YOLO26 may be convenient for application testing, but it is not sufficient for historical reproduction unless the exact model code and checkpoint provenance are retained.

## Model and weight identity

Every weight record should include:

- canonical model name and task;
- upstream download URL;
- upstream tag or commit;
- local filename;
- byte size;
- SHA-256 checksum;
- training dataset and split stated by upstream;
- whether the weight is original, converted, fused, pruned, quantized, or fine-tuned;
- expected preprocessing; and
- license/access note.

Do not rely on a filename such as `best.pt` or `yolov13n.pt` alone.

## Evaluation entry points

Commands below are orientation examples. The pinned upstream README is authoritative, and each completed run must store the exact command actually used.

### Darknet family

```bash
./darknet detector map <data-file> <cfg-file> <weights-file>
```

### YOLOv5

```bash
python val.py --weights <weights> --data <dataset-yaml> --img 640 --batch-size 1 --save-json
```

### YOLOv6

```bash
python tools/eval.py --data <dataset-yaml> --weights <weights> --task val --device 0 --half
```

### YOLOv7

```bash
python test.py --data <dataset-yaml> --weights <weights> --img 640 --batch-size 1 --device 0 --save-json
```

### YOLOv9

```bash
python val.py --data <dataset-yaml> --weights <converted-weights> --img 640 --batch-size 1 --device 0 --save-json
```

### Ultralytics-style repositories

```bash
yolo detect val model=<weights> data=<dataset-yaml> imgsz=640 batch=1 device=0 save_json=True
```

For YOLO26, add the explicit head mode used by the installed release, for example `end2end=True` or `end2end=False`. Do not infer the mode from the model name.

## Deployment/export records

For every ONNX, TensorRT, OpenVINO, CoreML, TFLite, NCNN, RKNN, or other export, record:

- source weight checksum;
- exporter version and command;
- opset and dynamic/static shape;
- precision and calibration method;
- input/output tensor names and shapes;
- inclusion or exclusion of decode and NMS;
- runtime and provider versions;
- target hardware;
- validation delta against the source checkpoint; and
- exported artifact checksum.

An exported engine is a separate experimental artifact, not merely another filename for the PyTorch model.

## Influential derivative repositories

| Model | Official/author-linked repository | Current license signal | Main reason to include |
|---|---|---|---|
| Scaled-YOLOv4 | [WongKinYiu/ScaledYOLOv4](https://github.com/WongKinYiu/ScaledYOLOv4) | GPL-3.0 | Scaling strategy and large-model frontier |
| YOLOR | [WongKinYiu/yolor](https://github.com/WongKinYiu/yolor) | Verify pinned revision | Unified representation and multi-task direction |
| YOLOX | [Megvii-BaseDetection/YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) | Apache-2.0 | Anchor-free head, decoupling, SimOTA |
| PP-YOLO family | [PaddlePaddle/PaddleDetection](https://github.com/PaddlePaddle/PaddleDetection) | Apache-2.0 for toolkit; verify included components | Industrial Paddle implementation and deployment |
| YOLO-NAS | [Deci-AI/super-gradients](https://github.com/Deci-AI/super-gradients) | Verify code and weight terms separately | NAS- and quantization-oriented deployment |

## Source acquisition helper

Run the included helper with a destination outside the OverviewYOLO repository:

```bash
bash scripts/clone_official_sources.sh ../yolo-upstream
```

After cloning, replace branch tips with release tags or commit SHAs in each experiment record. The helper intentionally does not download model weights or datasets.
