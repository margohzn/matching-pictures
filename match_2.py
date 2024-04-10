import pygame 

pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill((0,0,128))

pygame.display.update()

salt = pygame.image.load("salt.png")
peanutbutter = pygame.image.load("peanut_butter.png")
macaroni = pygame.image.load("macaroni.png")
cat = pygame.image.load("cat.png")

screen.blit(salt, (150,100))
screen.blit(peanutbutter, (150,200))
screen.blit(macaroni, (150,300))
screen.blit(cat, (150,400))

pygame.display.update()


font = pygame.font.SysFont("Arial", 30)


text_1 = font.render("Salt", True, "green")
text_2 = font.render("Peanut Butter", True, "blue")
text_3 = font.render("Macaroni", True, "purple")
text_4 = font.render("Cat", True, "pink")

screen.blit(text_1, (350,100))
screen.blit(text_2, (350,200))
screen.blit(text_3, (350,300))
screen.blit(text_4, (350,400))

pygame.display.update()