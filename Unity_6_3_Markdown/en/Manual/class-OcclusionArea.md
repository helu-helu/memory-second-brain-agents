* [Cameras](Cameras.html)
* [Excluding hidden objects with occlusion culling](OcclusionCulling-landing.html)
* Create high-precision occlusion areas

Cull moving GameObjects

Control occlusion in areas with Occlusion Portals

# Create high-precision occlusion areas

[Switch to Scripting](../ScriptReference/OcclusionArea.html "Go to OcclusionArea page in the Scripting Reference")

Use the Occlusion Area component to define View Volumes in the **occlusion culling**A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#occlusionculling) system. View Volumes are areas of the **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) where the **Camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) is likely to be located at runtime. At bake time, Unity generates higher precision data within View Volumes. At runtime, Unity performs higher precision calculations when the Camera’s position is within a View Volume.

If you have not defined any View Volumes in your Scene, Unity creates a View Volume at bake time that contains all Scene geometry that is marked as Occluder Static or Occludee Static. This can lead to unnecessarily large data size, slow bake times and resource-intensive runtime calculations in large or complex Scenes. To avoid this, place Occlusion Areas in your Scene to define View Volumes for the areas where the Camera is likely to be.

## Using an Occlusion Area component to define a View Volume

1. Add an **Occlusion Area** component to an empty **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
   See in [Glossary](Glossary.html#GameObject) in your Scene
2. In the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector) window, configure the **Size** property so that the **bounding volume**A closed shape representing the edges and faces of a collider or trigger.  
   See in [Glossary](Glossary.html#boundingvolume) covers the desired area
3. In the Inspector window, enable **Is View Volume**

## Occlusion Area component reference

| ***Property:*** | ***Function:*** |
| --- | --- |
| **Size** | Set the size of the Occlusion Area. |
| **Center** | Set the center of the Occlusion Area. By default this is 0,0,0 and is located in the center of the box. |
| **Is View Volume** | If enabled, the Occlusion Area defines a View Volume. If disabled, the Occlusion Area does not define a View Volume. This must be enabled for an Occlusion Area to work. |

OcclusionArea

Cull moving GameObjects

Control occlusion in areas with Occlusion Portals

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)