* [Materials and shaders](materials-and-shaders.html)
* [Color and High Dynamic Range (HDR)](graphics-color.html)
* [High dynamic range (HDR)](hdr-landing.html)
* [Color space and HDR in the Built-in Render Pipeline](hdr-birp-landing.html)
* HDR in the Built-in Render Pipeline

Color space and HDR in the Built-in Render Pipeline

HDR

# HDR in the Built-in Render Pipeline

Support for **HDR**high dynamic range  
See in [Glossary](Glossary.html#HDR) in the Built-In **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline) depends on the **rendering path**The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#renderingpath) in use.

## Forward Rendering

In the **Forward rendering**A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering) path, a **Camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) only supports HDR if you have a **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) effect on the Camera. This is due to performance considerations. If you have no post-processing effect on the Camera, the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) will be rendered directly to the back buffer where HDR is not supported.

## Deferred Shading

In the **Deferred Shading**A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](RenderTech-DeferredShading.html)  
See in [Glossary](Glossary.html#deferredshading) rendering path, when HDR is enabled for a Camera the lighting buffer is also allocated as a floating point buffer. This reduces banding in the lighting buffer.

Color space and HDR in the Built-in Render Pipeline

HDR

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)