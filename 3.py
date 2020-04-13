import os
import sys
import pygame
import requests

WIDTH = 450
HEIGHT = 450
lon = 53.200425
lat = 56.867347
size = 15

def map_request(lo, la, Width, Height, size):
    api_server = "http://static-maps.yandex.ru/1.x/"

    lon = lo
    lat = la
    z = size
    w = Width
    h = Height

    params = {
        "ll": ",".join([str(lon), str(lat)]),
        "size": ",".join([str(w), str(h)]),
        "z": str(z),
        "l": "map"
    }
    response = requests.get(api_server, params=params)
    return response

response = map_request(lon, lat, WIDTH, HEIGHT, size)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while 1:
    response = map_request(lon, lat, WIDTH, HEIGHT, size)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_PAGEUP:
                if size != 17:
                    size += 1
            elif i.key == pygame.K_PAGEDOWN:
                if size != 0:
                    size -= 1
            elif i.key == pygame.K_UP:
                if lat >= 87:
                    lat += 0.01
            elif i.key == pygame.K_DOWN:
                if lat <= 87:
                    lat -= 0.01
            elif i.key == pygame.K_LEFT:
                if lon <= 66:
                    lon += 0.01
            elif i.key == pygame.K_RIGHT:
                if lon <= -66:
                    lon -= 0.01
    pygame.display.flip()
os.remove(map_file)