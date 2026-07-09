* [Materials and shaders](materials-and-shaders.html)
* [Custom shaders](Shaders.html)
* [Troubleshooting shaders](shader-troubleshooting.html)
* [Fixing hitches or stalls](shader-reduce-stalling.html)
* [Asynchronous shader compilation in the Editor](AsynchronousShaderCompilation.html)
* Troubleshooting asynchronous shader compilation

Detect asynchronous shader compilation

Reducing the size or number of shaders

# Troubleshooting asynchronous shader compilation

Advanced rendering solutions rely on generating data once and reusing it in later frames. If the Editor uses a placeholder **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) during this process, it might pollute the generated data. If this happens, you can see the cyan color or other rendering artifacts in your **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), even after the shader variants have finished compiling.

To avoid this, you can [Disable asynchronous shader compilation](AsynchronousShaderCompilation-enable-or-disable.html).

## Customize compile time rendering

You can make your custom tools draw something other than the placeholder shader for each material. This way, you can avoid rendering in plain cyan, and instead draw something else while the shader variant compiles.

To check if a specific shader variant has compiled, see [Detecting asynchronous shader compilation](AsynchronousShaderCompilation-detect.html).

To trigger compilation manually, you can use [`ShaderUtil.CompilePass`](../ScriptReference/ShaderUtil.CompilePass.html). This way, you can avoid rendering with the cyan placeholder, and draw something else while the shader variant compiles.

Detect asynchronous shader compilation

Reducing the size or number of shaders

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)