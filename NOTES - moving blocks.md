# Code club - moving blocks

### Recap from last week
- using Pygame to display a block
- changing colours
- making the block move : using `top` and `left`
- the game loop : draw - inputs - update - timing

### Things we'll add this week
- making the block bounce of the edge of the screen : editing the block script
- creating several blocks
- controlling a block with the keyboard : using events
- using an image instead of a rectangle

### Blocks that bounce
First create some speed variables to control the block movement. This will make it easier to change direction.
Make these part of the block's script, like this: 
```

# Define the block sprite
class Block:
    def __init__(self, a, b, c, d, colour):                 
        self.rect = pygame.Rect(a, b, c, d)
        self.colour = colour
        self.vspeed = 0
        self.hspeed = 0

```
Then set the value when you create the block:
```

# create a block sprite        
block = Block(100,100,100,100, BLUE)
block.vspeed = 2
block.hspeed = 1

```
Then use these in the game loop where it moves the block
```

      # move the block
      self.rect.top += self.vspeed
      self.rect.left += self.hspeed

```
Try this out. Does it do anything different?  What else are you going to need to bounce off the edge? 
