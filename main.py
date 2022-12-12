import json
from scenes import *



key = {
    "First": pygame.K_d,
    "Second": pygame.K_f,
    "Third": pygame.K_j,
    "Fourth": pygame.K_k
}



with open("data\key.json", "w") as outfile:
    json.dump(key, outfile)








maingame()