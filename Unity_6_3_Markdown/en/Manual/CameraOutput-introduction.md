* [Cameras](Cameras.html)
* [Camera output](CameraOutput.html)
* Introduction to camera output

Camera output

Output a depth texture from a camera

# Introduction to camera output

A [Camera](Cameras.html)A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](CamerasOverview.html)  
See in [Glossary](Glossary.html#Camera) can generate a depth, depth+normals, or motion vector texture. This is a minimalistic G-buffer texture that can be used for **post-processing**A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](Glossary.html#post-processing) effects or to implement custom lighting models.

These are mostly used by effects; for example, [post-processing effects](PostProcessingOverview.html) often use depth information.

Pixel values in the depth texture range between 0 and 1, with a non-linear distribution. Precision is usually 32 or 16 bits, depending on configuration and platform used. When reading from the Depth Texture, a high precision value in a range between 0 and 1 is returned. If you need to get distance from the Camera, or an otherwise linear 0–1 value, compute that manually using [helper macros](SL-BuiltinFunctions.html).

Depth Textures are supported on most modern hardware and graphics APIs. Special requirements are listed below:

* Direct3D 11+ (Windows), OpenGL 3+ (Mac/Linux), Metal (iOS), and popular consoles support depth textures.

The Camera’s depth Texture mode can be enabled using [Camera.depthTextureMode](../ScriptReference/Camera-depthTextureMode.html) variable from script. It is also possible to build similar textures yourself, using [Shader Replacement](SL-ShaderReplacement.html) feature.

There are three possible depth texture modes:

* **DepthTextureMode.Depth**: a depth texture.
* **DepthTextureMode.DepthNormals**: depth and view space normals packed into one texture.
* **DepthTextureMode.MotionVectors**: per-pixel screen space motion of each screen texel for the current frame. Packed into a RG16 texture.

These are flags, so it is possible to specify any combination of the above textures.

## Under the hood

Depth textures can come directly from the actual **depth buffer**A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#depthbuffer), or be rendered in a separate pass, depending on the **rendering path**The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](RenderingPaths.html)  
See in [Glossary](Glossary.html#renderingpath) used and the hardware. Typically when using the **Deferred Shading**A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](RenderTech-DeferredShading.html)  
See in [Glossary](Glossary.html#deferredshading) rendering path in the Built-In **Render Pipeline**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline), the depth textures come “for free” since they are a product of the G-buffer rendering anyway.

When enabled, the MotionVectors texture always comes from a extra render pass. Unity will render moving **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) into this buffer, and construct their motion from the last frame to the current frame.

Camera output

Output a depth texture from a camera

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)