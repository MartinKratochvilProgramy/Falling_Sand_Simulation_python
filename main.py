from grid import Grid
import pygame

if __name__ == '__main__':
    grid = Grid(400, 400, 20, 20)  # (WIDTH, HEIGHT, # of division x dir, # of division y dir)

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]:
                try:
                    grid.add_sand(event.pos)
                # handles clicking out of bounds
                except AttributeError:
                    pass
            # RESET THE GRID WITH R KEY
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print("Reseting grid!")
                    grid.reset()

        grid.update()
        grid.draw()