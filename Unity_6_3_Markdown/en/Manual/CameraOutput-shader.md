* [Cameras](Cameras.html)
* [Camera output](CameraOutput.html)
* Sample output textures in a shader

Output a motion vector texture from a camera

Troubleshooting camera output

# Sample output textures in a shader

Depth textures are available for sampling in shaders as global **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) properties. By declaring a sampler called `_CameraDepthTexture` you will be able to sample the main depth texture for the **camera**A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera).

`_CameraDepthTexture` always refers to the camera’s primary depth
texture. By contrast, you can use `_LastCameraDepthTexture` to refer to the last depth texture rendered by any camera. This could be useful for example if you render a half-resolution depth texture in script using a secondary camera and want to make it available to a post-process shader.

In the Built-In **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline), the motion vectors texture (when enabled) is available in Shaders as a global Shader property. By declaring a sampler called ‘\_CameraMotionVectorsTexture’ you can sample the Texture for the currently rendering Camera. When sampling from this texture motion from the encoded **pixel**The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](ShadowPerformance.html)  
See in [Glossary](Glossary.html#pixel) is returned in a range of –1..1. This will be the UV offset from the last frame to the current frame.

## Additional resources

* [Sample motion vectors in a shader in URP](urp/features/motion-vectors-sample.html)

Output a motion vector texture from a camera

Troubleshooting camera output

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)