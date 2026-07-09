* [Cameras](Cameras.html)
* [Changing resolution scale](resolution-scale.html)
* [Dynamic Resolution](DynamicResolution-landing.html)
* Enable or disable Dynamic Resolution for render targets

Control when Dynamic Scaling happens

Excluding hidden objects with occlusion culling

# Enable or disable Dynamic Resolution for render targets

With **dynamic resolution**A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](DynamicResolution-landing.html)  
See in [Glossary](Glossary.html#dynamicresolution), render targets have the [DynamicallyScalable](../ScriptReference/RenderTextureCreationFlags.DynamicallyScalable.html) flag. You can set this to state whether Unity should scale this **render texture**A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture) as part of the dynamic resolution process or not. **Cameras**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) also have the [allowDynamicResolution](../ScriptReference/Camera-allowDynamicResolution.html) flag, which you can use to set up dynamic resolution so that there is no need to override the render target if you just want to apply dynamic resolution to a less complex **Scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

## MRT buffers

When you enable **Allow Dynamic Resolution** on the Camera, Unity scales all of that Camera’s targets.

Control when Dynamic Scaling happens

Excluding hidden objects with occlusion culling

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)