import cv2

input_folder = '/Users/a20/Documents/spring2024/4527_cv/projects/project3/assets/output_frames'
video_fps = 30
width, height = 1280, 720
output_video_path = '/Users/a20/Documents/spring2024/4527_cv/projects/project3/assets/bird.mp4'

out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'mp4v'), video_fps, (width, height))

frame_count = 556

for i in range(frame_count):
    frame_path = f"{input_folder}/frame{i}.jpg"
    frame = cv2.imread(frame_path)
    out.write(frame)

out.release()
