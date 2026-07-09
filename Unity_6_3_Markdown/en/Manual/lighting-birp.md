* [Lighting](LightingOverview.html)
* Lighting in the Built-In Render Pipeline

Light component Inspector window reference for URP

Per-pixel and per-vertex lights in the Built-In Render Pipeline

# Lighting in the Built-In Render Pipeline

Resources and approaches for lighting in the Built-In **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline).

| **Page** | **Description** |
| --- | --- |
| [Per-pixel and per-vertex lights in the Built-In Render Pipeline](PerPixelLights-BuiltIn.html) | Learn about how Unity categorizes Light components so they light objects per-pixel or per-vertex. |
| [Emit light from a GameObject](lighting-emissive-materials.html) | Make a material emissive so that it emits light across its surface area. |
| [Create cookies](creating-cookies-built-in-render-pipeline.html) | Create a cookie by creating a grayscale texture, importing the texture into Unity, then converting the brightness of the texture to alpha. |
| [Customize how shaders contribute lightmap data](MetaPass.html) | Make **shaders**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) compatible with **lightmap**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html) See in [Glossary](Glossary.html#Lightmap) textures. |
| [Shadows in the Built-In Render Pipeline](shadows-in-birp.html) | Set the resolution of the shadow map a Light component generates. |
| [Configure a GameObject to sample more Light Probes](LightProbeProxyVolume-landing.html) | To make lighting more realistic, use **Light Probe**Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html) See in [Glossary](Glossary.html#LightProbe) Proxy Volumes to configure a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html) See in [Glossary](Glossary.html#GameObject) to sample multiple Light Probes. |
| [Blend Reflection Probes](blend-reflection-probes-birp.html) | Enable Unity gradually fading between the **cubemap**A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html) See in [Glossary](Glossary.html#Cubemap) textures from different **Reflection Probes**A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html) See in [Glossary](Glossary.html#ReflectionProbe), as a reflective GameObject passes between them. |
| [Optimize lighting](lighting-optimize-builtin.html) | Avoid Unity using multiple render passes to render GameObjects, or doing too much work to render lighting. |
| [Troubleshooting emissive materials not rendering](ts-emissive-mats-not-rendering.html) | Fix issues causing emissive materials to not render as brightly as intended. |
| [Light component Inspector window reference](class-Light.html) | Explore the properties and settings in the Light component **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html) See in [Glossary](Glossary.html#Inspector) window to customize settings specific to the Built-In Render Pipeline. |

Light component Inspector window reference for URP

Per-pixel and per-vertex lights in the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)