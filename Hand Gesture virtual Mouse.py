import cv2
import mediapipe as mp
import pyautogui

# Initialize Mediapipe Hands and PyAutoGUI
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

# Screen Width and Height
screen_width, screen_height = pyautogui.size()

# Webcam
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            index_x = int(hand_landmarks.landmark[8].x * frame_width)
            index_y = int(hand_landmarks.landmark[8].y * frame_height)

            thumb_x = int(hand_landmarks.landmark[4].x * frame_width)
            thumb_y = int(hand_landmarks.landmark[4].y * frame_height)

            # Move Mouse
            mouse_x = int(index_x * screen_width / frame_width)
            mouse_y = int(index_y * screen_height / frame_height)
            pyautogui.moveTo(mouse_x, mouse_y)

            # Click Gesture (Thumb and Index close together)
            distance = abs(index_x - thumb_x)
            if distance < 40:
                pyautogui.click()
                cv2.putText(frame, "Click", (index_x, index_y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
