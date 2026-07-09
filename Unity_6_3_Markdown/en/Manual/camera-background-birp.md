* [Cameras](Cameras.html)
* [Cameras in the Built-In Render Pipeline](cameras-birp.html)
* Set the camera background with Clear Flags in the Built-In Render Pipeline

Cameras in the Built-In Render Pipeline

Camera Inspector window reference for the Built-In Render Pipeline

# Set the camera background with Clear Flags in the Built-In Render Pipeline

Each **Camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) stores color and depth information when it renders its view. The portions of the screen that are not drawn in are empty, and will display the **skybox**A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) by default. When you are using multiple Cameras, each one stores its own color and depth information in buffers, accumulating more data as each Camera renders. As any particular Camera in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) renders its view, you can set the **Clear Flags** to clear different collections of the buffer information. To do this, choose one of the following four options:

## Skybox

This is the default setting. Any empty portions of the screen will display the current Camera’s skybox. If the current Camera has no skybox set, it will default to the skybox chosen in the [Lighting Window](lighting-window.html) (menu: **Window** > **Rendering** > **Lighting**). It will then fall back to the **Background Color**. Alternatively a [Skybox component](sky-landing.html) can be added to the camera.

## Solid color

Any empty portions of the screen will display the current Camera’s **Background Color**.

## Depth only

If you want to draw a player’s gun without letting it get clipped inside the environment, set one Camera at **Depth** 0 to draw the environment, and another Camera at **Depth** 1 to draw the weapon alone. Set the weapon Camera’s **Clear Flags** to **depth only**. This will keep the graphical display of the environment on the screen, but discard all information about where each object exists in 3-D space. When the gun is drawn, the opaque parts will completely cover anything drawn, regardless of how close the gun is to the wall.

![The gun is drawn last, after clearing the depth buffer of the cameras before it](../uploads/Main/Camera-ClearFlags.jpg)


The gun is drawn last, after clearing the depth buffer of the cameras before it

## Don’t clear

This mode does not clear either the color or the **depth buffer**A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#depthbuffer). The result is that each frame is drawn over the next, resulting in a smear-looking effect. This isn’t typically used in games, and would more likely be used with a custom **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader).

Note that on some GPUs (mostly mobile GPUs), not clearing the screen might result in the contents of it being undefined in the next frame. On some systems, the screen may contain the previous frame image, a solid black screen, or random colored **pixels**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel).

Cameras in the Built-In Render Pipeline

Camera Inspector window reference for the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)