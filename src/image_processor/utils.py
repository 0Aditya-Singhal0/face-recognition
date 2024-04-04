from deepface import DeepFace
import os
import pandas as pd
import cv2

os.environ["TF_FORCE_GPU_ALLOW_GROWTH"] = "true"

from tensorflow.keras import mixed_precision

# Enable mixed precision
mixed_precision.set_global_policy("mixed_float16")

models = [
    "VGG-Face",
    "Facenet",
    "Facenet512",
    "OpenFace",
    "DeepFace",
    "DeepID",
    "ArcFace",
    "Dlib",
    "SFace",
    "GhostFaceNet",
]

backends = [
    "opencv",
    "ssd",
    "dlib",
    "mtcnn",
    "retinaface",
    "mediapipe",
    "yolov8",
    "yunet",
    "fastmtcnn",
]


def find_face(frame):
    dfs = DeepFace.find(
        img_path=frame,
        db_path="pluralDB/users/",
        model_name=models[1],
        detector_backend=backends[0],
        enforce_detection=False,
        silent=True,
        normalization=models[1],
        distance_metric="euclidean_l2",
        # threshold=0.6,
    )
    return get_result_table(dfs)


def get_result_table(result: list):
    """
    Args:
        result (list): Result of the DeepFace.find() function goes here. Its a list of pandas dataframes.

    Returns:
        df (pandas.Dataframe): dataframe of the result
    """
    df = pd.DataFrame(
        columns=[
            "identity",
            "hash",
            "target_x",
            "target_y",
            "target_w",
            "target_h",
            "source_x",
            "source_y",
            "source_w",
            "source_h",
            "threshold",
            "distance",
        ]
    )
    for data in result:
        # Append pandas rows to the dataframe df
        df = pd.concat([df, data], ignore_index=True)
    return df


def draw_bounding_boxes(df, frame):
    """
    Args:
        df (pandas.DataFrame): DataFrame containing bounding box coordinates per row.
        frame (numpy.ndarray): Image frame to draw bounding boxes on.

    Returns:
        frame (numpy.ndarray): Image frame with bounding boxes drawn.
    """
    for index, row in df.iterrows():
        x = int(row["source_x"])
        y = int(row["source_y"])
        w = int(row["source_w"])
        h = int(row["source_h"])
        identity = row["identity"]
        threshold = row["threshold"]
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        frame = cv2.putText(
            frame,
            f"{str(os.path.basename(identity)).split('.')[0]} ({threshold})",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1,
        )

    return frame
