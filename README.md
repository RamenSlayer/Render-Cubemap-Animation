# Render-Cubemap-Animation
A blender addon I made for rendering animations with reflection cubemaps

## Update
Seems to still work for 4.0.1. Why this is still not an option in blender itself I do not know.

## Main
For some reason I couldn't think of, EEVEE in blender doesn't support updating reflection cubemaps during animation. So on frame 3000 you are going to have a reflection of frame 1. Not great. I based the code on [this thread](https://blenderartists.org/t/baking-reflection-cubemaps-every-frame-of-an-animation/1245233) and made it an addon. 

This addon renders your animation as a frame sequence and saves it into a folder of your choosing. Unfortunately you can't stop the rendering mid process, but it being a frame sequence you can kill it and resume from last frame. 
Only supports rendering images, not animations. So be sure to set the format you want in the render tab.

## TODO
Not like I'm going to do this BUT
1. Pick up the location from the render tab. Is that possible? Should be.
2. Move the menu to the render tab. Should be ez but idk how. And since it's been quite some time would have to relearn it. Though I MIGHT do it.
