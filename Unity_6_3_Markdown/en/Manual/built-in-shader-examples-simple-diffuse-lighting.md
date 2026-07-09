* [Materials and shaders](materials-and-shaders.html)
* [Custom shaders](Shaders.html)
* [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
* [HLSL shader examples in the Built-in Render Pipeline](built-in-shader-examples.html)
* Simple diffuse lighting shader example in the Built-In Render Pipeline

Tri-planar texturing shader example in the Built-In Render Pipeline

Ambient light shader example in the Built-In Render Pipeline

# Simple diffuse lighting shader example in the Built-In Render Pipeline

![A cat-like character lit using simple diffuse lighting, so surfaces facing away from the light are much darker.](../uploads/SL/ExampleDiffuseLighting.png)


A cat-like character lit using simple diffuse lighting, so surfaces facing away from the light are much darker.

The first thing we need to do is to indicate that our **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) does in fact need lighting information passed to it. Unity’s [rendering pipeline](SL-RenderPipeline.html) supports various ways of rendering; here we’ll be using the default [forward rendering](RenderTech-ForwardRendering.html)A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](RenderTech-ForwardRendering.html)  
See in [Glossary](Glossary.html#ForwardRendering) one.

We’ll start by only supporting one directional light. Forward rendering in Unity works by rendering the main directional light, ambient, **lightmaps**A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](Lightmapping.html)  
See in [Glossary](Glossary.html#Lightmap) and reflections in a single pass called **ForwardBase**. In the shader, this is indicated by adding a [pass tag](SL-PassTags.html): **Tags {“LightMode”=“ForwardBase”}**. This will make directional light data be passed into shader via some [built-in variables](SL-UnityShaderVariables.html).

Here’s the shader that computes simple diffuse lighting per vertex, and uses a single main texture:

```
Shader "Lit/Simple Diffuse"
{
    Properties
    {
        [NoScaleOffset] _MainTex ("Texture", 2D) = "white" {}
    }
    SubShader
    {
        Pass
        {
            // indicate that our pass is the "base" pass in forward
            // rendering pipeline. It gets ambient and main directional
            // light data set up; light direction in _WorldSpaceLightPos0
            // and color in _LightColor0
            Tags {"LightMode"="ForwardBase"}
        
            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc" // for UnityObjectToWorldNormal
            #include "UnityLightingCommon.cginc" // for _LightColor0

            struct v2f
            {
                float2 uv : TEXCOORD0;
                fixed4 diff : COLOR0; // diffuse lighting color
                float4 vertex : SV_POSITION;
            };

            v2f vert (appdata_base v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);
                o.uv = v.texcoord;
                // get vertex normal in world space
                half3 worldNormal = UnityObjectToWorldNormal(v.normal);
                // dot product between normal and light direction for
                // standard diffuse (Lambert) lighting
                half nl = max(0, dot(worldNormal, _WorldSpaceLightPos0.xyz));
                // factor in the light color
                o.diff = nl * _LightColor0;
                return o;
            }
            
            sampler2D _MainTex;

            fixed4 frag (v2f i) : SV_Target
            {
                // sample texture
                fixed4 col = tex2D(_MainTex, i.uv);
                // multiply by lighting
                col *= i.diff;
                return col;
            }
            ENDHLSL
        }
    }
}
```

This makes the object react to light direction - parts of it facing the light are illuminated, and parts facing away are not illuminated at all.

Tri-planar texturing shader example in the Built-In Render Pipeline

Ambient light shader example in the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)