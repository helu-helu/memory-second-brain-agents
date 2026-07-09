* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Graphics performance and profiling in URP](graphics-performance-and-profiling-in-urp.html)
* [Optimizing draw calls in URP](reduce-draw-calls-landing-urp.html)
* [BatchRendererGroup API in URP](batch-renderer-group.html)
* [Writing custom shaders for the BatchRendererGroup API](batch-renderer-group-writing-shaders.html)
* DOTS Instancing shader functions reference for URP

DOTS Instancing shader macros reference for URP

Enable GPU occlusion culling in URP

# DOTS Instancing shader functions reference for URP

Alongside the access macros, Unity provides **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) functions that load the values of constants directly from the draw command data. Shaders that Unity provides use these functions.

Unity provides the following shader functions:

| **Shader function** | **Description** |
| --- | --- |
| `LoadDOTSInstancedData_RenderingLayer` | Returns the [renderingLayerMask](../ScriptReference/Rendering.BatchFilterSettings-renderingLayerMask.html) for the draw command. |
| `LoadDOTSInstancedData_MotionVectorsParams` | Returns the [motion vector generation mode](../ScriptReference/Rendering.BatchFilterSettings-motionMode.html) for the draw command. This is formatted as a float4, which is what Unity shaders expect. |
| `LoadDOTSInstancedData_WorldTransformParams` | Returns whether to draw the instance with a flipped triangle winding. See [FlipWinding](../ScriptReference/Rendering.BatchDrawCommandFlags.FlipWinding.html). |
| `LoadDOTSInstancedData_LightData` | Returns whether the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html) See in [Glossary](Glossary.html#Scene)’s main Directional Light is active for the instance. The main light can be deactivated for multiple reasons, for example if the light already included in light maps. |
| `LoadDOTSInstancedData_LODFade` | Returns the 8 bit crossfade value you set if the [LODCrossFade flag](../ScriptReference/Rendering.BatchDrawCommandFlags.LODCrossFade.html) is set. If the flag is not set, the return value is undefined. |

DOTS Instancing shader macros reference for URP

Enable GPU occlusion culling in URP

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)