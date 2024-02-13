import pygame as pg
import requests
from io import BytesIO

pg.init()

win = pg.display.set_mode((600, 450))
clk = pg.time.Clock()

url = 'https://static-maps.yandex.ru/1.x/'

spn = 0.1
map_type = 'map'
lon, lat = 50, 50

image = pg.Surface((600, 450))


def get_map():
    global image
    resp = requests.get(url, params={
        'll': ','.join(map(str, [lon, lat])),
        'spn': ','.join(map(str, [spn, spn])),
        'l': map_type
    })
    print(resp)
    if not resp:
        print(resp.status_code, resp.url)
    imgio = BytesIO(resp.content)
    image = pg.image.load(imgio)
    imgio.close()


get_map()

running = True
while running:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            running = False
    win.fill((0, 0, 0))
    win.blit(image, (0, 0))
    pg.display.update()

pg.quit()


