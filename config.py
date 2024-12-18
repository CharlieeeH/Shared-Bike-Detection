# 配置文件
IP_CAMERA_URL = "rtsp://hucr4670@163.com:Charlie415@172.20.10.9:554/stream2" #视频流地址
YOLO_MODEL_PATH = "/mnt/c/Users/hucr/Desktop/24fall/p2/best.pt" 
# 报警设置
ALERT_FRAMES_THRESHOLD = 10  # 连续帧阈值
ALERT_COOLDOWN_TIME = 30  # 警报冷却时间（秒）
# # Replace with the actual IP address of your loudspeaker
SPEAKER_IP = "172.20.10.10"  # Example IP address
COMMAND = "mp3=00046"

# Construct the URL
SPEAKER_URL = f"http://{SPEAKER_IP}/?command={COMMAND}"