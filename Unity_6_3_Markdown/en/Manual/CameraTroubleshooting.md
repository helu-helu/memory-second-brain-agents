* [Cameras](Cameras.html)
* Troubleshooting cameras

Camera Inspector window reference for the Built-In Render Pipeline

World building

# Troubleshooting cameras

Solve common issues with **cameras**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera), such as flickering lights and shadows.

## Reduce flickering

### Symptoms

Objects, lights, and shadows flicker if they’re far away.

### Cause

The flickering occurs because distances are too large to calculate positions precisely with floating point math. In each frame, the object, light, or shadow is at a slightly different position, so it moves in and out of the view frustum.

### Resolution

To minimize flickering, use one of the following approaches:

* Reduce the far **clipping plane**A plane that limits how far or close a camera can see from its current position. A camera’s viewable range is between the far and near clipping planes. See far clipping plane and near clipping plane. [More info](class-Camera.html)  
  See in [Glossary](Glossary.html#clippingplane) distance in the Camera **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
  See in [Glossary](Glossary.html#Inspector) window to avoid the distance of objects becoming too large for precise calculations.
* Make everything in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
  See in [Glossary](Glossary.html#Scene) smaller, to reduce distances across your whole scene.
* Enable camera-relative culling, so Unity uses the camera position as the relative position for shadow calculations. For more information, refer to [Culling settings in Graphics settings](class-GraphicsSettings.html#culling-settings).

## Reduce tearing

### Symptoms

A ‘tear’ across the screen, where the top and bottom halves don’t match up.

![Simulated example of tearing. The shift in the picture is visible in the magnified portion.](../uploads/Main/Tearing.jpg)


Simulated example of tearing. The shift in the picture is visible in the magnified portion.

### Cause

Updates in Unity aren’t synchronized with updates of the display device, so Unity might send a new frame while the display device is still rendering the previous frame. This results in a visible ‘tear’ at the position the frame changes.

### Resolution

To reduce tearing, go to **Edit** > **Project Settings** > **Quality**, then set **VSync Count** to one of the following:

* **Every V Blank** to send frames only during the periods when the display device isn’t updating, which is called its vertical blank.
* **Every Second V Blanks** to send frames during every other vertical blank. Use this value if your project takes longer than one update of the display device to render a frame.

## Additional resources

* [Quality settings](class-QualitySettings.html)
* [Camera Inspector windows reference for URP](urp/camera-components-reference-landing.html)
* [Camera Inspector window reference for the Built-In Render Pipeline](class-Camera.html)

Camera Inspector window reference for the Built-In Render Pipeline

World building

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)