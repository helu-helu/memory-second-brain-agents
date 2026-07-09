* [Lighting](LightingOverview.html)
* Lighting configuration workflow

Introduction to lighting

Light sources

# Lighting configuration workflow

To set up lighting in Unity, follow these steps:

1. [Choose a render pipeline](#choose-a-render-pipeline)
2. [Configure lighting](#configure-lighting)
3. [Fine-tune your scene lighting](#fine-tune-your-scene-lighting)

## Choose a render pipeline

Unity provides **render pipelines**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline) that differ in customization and lighting features:

* [Built-in Render Pipeline](lighting-birp.html) (not scriptable)
* [Universal Render Pipeline (URP)](urp/lighting/lighting-in-urp.html)
* [High-Definition Render Pipeline (HDRP)](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@latest?subfolder=/manual/Light-Component.html)
* Custom Scriptable Render Pipeline (SRP)

For more information on render pipeline selection, refer to [choose a render pipeline](choose-a-render-pipeline.html).

## Configure lighting

1. Choose baked GI, realtime GI, mixed baked and realtime GI, or opt for no GI.

   For more information, refer to [Lighting Settings Asset Inspector window reference](class-LightingSettings.html#MixedLighting)
2. Choose one of the following Lighting Modes:

   * Baked Indirect
   * Subtractive
   * Shadowmask
   * Distance Shadowmask

   For more information, refer to [Lighting Mode](lighting-mode.html).

## Fine-tune your scene lighting

To fine-tune your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) lighting, follow these tasks based on project requirements:

1. Add [baked, realtime, or mixed lights](LightModes-introduction.html).
2. Optionally configure emissive surfaces with [Baked GI or Realtime GI](class-LightmapParameters.html).
3. Add baked, realtime, or custom [Reflection Probes](ReflectionProbes.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
   See in [Glossary](Glossary.html#ReflectionProbe).
4. If a GI mode is set, add [Light Probes](LightProbes-landing.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
   See in [Glossary](Glossary.html#LightProbe). You can also add [Light Probe Proxy Volumes (LPPVs)](LightProbeProxyVolume-landing.html).

## Additional resources

* [Add light emission to a material](StandardShaderMaterialParameterEmission.html)
* [Reflection Probe Inspector window reference](class-ReflectionProbe.html)
* [Light Probes](LightProbes.html)
* [SRP Core](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@latest)

Introduction to lighting

Light sources

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)