* [Materials and shaders](materials-and-shaders.html)
* [Custom shaders](Shaders.html)
* [Writing custom shaders](writing-custom-shaders.html)
* [Compute shaders](class-ComputeShader.html)
* Run a compute shader

Use HLSL and ShaderLab in a compute shader

Writing compute shaders for multiple platforms

# Run a compute shader

In your script, define a variable of ComputeShader type and assign a reference to the Asset. This allows you to invoke them with [ComputeShader.Dispatch](../ScriptReference/ComputeShader.Dispatch.html) function. See Unity documentation on [ComputeShader class](../ScriptReference/ComputeShader.html) for more details.

Closely related to compute **shaders**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) is a [ComputeBuffer](../ScriptReference/ComputeBuffer.html) class, which defines arbitrary data buffer (“structured buffer” in DX11 lingo). [Render Textures](../ScriptReference/RenderTexture.html)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](class-RenderTexture.html)  
See in [Glossary](Glossary.html#RenderTexture) can also be written into from compute shaders, if they have “random access” flag set (“unordered access view” in DX11). See [RenderTexture.enableRandomWrite](../ScriptReference/RenderTexture-enableRandomWrite.html) to learn more about this.

Use HLSL and ShaderLab in a compute shader

Writing compute shaders for multiple platforms

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)