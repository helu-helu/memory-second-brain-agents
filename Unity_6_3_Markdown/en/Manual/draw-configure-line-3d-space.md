* [Visual effects](visual-effects.html)
* [Lines and trails](visual-effects-lines-trails-billboards.html)
* [Rendering lines](rendering-lines.html)
* Draw and configure a line in 3D space

Rendering lines

Line Renderer component reference

# Draw and configure a line in 3D space

To create a **Line Renderer**A component that takes an array of two or more points in 3D space and draws a straight line between each one. You can use a single Line Renderer component to draw anything from a simple straight line to a complex spiral. [More info](class-LineRenderer.html)  
See in [Glossary](Glossary.html#LineRenderer):

1. In the Unity menu bar, go to **GameObject** > **Effects** > **Line**.
2. Select the Line Renderer **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
   See in [Glossary](Glossary.html#GameObject).
3. Add points to the Line Renderer’s Positions array, either by directly setting array values in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector) window or by using the **Create Points** **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
   See in [Glossary](Glossary.html#Scene) Editing Mode. Refer to [Access scene editing tools](#SceneEditingMode).
4. Use the Inspector window to configure the color, width, and other display settings of the line.

![Example Line Renderer configuration](../uploads/Main/LineRenderer-example.jpg)


Example Line Renderer configuration

## Set the Line Renderer Material

By default, a Line Renderer uses the built-in Material, **Default-Line**. You can make many changes to the appearance of the line without changing this Material, such as editing the color gradient or width of the line.

For other effects, such as applying a texture to the line, you will need to use a different Material. If you do not want to write your own **Shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) for the new Material, Unity’s built-in [Standard Particle Shaders](shader-StandardParticleShaders.html) work well with Line Renderers.

See [Creating and using Materials](Materials.html) for more information.

## Access scene editing tools

You can use the Line Renderer’s Inspector to change the Scene Editing Mode. Different Scene Editing Modes enable you to use the **Scene view**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
See in [Glossary](Glossary.html#SceneView) and the Inspector to edit the Line Renderer in different ways.

There are three Scene Editing Modes: **None**, **Edit Points**, and **Create Points**.

### Scene Editing Mode: None

When no Scene Editing Mode is selected, you can configure and perform a simplification operation that removes unnecessary points from the Positions array.

### Scene Editing Mode: Edit Points

When the Scene Editing Mode is set to **Edit Points**, Unity represents each point in the Line Renderer’s Positions array as a yellow sphere in the Scene view. You can move the individual points using the Move tool.

### Scene Editing Mode: Create Points

When the Scene Editing Mode is set to **Create Points**, you can click inside the Scene view to add new points to the end of the Line Renderer’s Positions array.

Rendering lines

Line Renderer component reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)