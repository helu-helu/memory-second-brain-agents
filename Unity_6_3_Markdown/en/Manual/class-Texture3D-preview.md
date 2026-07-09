* [Materials and shaders](materials-and-shaders.html)
* [Custom textures](Textures-landing.html)
* [3D textures](class-Texture3D.html)
* Preview a 3D texture

Create a 3D texture

Sample a 3D texture in a shader

# Preview a 3D texture

To preview a 3D texture, do one of the following:

* Use the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
  See in [Glossary](Glossary.html#Inspector) window.
* Draw the 3D texture in the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
  See in [Glossary](Glossary.html#Scene) view.

## Use the Inspector window

To preview a 3D texture, select the texture in the **Project** window. In the **Inspector** window, Unity displays the preview of the texture at the bottom of the **Texture Import Settings** window.

There are three different 3D texture preview modes available:

* **Volume** mode displays the 3D texture as a translucent cube. Click and drag the cube to rotate the preview.
* **Slice** mode displays a 2D slice of each of the three axes of the 3D texture. Use the **X**, **Y** and **Z** sliders to select the slices to preview.
* **SDF** mode displays the 3D texture as a signed distance field (SDF) in 3D space.

Refer to [3D texture preview reference](class-Texture3D-reference.html) for more information.

## Draw the 3D texture in the Scene view

Use the [`Handles`](../ScriptReference/Handles.html) API to draw the 3D texture in the **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView). The `Handles` API lets you use custom gradients and configure how you draw the texture.

Refer to the following for more information:

* [`Handles.DrawTexture3DVolume`](../ScriptReference/Handles.DrawTexture3DVolume.html)
* [`Handles.DrawTexture3DSlice`](../ScriptReference/Handles.DrawTexture3DSlice.html)
* [`Handles.DrawTexture3DSDF`](../ScriptReference/Handles.DrawTexture3DSDF.html)

Create a 3D texture

Sample a 3D texture in a shader

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)