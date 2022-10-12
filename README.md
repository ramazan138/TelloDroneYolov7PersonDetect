# Official YOLOv7

Implementation of paper - [YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors](https://arxiv.org/abs/2207.02696)


## Installation

Docker environment (recommended)
<details><summary> <b>Expand</b> </summary>

``` shell
# create the docker container, you can change the share memory size if you have more.
nvidia-docker run --name yolov7 -it -v your_coco_path/:/coco/ -v your_code_path/:/yolov7 --shm-size=64g nvcr.io/nvidia/pytorch:21.08-py3

# apt install required packages
apt update
apt install -y zip htop screen libgl1-mesa-glx

# pip install required packages
pip install seaborn thop

# go to code folder
cd /yolov7
```

</details>

### detect.pt dosyasını çalıştırmadan önce Tello Drone Kendi Pc'niz ile Wifi baglantısu kurdugunuzdan emin olun !
## detect.py yürütülgü zaman baglantı sağlanıp Tello Drone camerasına baglananıp Pc ekranına görüntü gelecektir
## e tuşu = TakeOff(Yerden Kaldırma) 
## q tuşu = LannOff (Güvenli Yere İndirme)




On Tello Camera:
``` shell
python detect.py 
```

<div align="center">
    <a href="./">
        <img src="./images/photoTello/1660770154.0463047.jpg" width="59%"/>
    </a>
</div>

















