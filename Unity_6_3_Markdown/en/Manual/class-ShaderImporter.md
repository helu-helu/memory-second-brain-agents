* [Materials and shaders](materials-and-shaders.html)
* Shader Import Settings window reference

Troubleshooting Scriptable Render Passes with HDR Output in URP

Visual effects

# Shader Import Settings window reference

[Switch to Scripting](../ScriptReference/ShaderImporter.html "Go to ShaderImporter page in the Scripting Reference")

View and edit properties and settings for a [shader](materials-and-shaders.html)A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader).

## ShaderLab shader properties

The following properties are available only for [ShaderLab shaders](SL-landing.html).

| **Property** | **Description** |
| --- | --- |
| **Default Maps** | Displays the textures that appear as material properties. |
| **NonModifiable Maps** | Displays the textures that have the `[NonModifiableTextureData]` attribute in the shader. These textures don’t appear as material properties. |

## Shader graph properties

The following properties are available only for [shader graphs](shader-graph.html).

| **Property** | **Description** |
| --- | --- |
| **Open Shader Editor** | Opens the **Shader Graph** window so you can edit the shader graph. |
| **View Generated Shader** | Opens your text editor with the **ShaderLab**Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html) See in [Glossary](Glossary.html#ShaderLab) shader code that Shader Graph generates. |
| **Copy Shader** | Copies the ShaderLab shader code that Shader Graph generates to the clipboard. |

## Imported object

| **Property** | **Description** |
| --- | --- |
| **Surface Shader** | Opens your text editor with the shader Unity generates, if the shader is a [surface shader](writing-surface-shaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html) See in [Glossary](Glossary.html#SurfaceShader). |
| **Fixed Function** | Opens your text editor with the shader Unity generates, if the shader is a fixed function shader. |
| **Preprocess only** | Sets **Compile and show code** to generate only the preprocessed code, instead of the final code. For more information, refer to [Shader compilation](shader-compilation.html). |
| **Strip #line directives** | Removes `#line` statements that display how the preprocessed code maps to the original ShaderLab and HLSL code. This property is available only if you enable **Preprocess only**. |
| **Compiled code** | Select **Compile and show code** to open your text editor with the shader code Unity compiles. Use the dropdown to select which graphics APIs and platforms Unity compiles the code for. For more information, refer to [Compiled code dropdown](#compiled-code-dropdown).  This property is only available for code shaders. For shader graphs, select **View Generated Shader**. |
| **Cast shadows** | Displays whether geometry casts shadows when it uses this shader. |
| **Render queue** | Displays which render queue Unity uses for geometry that uses this shader. For more information, refer to [Set the render pipeline and render order for a shader](writing-shader-tags-introduction.html). |
| ****LOD**The *Level Of Detail* (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](LevelOfDetail.html) See in [Glossary](Glossary.html#LOD)** | Displays the shader LOD value of the shader, which Unity uses to prioritize shaders. For more information, refer to [Optimize shaders](SL-ShaderPerformance.html). |
| **Ignore projector** | Displays whether geometry that uses this shader receives effects from projector components. |
| **Disable batching** | Displays whether the shader prevents Unity from applying **dynamic batching**An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](DrawCallBatching.html) See in [Glossary](Glossary.html#dynamicbatching) to geometry that uses the shader. For more information, refer to [Batch meshes at runtime](static-batching-enable.html). |
| **Keywords** | Displays the **Overridable** and **Not Overridable** keywords the shader defines. For more information, refer to [shader keywords](shader-keywords.html). |
| **SRP Batcher** | Displays whether the shader is compatible with the [Scriptable Render Pipeline (SRP) Batcher](SRPBatcher-landing.html). |
| **Properties** | Displays the properties in the `Properties` block of the shader code. For more information, refer to [Properties block reference in ShaderLab](SL-Properties.html). |

### Compiled code dropdown

For more information, refer to [Shader compilation](shader-compilation.html).

| **Property** | **Description** |
| --- | --- |
| **Current graphics device** | Compiles the shader code for the graphics device on your current machine. |
| **Current build platform** | Compiles the shader code for the current build platform. For more information, refer to [Build profiles](BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html) See in [Glossary](Glossary.html#buildprofile) |
| **All platforms** | Compiles the shader code for all platforms and graphics APIs. |
| **Custom** | Compiles the shader code for the graphics APIs you select. The options are:  * **D3D**: Compiles shader code into DirectX Bytecode (DXBC) for DirectX 11 or DirectX 12. * **GLES3x**: Compiles shader code into OpenGL Shading Language (GLSL). * **Metal**: Compiles shader code into Metal Shading Language (MSL). * **OpenGLCore**: Compiles shader code into OpenGL Shading Language (GLSL). * **Vulkan**: Compiles shader code into SPIR-V. * **WebGPU**: Compiles shader code into WebGPU Shading Language (WGSL). |
| **Skip unused shader\_features** | Strips shader variants that materials don’t use. For more information, refer to [Changing how shaders work via branching and keywords](SL-MultipleProgramVariants.html). |

The bottom of the **Compiled code** dropdown displays the number of shader variants Unity compiles. Select **Show** to open your text editor with a list of the shader variants.

## Additional resources

* [Introduction to shaders](shader-introduction.html)
* [Assets and media](assets-and-media.html)

Troubleshooting Scriptable Render Passes with HDR Output in URP

Visual effects

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)