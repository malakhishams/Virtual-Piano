import cv2
#import piano_hand_tracker as detector
import virtual_piano as piano

from piano_hand_tracker import HandDetector

#print(dir(piano_hand_tracker))

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WINDOW_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, WINDOW_HEIGHT)


actual_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
actual_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

tracker = HandDetector(detectconf=0.8)
keys = piano.define_keys(actual_w, actual_h)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame = tracker.FindHands(frame)
    landmarkslist = tracker.FindPosition(frame)

    tips = []
    if len(landmarkslist) != 0:
    # hand 0
        lm0 = tracker.FindPosition(frame, handnum=0)
        tips += [(lm[1], lm[2]) for lm in lm0 if lm[0] in tracker.tipsID]
        
    # hand 1 if it exists
    if tracker.result.multi_hand_landmarks and len(tracker.result.multi_hand_landmarks) > 1:
        lm1 = tracker.FindPosition(frame, handnum=1)
        tips += [(lm[1], lm[2]) for lm in lm1 if lm[0] in tracker.tipsID]

    piano.check_pressed_key(keys, tips)
    piano.draw_keys(frame, keys)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()