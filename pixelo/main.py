import pygame, json, os,logging as log
from pygame.locals import *
from win32api import GetSystemMetrics
class handler(log.StreamHandler):
    colors = {
        log.DEBUG: '\033[33m',
        log.INFO: '\033[36m',
        log.WARNING: '\033[1;31m',
        log.ERROR: '\033[31m',
        log.CRITICAL: '\033[101m'
    }
    reset = '\033[0m'
    fmtr = log.Formatter('%(levelname)s'+ reset +': %(message)s')
    def format(self, record):
        color = self.colors[record.levelno]
        log = self.fmtr.format(record)
        reset = self.reset
        return color + log + reset
log.basicConfig(level=log.DEBUG, handlers=[handler()])
def create_folder_structure_json(path): 
    result = {os.path.basename(path): 'name', 
              'type': 'folder', 'children': []} 
    if not os.path.isdir(path): 
        return result 
    for entry in os.listdir(path): 
        entry_path = os.path.join(path, entry) 
        if os.path.isdir(entry_path): 
            result['children'].append(create_folder_structure_json(entry_path))
        else: 
            result['children'].append({entry: 'name', 'type': 'file'}) 
    return result['children']

os.system('cls' if os.name == 'nt' else 'clear')

log.info('Welcome to Pixelo')
pygame.init()

screen = pygame.display.set_mode((GetSystemMetrics(0)-10,GetSystemMetrics(1)-10), pygame.RESIZABLE)

_theme = create_folder_structure_json('themes\\'+json.load(open('settings.json'))['enabled_theme'])


print(type(_theme))
print(_theme)

pygame.display.set_caption('Pixelo')
pygame.display.set_icon(pygame.image.load(r'pixelo\icon.png'))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False