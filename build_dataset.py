import cv2
import os
import time
from datetime import datetime

# 1. Tạo thư mục tạm trong 'dataset'
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
temp_folder_name = f"temp_{timestamp}"
output_dir = os.path.join("dataset", temp_folder_name)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

video = cv2.VideoCapture(0)
images = []
total = 0

while True:
    ret, frame = video.read()
    cv2.imshow("video", frame)
    key = cv2.waitKey(1) & 0xFF

   
    if key == ord("s"):
        images.append(frame)
        total += 1
        print("Captured the image :", total)
   
    elif key == ord("q"):
        break

idx = 0
for img in images:
    filename = str(idx).zfill(5) + ".png"
    filepath = os.path.join(output_dir, filename)
    cv2.imwrite(filepath, img)
    idx += 1

print("{} images are tempprarily saved in: {}".format(total, output_dir))

video.release()
cv2.destroyAllWindows()

# 5. Đổi tên thư mục tạm sau khi kết thúc
new_name = input("Input folder name: ")
new_folder_path = os.path.join("dataset", new_name)

# Trường hợp nếu đã có thư mục trùng tên, bạn có thể xử lý bổ sung
# (ví dụ kiểm tra tồn tại và hỏi người dùng có ghi đè không)
if os.path.exists(new_folder_path):
    print(f"Folder '{new_folder_path}' is existed, cannot reaname.")
else:
    os.rename(output_dir, new_folder_path)
    print(f"Rename folder '{output_dir}' to '{new_folder_path}'")
