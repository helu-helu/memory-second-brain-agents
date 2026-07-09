* [Lighting](LightingOverview.html)
* [Direct and indirect lighting](direct-and-indirect-lighting.html)
* [Precalculating surface lighting with lightmaps](Lightmapping-landing.html)
* Global illumination

Precalculating surface lighting with lightmaps

Baking lightmaps before runtime

# Global illumination

Global illumination is a group of techniques that model both direct and indirect lighting to provide realistic lighting results.

Unity has the following **global illumination**A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](Glossary.html#globalillumination) systems:

* Baked Global Illumination
* **Enlighten**A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
  See in [Glossary](Glossary.html#Enlighten) Realtime Global Illumination

With both systems, you need to make sure you set up texture UVs correctly, and control **Light Probe**Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) placement to avoid increasing baking time.

If you’re experimenting with lighting, you can disable both global illumination systems so lighting updates more quickly. To compensate for the lack of indirect lighting, enable [screen space ambient occlusion (SSAO)](urp/post-processing-ssao.html).

For more information about support for global illumination across **render pipelines**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline), refer to [render pipeline feature comparison reference](render-pipelines-feature-comparison.html).

## Baked Global Illumination

Unity uses a CPU or GPU **lightmapper**A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmapper) to store lighting data in your build, in Light Probes, **Reflection Probes**A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe), and textures called **lightmaps**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap).

Lighting quality is usually better than Enlighten Realtime Global Illumination.

For more information, refer to [Baking lightmaps before runtime](Lightmapping-baking-before-runtime.html).

## Enlighten Realtime Global Illumination

Unity stores some lighting data in your build, but uses the data to create lightmaps at runtime. As a result, you can adjust lights and see the effects on indirect lighting in real-time, in the Editor or at runtime.

Enlighten Realtime Global Illumination doesn’t support global illumination from realtime shadows.

For more information, refer to [Update lightmaps at runtime with Enlighten Realtime Global Illumination](realtime-gi-using-enlighten-landing.html).

## Using both systems together

The Unity Editor and Player allow you to use both Enlighten Realtime Global Illumination and baked lighting at the same time.

However, simultaneously enabling these features greatly increases baking time and memory usage at runtime, because they do not use the same data sets. You can expect visual differences between indirect light you have baked and indirect light provided by Enlighten Realtime Global Illumination, regardless of the lightmapper you use for baking. This is because Enlighten Realtime Global Illumination often operates at a significantly different resolution than Unity’s baking backends, and relies on different techniques to simulate indirect lighting.

If you wish to use both Enlighten Realtime Global Illumination and baked lighting at the same time, limit your simultaneous use of both global illumination systems to high-end platforms and/or to projects that have tightly controlled **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) with predictable costs. Only expert users who have a very good understanding of all lighting settings can effectively use this approach. Consequently, picking one of the two global illumination systems is usually a safer strategy for most projects. Using both systems is rarely recommended.

## Additional resources

* [Choose a render pipeline](choose-a-render-pipeline.html)
* [Choose a Light Mode](LightModes-choose.html)
* [Lighting Mode](lighting-mode.html)
* [Lighting in URP](urp/lighting-landing.html)
* [Lighting in the Built-In Render Pipeline](lighting-birp.html)
* [Manage your templates](https://docs.unity.com/hub/project-create#template-categories.html)
* [Creating Believable Visuals tutorial (Built-In Render Pipeline)](https://unity3d.com/learn/tutorials/s/creating-believable-visuals)

Precalculating surface lighting with lightmaps

Baking lightmaps before runtime

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)