@echo off
cd C:\Users\VIRAT\Projects\industrial-conclave\EcoSort\yolov5
call yolov5-env\Scripts\activate
pip install -r requirements.txt
python train.py --img 640 --batch 16 --epochs 100 --data C:/Users/VIRAT/Projects/industrial-conclave/EcoSort/datasets/data.yaml --weights yolov5s.pt
pause