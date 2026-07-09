* [Lighting](LightingOverview.html)
* [Direct and indirect lighting](direct-and-indirect-lighting.html)
* [Lighting data](Lightmap-data-landing.html)
* Introduction to lighting data

Lighting data

Lighting Data Assets

# Introduction to lighting data

Precomputed lighting data and baked lighting are not the same.

Baked lighting data is static. For example, the appearance of a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) can change as it moves around a **Light Probe**Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) (if that GameObject has Contribute Global Illumination enabled). However, the data in the Light Probe itself does not change.
Unity can store baked lighting data in **lightmaps**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap), Light Probes, and Reflection Probes.

Enlighten Realtime **Global Illumination**A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) does not rely on baked lighting. Instead, it uses precomputed visibility data to speed up the process of determining how a light moving in real-time affects the surfaces that its rays can reach.

## Generating lighting data

The Editor follows different steps to calculate **Enlighten**A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](Glossary.html#Enlighten) Realtime Global Illumination and Baked Global Illumination. The progress bar displays information about the current process. You can continue working in the Editor while the processes run.

The stages of lighting precomputation are listed below:

**Enlighten Realtime Global Illumination**

1. Create Geometry
2. Layout Systems
3. Create Systems
4. Create Atlas
5. Clustering
6. Visibility
7. Light Transport
8. Tetrahedralize Probes
9. Create ProbeSet

**Probes**

1. Ambient Probes
2. Baked/Realtime Ref. Probes

## Generating data

Unity’s precomputed lighting solutions only consider static geometry. To begin the lighting precompute process, you need at least one [Static](https://docs.unity3d.com/Manual/StaticObjects.html) **GameObject** in your ****Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene)**.

When you initiate a precompute, the Unity Editor evaluates and computes all aspects of your Scene lighting. To recalculate and bake only [Reflection Probes](class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe), select the **Generate Lighting** option **Reflection Probes** [Lighting Window](lighting-window.html).

## Before you build

Before building your game, generate the lighting data for all your Scenes, to ensure that you do not lose any lighting data.

When you generate lighting for your Scene, Unity saves your lighting data as Asset files in your project directory. This ensures that the data you need is part of your build.

Lighting data

Lighting Data Assets

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)