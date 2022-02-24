from vidstream import CameraClient
from vidstream import VideoClient
from vidstream import ScreenShareClient

client3 = ScreenShareClient('ip do reciver', 9999)

client3.start_stream()