* [Materials and shaders](materials-and-shaders.html)
* [Custom shaders](Shaders.html)
* [Troubleshooting shaders](shader-troubleshooting.html)
* [Fixing hitches or stalls](shader-reduce-stalling.html)
* [Asynchronous shader compilation in the Editor](AsynchronousShaderCompilation.html)
* Introduction to asynchronous shader compilation

Asynchronous shader compilation in the Editor

Enable or disable asynchronous shader compilation

# Introduction to asynchronous shader compilation

Shader objects can contain of hundreds or thousands of [shader variants](shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](shader-variants.html)  
See in [Glossary](Glossary.html#shadervariant). If the Editor compiled all variants when loading a **Shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) object, the import process would be very slow. Instead, the Editor compiles shader variants on-demand, the first time it encounters them.

Compiling these shader variants can cause the Editor to stall for milliseconds or even seconds, depending on the graphics API and the complexity of the **Shader object**An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject). To avoid these stalls, you can use asynchronous shader compilation to compile the shader variants in the background, and use placeholder Shader objects in the meantime.

## How asynchronous shader compilation works

Asynchronous shader compilation works like this:

1. When the Editor first encounters an uncompiled shader variant, it adds the shader variant to a compilation queue on a job thread. The progress bar in the bottom right corner of the Editor shows the status of the compilation queue.
2. While the shader variant is loading, Editor renders the geometry with a placeholder shader, which appears as a plain cyan color.
3. When the Editor has finished compiling the shader variant, it renders the geometry using the shader variant.

![Unity renders shader variants that are still compiling with a cyan dummy Shader until compilation has finished. The bottom right progress bar indicates the compilation queue progress.](../uploads/Main/cyan_dummy_shaders.png)


Unity renders shader variants that are still compiling with a cyan dummy Shader until compilation has finished. The bottom right progress bar indicates the compilation queue progress.

## Exceptions

The following exceptions apply:

* If you draw geometry using [`DrawProcedural`](../ScriptReference/Graphics.DrawProcedural.html) or [`CommandBuffer.DrawProcedural`](../ScriptReference/Rendering.CommandBuffer.DrawProcedural.html), the Editor doesn’t use a placeholder shader. Instead, the Editor just skips rendering this geometry until it has compiled the shader variant.
* The Unity Editor does not use asynchronous shader compilation with **Blit**A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
  See in [Glossary](Glossary.html#blit) operations. This is to guarantee correct output in the most common use cases.

Asynchronous shader compilation in the Editor

Enable or disable asynchronous shader compilation

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)