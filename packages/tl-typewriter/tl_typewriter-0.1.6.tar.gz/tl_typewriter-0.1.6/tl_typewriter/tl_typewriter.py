import keyboard
import fire
from pathlib import Path
from loguru import logger

def main(write_to='clipboard'):
    page = 0
    picture = 1
    box = 0
    text = 0
    bubble = 0
    
    if write_to == 'clipboard':
        raise ValueError('write_to must be a path to a text file')
    write_to = Path(write_to)
    if write_to.suffix != '.txt':
        raise ValueError('write_to must be a path to a text file')
    logger.info('Using CPU')
    logger.info('typewriter start')
    while True:
        event = keyboard.read_event()
        logger.info('keyboard pressed')
        if event.event_type == 'down':
            result, page, picture, bubble, text, box = record_keystrokes(event, page, picture, bubble, text, box)
            with write_to.open('a', encoding="utf-8") as f:
                f.write(result)

def record_keystrokes(event, page, picture, bubble, text, box):
    result = ""
    if event.name == 'b':
        bubble += 1
        result = "b" + str(bubble)
        result = "P" + str(picture)  + result + ": "
    elif event.name == 'x':
        box += 1
        result = "box " + str(box)
        result = "P" + str(picture) + " " + result + ": "
    elif event.name == 't':
        text += 1
        result = "text " + str(text)
        result = "P" + str(picture) + " " + result + ": "
    elif event.name == 'space':
        picture += 1
        box = bubble = text = 0
    elif event.name == 'z':
        page += 1
        box = bubble = text = 0
        picture = 1
        result = "Page " + str(page) + "\n"
    else:
        result = ""
    return result, page, picture, bubble, text, box

if __name__ == '__main__':
    fire.Fire(main)