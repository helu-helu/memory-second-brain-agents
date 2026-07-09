* [Unity Editor interface](unity-editor.html)
* [Unity Editor settings reference](editor-settings-reference.html)
* [Project Settings reference](comp-ManagerGroup.html)
* 2D and 3D mode settings

Editor

Graphics

# 2D and 3D mode settings

When creating a new Project, you can specify whether to start the Unity Editor in 2D mode or 3D mode. However, you also have the option of switching the Editor between 2D mode and 3D mode at any time. You can read more about [the difference between 2D and 3D Projects here](2Dor3D.html). This page provides information about how to switch modes, and what exactly changes within the editor when you do.

## Switching between 3D and 2D modes

To change modes between 2D or 3D mode:

1. Open the [Editor](class-EditorManager.html) settings (top menu: **Edit > Project Settings**, then select the **Editor** category).
2. Then set **Default Behavior Mode** to either **2D** or **3D**.

![Use the Default Behavior Mode setting in the Editor settings to set the Project to 2D or 3D](../uploads/Main/BehaviorMode.png)


Use the Default Behavior Mode setting in the Editor settings to set the Project to 2D or 3D

## 2D vs 3D mode settings

2D or 3D mode determines some settings for the Unity Editor. These are listed below.

### In 2D Project mode:

* Any images you import are assumed to be 2D images (**Sprites**A 2D graphic objects. If you are used to working in 3D, Sprites are essentially just standard textures but there are special techniques for combining and managing sprite textures for efficiency and convenience during development. [More info](sprite/sprite-landing.html)  
  See in [Glossary](Glossary.html#Sprite)) and set to **Sprite** mode.
* The **Scene View**An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](UsingTheSceneView.html)  
  See in [Glossary](Glossary.html#SceneView) is set to 2D.
* The default game objects do not have real time, directional light.
* The **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
  See in [Glossary](Glossary.html#Camera)’s default position is at 0,0,–10. (It is 0,1,–10 in 3D Mode.)
* The camera is set to be **Orthographic**. (In 3D Mode it is **Perspective**.)
* In the Lighting Window:
  + **Skybox**A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
    See in [Glossary](Glossary.html#Skybox) is disabled for new **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
    See in [Glossary](Glossary.html#Scene).
  + **Ambient Source** is set to **Color**. (With the color set as a dark grey: RGB: 54, 58, 66.)
  + **Realtime Global Illumination** (Enlighten) is set to off.
  + **Baked Global Illumination** is enabled.
  + **Auto-Building** set to off.

### In 3D Project mode:

* Any images you import are NOT assumed to be 2D images (**Sprites**).
* The **Scene View** is set to 3D.
* The default game objects have real time, directional light.
* The camera’s default position is at 0,1,–10. (It is 0,0,–10. in 2D Mode.)
* The camera is set to be **Perspective**. (In 2D Mode it is **Orthographic**.)
* In the Lighting Window:
  + **Skybox** is the built-in default **Skybox Material**.
  + **Ambient Source** is set to **Skybox**.
  + **Realtime Global Illumination** (Enlighten) is set to on.
  + **Baked Global Illumination** is set to on.
  + **Auto-Building** is set to on.

Editor

Graphics

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)