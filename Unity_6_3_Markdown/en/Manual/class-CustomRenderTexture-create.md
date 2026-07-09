* [Materials and shaders](materials-and-shaders.html)
* [Custom textures](Textures-landing.html)
* [Rendering to a texture](render-texture-landing.html)
* [Drawing to textures with shaders via Custom Render Textures](class-CustomRenderTexture-landing.html)
* Create a Custom Render Texture

Introduction to Custom Render Textures

Write a shader for a Custom Render Texture

# Create a Custom Render Texture

To assign a compatible material to a Custom **Render Texture**A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture) asset:

1. To create a Custom Render Texture, go to **Assets** > **Create** > **Rendering** > **Custom Render Texture**.
2. Assign a compatible Material to it in the **Material** property in the **Custom Render Texture** asset.

This Material updates the content of a texture according to its parameters.

## Chaining Custom Render Textures

You can chain Custom Render Textures together. To do this, use a Custom Render Texture as the input for a material that you have assigned to the **Material** or **Initialization Mode > Texture** in another Custom Render Texture.

You can use chained Custom Render Textures to generate a simulation with multiple steps.

Chained Custom Render Textures are dependent on each other. Unity calculates this dependency automatically so that each update happens in the right order. It does this by looking at the materials assigned to the **Material** and **Initialization Mode > Texture** properties in the **Custom Render Textures** inspector window.

Introduction to Custom Render Textures

Write a shader for a Custom Render Texture

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)