# Render-Cubemap-Animation
An addon I made for rendering animations with reflection cubemaps

For some reason I couldn't think of, EEVEE in blender doesn't support updating reflection cubemaps during animation. So on frame 3000 you are going to have a reflection of frame 1. Not great. I based the code on [this thread](https://blenderartists.org/t/baking-reflection-cubemaps-every-frame-of-an-animation/1245233) and made it an addon. 

This addon renders your animation as a frame sequence and saves it into a folder of your choosing. Unfortunately you can't stop the rendering mid process, but it being a frame sequence you can kill it and resume from last frame. 
