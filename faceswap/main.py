import cv2
import argparse
from face_swaps.face_swap import swap_faces

class FaceSwapCamera:
    def __init__(self, filename):
        # 读取传入的图像
        self.img2 = cv2.imread(filename)
        if self.img2 is None:
            raise ValueError(f"无法读取图像文件: {filename}")
        # 打开摄像头
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise RuntimeError("无法打开摄像头")

    def run(self):
        while True:
            # 从摄像头读取一帧
            ret, frame = self.cap.read()
            
            if not ret:
                print("无法接收帧（流结束？）")
                break

            # 进行人脸交换
            try:
                swapped_frame = swap_faces(self.img2, frame)
            except Exception as e:
                swapped_frame = frame
            # swapped_frame = swap_faces(frame, self.img2)
            # 在窗口中显示当前帧
            cv2.imshow('Camera Feed', swapped_frame)

            # 按下 'q' 键退出
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # 释放摄像头并关闭所有窗口
        self.cap.release()
        cv2.destroyAllWindows()

def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="实时摄像头人脸交换")
    parser.add_argument('filename', nargs='?', default="images/donald_trump.jpg", help="要交换的人脸图片路径 (默认: images/donald_trump.jpg)")
    args = parser.parse_args()

    # 初始化并运行人脸交换
    try:
        face_swap_camera = FaceSwapCamera(args.filename)
        face_swap_camera.run()
    except Exception as e:
        print(f"程序出现错误: {e}")

if __name__ == '__main__':
    main()
