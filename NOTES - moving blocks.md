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
Then use these in the game loop where it moves the block
```

      # move the block
      self.rect.top += self.vspeed
      self.rect.left += self.hspeed

```
Try this out. Does it do anything different?  You need some `ifs` to do the bouncing. This will start you off, can you complete it:
```

    # update the game 
    block.rect.top += block.vspeed
    block.rect.left += block.hspeed  
    if block.rect.bottom>=WINDOWHEIGHT and block.vspeed>0:
        # bounce off the bottom --- can you fill this in?

```