import cv2
import pygame

NUM_KEYS = 10

pygame.mixer.init()
sounds = [
    pygame.mixer.Sound('sounds/C4.mp3'),
    pygame.mixer.Sound('sounds/D4.mp3'),
    pygame.mixer.Sound('sounds/E4.mp3'),
    pygame.mixer.Sound('sounds/F4.mp3'),
    pygame.mixer.Sound('sounds/G4.mp3'),
    pygame.mixer.Sound('sounds/A4.mp3'),
    pygame.mixer.Sound('sounds/B4.mp3'),
    pygame.mixer.Sound('sounds/C5.mp3'),
    pygame.mixer.Sound('sounds/D5.mp3'),
    pygame.mixer.Sound('sounds/E5.mp3')
]

def define_keys(frame_width, frame_height):
    key_width = frame_width // NUM_KEYS
    keys = []
    y1 = 50
    y2 = 350
    for i in range(NUM_KEYS):
        x1 = i * key_width
        x2 = x1 + key_width
        dic_key = {'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2, 'pressed': False, 'prev_pressed': False, 'sound': sounds[i]}
        keys.append(dic_key)
    return keys

def draw_keys(frame, keys):
    for key in keys:
        x1, y1, x2, y2 = key['x1'], key['y1'], key['x2'], key['y2']
        color = (175, 175, 175) if key['pressed'] else (255, 255, 255)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, -1)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 6)
        cv2.rectangle(frame, (x1, 0), (x2, y1), (0, 0, 0), -1)

def check_pressed_key(keys, tips):
    for key in keys:
        key['prev_pressed'] = key['pressed']
        key['pressed'] = False

    for x, y in tips:
        for key in keys:
            if key['x1'] < x < key['x2'] and key['y1'] < y < key['y2']:
                if not key['prev_pressed']:
                    key['sound'].play()
                key['pressed'] = True