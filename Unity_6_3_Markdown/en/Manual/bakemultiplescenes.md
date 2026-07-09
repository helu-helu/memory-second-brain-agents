* [Scenes](working-with-scenes.html)
* [Work with multiple scenes in Unity](MultiSceneEditing.html)
* Bake data in multiple scenes

Set up multiple scenes

Use scripts to edit multiple scenes

# Bake data in multiple scenes

You can reduce the time taken to bake data and the size of the generated data if you bake your data into multiple **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

## Bake lightmaps with multiple scenes

To predetermine the brightness of surfaces in your scenes, you can bake [lightmaps](https://docs.unity3d.com/2022.2/Documentation/Manual/Lightmappers.html)A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap). There are two ways to bake lightmaps for multiple scenes at once:

* To automate your lightmap builds, use the [Lightmapping.BakeMultipleScenes](https://docs.unity3d.com/ScriptReference/Lightmapping.BakeMultipleScenes.html) function.
* To manually bake the lightmaps in multiple scenes, use the Unity Editor and perform the following steps:
  1. Open the scenes that you want to bake.
  2. Select **Generate Lighting**.

Shadows and GI light bounces work across all scenes, but the lightmaps and Realtime GI data loads and unloads separately for each scene. This means scenes don’t share and you can unload scenes with lightmaps safely. Scenes do share **Light Probe**Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) data so all Light Probes for scenes baked together load at the same time.

## Bake occlusion culling data with multiple scenes

You can bake **occlusion culling**A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](OcclusionCulling.html)  
See in [Glossary](Glossary.html#occlusionculling) data for multiple scenes at once to determine which **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) render:
1. Open the scenes that you want to bake.
2. Go to the Occlusion Culling window (**Window** > **Rendering** > **Occlusion Culling**).
3. Select the Bake button.
4. Save the baked scenes to make the scene-to-occlusion-data reference persistent.

This saves the occlusion culling data into a single asset called `OcclusionCullingData.asset` in a folder matching the name of the current active scene.

If you load a scene additively and it has the same occlusion data reference as the active scene, then the static renderers and portals that cull information for that scene initialize from the occlusion data. This means the occlusion system performs as if static renderers and portals are baked into a single scene.

## Additional resources

* [Creating, loading, and saving Scenes](scenes-working-with.html)
* [Setup multiple scenes](setupmultiplescenes.html)
* [Use scripts to edit multiple scenes](scriptmultiplescenes.html)

Set up multiple scenes

Use scripts to edit multiple scenes

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)