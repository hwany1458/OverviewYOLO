#!/usr/bin/env sh
set -eu

destination="${1:-../yolo-upstream}"
mkdir -p "$destination"

clone_if_missing() {
  name="$1"
  url="$2"
  if [ -d "$destination/$name/.git" ]; then
    echo "SKIP $name (already cloned)"
  else
    git clone --filter=blob:none "$url" "$destination/$name"
  fi
}

clone_if_missing darknet-original https://github.com/pjreddie/darknet.git
clone_if_missing darknet-yolov4 https://github.com/AlexeyAB/darknet.git
clone_if_missing yolov5 https://github.com/ultralytics/yolov5.git
clone_if_missing yolov6 https://github.com/meituan/YOLOv6.git
clone_if_missing yolov7 https://github.com/WongKinYiu/yolov7.git
clone_if_missing ultralytics https://github.com/ultralytics/ultralytics.git
clone_if_missing yolov9 https://github.com/WongKinYiu/yolov9.git
clone_if_missing yolov10 https://github.com/THU-MIG/yolov10.git
clone_if_missing yolov12 https://github.com/sunsmarterjie/yolov12.git
clone_if_missing yolov13 https://github.com/iMoonLab/yolov13.git

echo "Official repositories cloned into: $destination"
echo "Next: checkout a release tag or commit SHA and record it in each run manifest."
