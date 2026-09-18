from ultralytics import YOLO
import cv2
import time

# Load YOLO model
model = YOLO("yolo11n.pt")

# Open input video
cap = cv2.VideoCapture("video.mp4")

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps_video = cap.get(cv2.CAP_PROP_FPS)

# Create output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    "output_tracking.mp4",
    fourcc,
    fps_video,
    (width, height)
)

# FPS calculation
prev_time = 0

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # YOLO Tracking
    results = model.track(
        frame,
        persist=True,
        conf=0.5
    )

    # Current tracked objects
    current_objects = 0

    for result in results:

        # If there are no tracking IDs
        if result.boxes.id is None:
            continue

        boxes = result.boxes

        for box in boxes:

            # Class
            cls = int(box.cls[0])

            # Confidence
            conf = float(box.conf[0])

            # Tracking ID
            track_id = int(box.id[0])

            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = map(
                int,
                (x1, y1, x2, y2)
            )

            # Object label
            label = result.names[cls]

            # Center point
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            # Count current object
            current_objects += 1

            # Draw Bounding Box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Draw Center Point
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            # Object information
            text = f"{label} ID:{track_id} {conf:.2f}"

            cv2.putText(
                frame,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    # Calculate FPS
    current_time = time.time()

    if prev_time != 0:
        fps = 1 / (current_time - prev_time)
    else:
        fps = 0

    prev_time = current_time

    # Display statistics
    cv2.putText(
        frame,
        f"Objects: {current_objects}",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"FPS: {fps:.1f}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    # Show frame
    cv2.imshow(
        "YOLO Object Tracking",
        frame
    )

    # Save frame
    out.write(frame)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()