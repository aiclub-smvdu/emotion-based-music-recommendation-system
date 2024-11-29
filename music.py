import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2 
import numpy as np 
import mediapipe as mp 
from keras.models import load_model
import webbrowser

# Paths to model and labels are hardcoded. Issue 1: Make them configurable.
model  =  # Replace with dynamic or environment-configured path.
label = # Ensure file checks before loading.

# Initialize Mediapipe tools
holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

st.header("Emotion Based Music Recommender")

# Streamlit session state initialization
if "run" not in st.session_state:
    st.session_state["run"] = "true"

# Handle missing or corrupted `emotion.npy` file. Issue 2: Improve exception handling.
try:
    emotion = 
except:
    emotion = ""

if not emotion:
    st.session_state["run"] = "true"
else:
    st.session_state["run"] = "false"

class EmotionProcessor:
    def recv(self, frame):
        # Convert frame to BGR format
        frm = frame.to_ndarray(format="bgr24")

        ##############################
        # Flip frame for a mirror effect
        frm = cv2.flip(frm, 1)

        # Mediapipe processing of frame
        res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

        lst = []

        if res.face_landmarks:
            for i in res.face_landmarks.landmark:
                lst.append(i.x - res.face_landmarks.landmark[1].x)
                lst.append(i.y - res.face_landmarks.landmark[1].y)

            # Handle left-hand landmarks. Issue 4: Optimize zero-padding for missing hands.
            if res.left_hand_landmarks:
                
            else:
                  # Add zeros if landmarks are missing.

            # Handle right-hand landmarks
            if res.right_hand_landmarks:
                for i in res.right_hand_landmarks.landmark:
                    lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                    lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
            else:
                lst.extend([0.0] * 42)

            # Prepare data for model prediction. Issue 5: Add error handling for model.predict().
            lst = np.array(lst).reshape(1, -1)
            try:
                
            except Exception as e:
                

            # Display prediction on frame. Issue 6: Text may not scale properly across resolutions.
            cv2.putText(frm, , (50, 50), , 1, (255, 0, 0), 2)

            # Save emotion state. Issue 7: Validate data before overwriting `emotion.npy`.
            np.save()

        # Draw landmarks
        drawing.draw_landmarks(
            frm, res.face_landmarks, holistic.FACEMESH_TESSELATION,
            landmark_drawing_spec=drawing.DrawingSpec(color=(0, 0, 255), thickness=-1, circle_radius=1),
            connection_drawing_spec=drawing.DrawingSpec(thickness=1)
        )
        drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS)
        drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)

        ##############################
        return av.VideoFrame.from_ndarray(frm, format="bgr24")

# Streamlit text inputs for language and singer
  # Issue 8: Add validation for input.


# WebRTC streamer to capture video input
if lang and singer and st.session_state["run"] != "false":
    webrtc_streamer(
        key="key", 
        desired_playing_state=True,
        video_processor_factory=EmotionProcessor
    )

# Button for song recommendation
btn = st.button("Recommend me songs")

if btn:
    # Handle cases where emotion is not captured. Issue 9: Validate `emotion` before proceeding.
    if not emotion:
        

    else:
        

		