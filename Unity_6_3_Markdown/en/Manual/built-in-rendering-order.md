* [Cameras](Cameras.html)
* Render queues and sorting behaviours

Troubleshooting occlusion culling

Simulating real-world cameras with Physical Cameras

# Render queues and sorting behaviours

The order in which Unity renders objects is based on two things: which render queue the object is in, and how Unity sorts objects within that render queue.

## Render queues

Unity sorts objects into groups called render queues. Unity renders the contents of one render queue, and then renders the contents of another render queue, and so on.

Unity has the following named render queues, which it renders in the following order:

| **Name** | **Index** | **Description** |
| --- | --- | --- |
| **Background** | 1000 | Use this queue for anything that should be drawn in the background of your **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene). |
| **Geometry** | 2000 | Use this queue for opaque geometry. This is the default queue. |
| **AlphaTest** | 2450 | Use this queue for alpha tested geometry. This is after the **Geometry** queue because it’s more efficient to render alpha-tested objects after all solid ones are drawn. |
| **Transparent** | 3000 | Use this queue for anything alpha-blended (shaders that don’t write to the depth buffer). Examples include glass, or **particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html) See in [Glossary](Glossary.html#particle) effects. |
| **Overlay** | 4000 | Use this queue for effects that are rendered on top of everything else, such as **lens flares**A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](class-LensFlare.html) See in [Glossary](Glossary.html#LensFlare). |

Note that **Skybox**A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) materials are a special case. Unity draws Skybox materials after all opaque geometry (after queue index 2500), but before all transparent geometry (before queue index 2501).

## Sorting behaviors within render queues

Within each render queue, Unity sorts and draws objects based on their distance from the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera). The sorting behavior depends on the index of the render queue:

* For queues with an index up to and including 2500 (Geometry + 500), Unity sorts Renderers in these queues using the behavior defined in [OpaqueSortMode.FrontToBack](../ScriptReference/OpaqueSortMode.FrontToBack.html) by default.
* For queues with an index of 2501 or above, Unity sorts Renderers in these queues using the behavior defined in [TransparencySortMode.Default](../ScriptReference/TransparencySortMode.Default.html) by default.

## Set how a camera sorts materials

How you change the sorting behavior within a render queue depends on the index of the render queue:

* For queues with an index up to and including 2500 (Geometry + 500), you can change the opaque sort mode for a Camera by using the [Camera.opaqueSortMode](../ScriptReference/Camera-opaqueSortMode.html) API.
* For queues with an index of 2501 or above, you can change the default transparent sort mode by using the [Rendering.GraphicsSettings-transparencySortMode](../ScriptReference/Rendering.GraphicsSettings-transparencySortMode.html) API. You can change the transparent sort mode for a Camera by using the [Camera.transparencySortMode](../ScriptReference/Camera-transparencySortMode.html) API.

Troubleshooting occlusion culling

Simulating real-world cameras with Physical Cameras

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)