import pygame
import random
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 60
LETTER_SIZE = (40, 40)  # Define the new size (width, height) for the scaled letters


# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Letter Catcher")
clock = pygame.time.Clock()




# Load player and letter images
player_image = pygame.image.load("rocketship.png")
letter_images = [pygame.image.load("A.png"), pygame.image.load("B.png"), pygame.image.load("C.png"), pygame.image.load("D.png"), pygame.image.load("E.png"), pygame.image.load("F.png"), pygame.image.load("G.png")]


# Fonts
font = pygame.font.Font(None, 36)


#list of words
word_list = ["fed", "dab", "age", "dad", "bed"]

#function to display words
def display_word(word):
    text = font.render(word, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(5000)
    
#player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20
        self.speed_x = 0
        self.speed_y=0

    def update(self):
        self.speed_x = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x = -5
        if keys[pygame.K_RIGHT]:
            self.speed_x = 5
        if keys[pygame.K_UP]:
            self.speed_y = -5
        if keys[pygame.K_DOWN]:
            self.speed_y= 5
        
       # if keys[pygame.k_ 
        #completcode up and down
        self.rect.x += self.speed_x
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

#falling letters
class Letter(pygame.sprite.Sprite):
    def __init__(self, letter):
        super().__init__()
        original_image = letter_images[letter]
        self.image = pygame.transform.scale(original_image, LETTER_SIZE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.letter = letter
        pygame.time.wait(80)




    def update(self):
        self.rect.y += 10


def main():
    player = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)


    word = random.choice(word_list)
    display_word(word)

    letter_sprites = pygame.sprite.Group()
    score = 0

        

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        letter = random.randint(0, 4)
        falling_letter = Letter(letter)
        all_sprites.add(falling_letter)
        letter_sprites.add(falling_letter)

        all_sprites.update()
        letter_sprites.update()

        # Check for collisions
        collisions = pygame.sprite.spritecollide(player, letter_sprites, True)
        for letter in collisions:
            if letter.letter == word[0]:
                word = word[1:]
                if not word:
                    score += 10
                    word = random.choice(word_list)
                    display_word(word)

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        
        # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

