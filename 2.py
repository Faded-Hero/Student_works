import os
import sys
import pygame
import requests

WIDTH = 450
HEIGHT = 450
lon = '53.200425'
lat = '56.867347'
size = 10

def map_request(lo, la, Width, Height, size):
    api_server = "http://static-maps.yandex.ru/1.x/"

    lon = lo
    lat = la
    delta = "0.002"
    w = Width
    h = Height

    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "size": ",".join([w, h]),
        "l": "map"
    }
    response = requests.get(api_server, params=params)
    return response


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    response = map_request(lon, lat, WIDTH, HEIGHT)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_PAGEUP:
            if size != 17:
                size += 1
        elif event.key == pygame.K_PAGEDOWN:
            if size != 0:
                size -= 1
pygame.quit()
os.remove(map_file)