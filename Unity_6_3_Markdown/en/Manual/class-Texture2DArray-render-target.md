* [Materials and shaders](materials-and-shaders.html)
* [Custom textures](Textures-landing.html)
* [2D texture arrays](class-Texture2DArray.html)
* Render to a 2D texture array

Create a 2D texture array in a script

Sample a 2D texture array in a shader

# Render to a 2D texture array

To render to a 2D texture array, create a [render texture](render-texture-landing.html)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture) and set the **Dimension** property to **2D Array**.

If you use the [`Graphics.SetRenderTarget`](../ScriptReference/Graphics.SetRenderTarget.html) API, set the `depthSlice` parameter to the slice you want to render to.

If the platform supports geometry shaders, use a geometry **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) to render to individual slices, or set `depthSlice` to `-1` to render to all the slices.

Create a 2D texture array in a script

Sample a 2D texture array in a shader

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)