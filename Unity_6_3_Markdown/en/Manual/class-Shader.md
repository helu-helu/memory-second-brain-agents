* [Materials and shaders](materials-and-shaders.html)
* [Custom shaders](Shaders.html)
* [Writing custom shaders](writing-custom-shaders.html)
* [Writing shaders in code](shader-writing.html)
* [Writing a custom shader in ShaderLab and HLSL](SL-landing.html)
* Create a shader file

Writing a custom shader in ShaderLab and HLSL

Add a subshader in a custom shader

# Create a shader file

[Switch to Scripting](../ScriptReference/Shader.html "Go to Shader page in the Scripting Reference")

A shader asset is an asset in your Unity project that defines a [Shader object](shader-objects.html)An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](shader-objects.html)  
See in [Glossary](Glossary.html#Shaderobject). It’s a text file with a `.shader` extension. It contains [shader code](shader-writing.html).

1. Select **Assets**Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](AssetWorkflow.html)  
   See in [Glossary](Glossary.html#asset) > **Create** > **Shader**A program that runs on the GPU. [More info](Shaders.html)  
   See in [Glossary](Glossary.html#shader) from the main menu.
2. Create a shader.

You can create the following types of shaders:

| Shader type | Description |
| --- | --- |
| [Standard Surface Shader](SL-SurfaceShaders.html) | A shader that lets you write streamlined shader code that interacts with lighting. |
| Unlit Shader | A basic shader that displays a texture without any lighting. |
| Image Effect Shader | A shader file associated with a C# script that creates an [image effect](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest). |
| [Compute Shader](class-ComputeShader.html) | A shader that performs calculations on the GPU, outside of the regular graphics pipeline. |
| **Ray Tracing**The process of generating an image by tracing out rays from the Camera through each pixel and recording the color contribution at the hit point. This is an alternative to rasterization. raytracing See in [Glossary](Glossary.html#raytracing) Shader | A shader that performs calculations related to ray tracing. |

Unity populates a new `.shader` file in your `Assets` folder with basic code.

## Create a shader file manually

To define a Shader object in **ShaderLab**Unity’s language for defining the structure of Shader objects. [More info](SL-Shader.html)  
See in [Glossary](Glossary.html#ShaderLab), use a `Shader` block. This page contains information on using `Shader` blocks.

For information on how a Shader object works, and the relationship between Shader objects, SubShaders and Passes, see [Shader objects introduction](shader-objects.html).

This example code demonstrates the basic syntax and structure of a Shader object. The example Shader object has a single SubShader that contains a single pass. It defines Material properties, a CustomEditor, and a Fallback.

```
Shader "Examples/ShaderSyntax"
{
    CustomEditor = "ExampleCustomEditor"

    Properties
    {
        // Material property declarations go here
    }
    SubShader
    {
        // The code that defines the rest of the SubShader goes here

        Pass
        {
           // The code that defines the Pass goes here
        }
    }

    Fallback "ExampleFallbackShader"
}
```

For example custom shaders that are compatible with different **render pipelines**A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](render-pipelines.html)  
See in [Glossary](Glossary.html#renderpipeline), see [Example custom shaders](built-in-shader-examples.html)

## Legacy shader names

Prior to Unity 5.0, some of the functionality of a shader was determined by its path and name. This is still how [Unity’s Legacy Shaders](Built-inShaderGuide.html) work. Changing the name of these shaders can affect their functionality.

## Disable Auto-Upgrade

`UNITY_SHADER_NO_UPGRADE` allows you to disable Unity from automatically upgrading or modifying your shader file.

Unity regularly upgrades shaders to maintain compatibility with changes in syntax, APIs, or rendering pipelines.

## Additional resources

* [ShaderLab language reference](SL-Reference.html)
* [Shader block reference in ShaderLab](SL-Shader.html)
* [Fallback block in ShaderLab reference](SL-Fallback.html)
* [Create and assign a material](create-material.html)

Writing a custom shader in ShaderLab and HLSL

Add a subshader in a custom shader

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)