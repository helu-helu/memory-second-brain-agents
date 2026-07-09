* [Materials and shaders](materials-and-shaders.html)
* [Custom shaders](Shaders.html)
* [Writing custom shaders](writing-custom-shaders.html)
* [Compute shaders](class-ComputeShader.html)
* Compute shader Import Settings window reference

Writing compute shaders for multiple platforms

Optimize custom shaders

# Compute shader Import Settings window reference

[Switch to Scripting](../ScriptReference/ComputeShaderImporter.html "Go to ComputeShaderImporter page in the Scripting Reference")

View the properties and compiled code of a [compute shader](class-ComputeShader.html).

## Imported object

| **Property** | **Description** |
| --- | --- |
| **Kernels** | Displays the names of the kernels the **shader**A program that runs on the GPU. [More info](Shaders.html) See in [Glossary](Glossary.html#shader) code defines, and which graphics APIs Unity compiles the kernels for. |
| **Preprocess only** | Sets **Show compiled code** to generate only the preprocessed code instead of the final code. For more information, refer to [Shader compilation](shader-compilation.html). |
| **Strip #line directives** | Removes `#line` statements that display how the preprocessed code maps to the original HLSL code. This property is available only if you enable **Preprocess only**. |
| **Show compiled code** | Opens your text editor with the shader code Unity compiles. |

## Additional resources

* [Create a compute shader](class-ComputeShader-create.html)
* [Shader Import Settings window reference](class-ShaderImporter.html)

Writing compute shaders for multiple platforms

Optimize custom shaders

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)