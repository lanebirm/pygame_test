import pygame


def main():
    print("test")
    gui = GUI_Support()
    xWidth = 800
    yHeight = 600
    screen = gui.initDisplay((xWidth, yHeight))
    handX = 200
    handY = 100
    handZ = 1501
    x = 50
    y = 50

    gui.drawGraphics((handX, handY, handZ), screen, (xWidth, yHeight))
    gui.displayMetrics(f'X: {x},Y: {y},Z: ', screen)
    pygame.display.update()

    while 1:
        if gui.isQuit():
            break


class GUI_Support:

    def initDisplay(self, dims):
        pygame.init()
        return pygame.display.set_mode(dims)

    def isQuit(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            else:
                return False

    def buttonTracker(self, inc, dec, stater):
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[inc]:
            stater = stater + 10 if stater < 100 else stater
        if keys[dec]:
            stater = stater - 10 if stater > 0 else stater
        return stater

    def drawGraphics(self, position, screen, dims):
        handX, handY, handZ = position
        width, height = dims
        screen.fill((0, 0, 0))
        pygame.draw.line(screen, (255, 0, 0), (0, handY), (width, handY))
        pygame.draw.line(screen, (0, 255, 0), (handX, 0), (handX, height))

        circleRadius = int(handZ / 20) if (handZ / 20) > 0 else 1
        pygame.draw.circle(screen, (0, 0, 255), (handX, handY), circleRadius)

    # thank you Sentdex <3
    def getTextObjects(self, text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()

    def drawText(self, text, y, fontSize, screen):
        largeText = pygame.font.Font('Lato-Medium.ttf', fontSize)
        TextSurf, TextRect = self.getTextObjects(text, largeText)
        TextRect.left = 0
        TextRect.top = y
        screen.blit(TextSurf, TextRect)

    def displayMetrics(self, data, screen):
        fontSize = 25
        data = data.split(',')
        for i in range(len(data)):
            self.drawText(data[i], i * fontSize, fontSize, screen)


if __name__ == "__main__":
    main()
