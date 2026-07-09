* [Materials and shaders](materials-and-shaders.html)
* [Prebuilt materials and shaders](built-in-materials-and-shaders.html)
* [Prebuilt shaders in the Built-In Render Pipeline](shader-built-in-birp.html)
* [Particle shaders in the Built-In Render Pipeline](shader-StandardParticleShadersLanding.html)
* [Particle System optimization in the Built-In Render Pipeline](particle-system-optimization.html)
* Example of Particle System GPU instancing in a Surface Shader

Apply GPU instancing for a Particle System in the Built-In Render Pipeline

Example of Particle System GPU instancing in the Built-In Render Pipeline

# Example of Particle System GPU instancing in a Surface Shader

Here is a complete working example of Surface **Shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) using **Particle**A small, simple image or mesh that is emitted by a particle system. A particle system can display and move particles in great numbers to represent a fluid or amorphous entity. The effect of all the particles together creates the impression of the complete entity, such as smoke. [More info](class-ParticleSystem.html)  
See in [Glossary](Glossary.html#particle) System GPU Instancing:

```
Shader "Instanced/ParticleMeshesSurface" {
    Properties {
        _Color ("Color", Color) = (1,1,1,1)
        _MainTex ("Albedo (RGB)", 2D) = "white" {}
        _Glossiness ("Smoothness", Range(0,1)) = 0.5
        _Metallic ("Metallic", Range(0,1)) = 0.0
    }
    SubShader {
        Tags { "RenderType"="Opaque" }
        LOD 200

        CGPROGRAM
        // Physically based Standard lighting model, and enable shadows on all light types
        // And generate the shadow pass with instancing support
        #pragma surface surf Standard nolightmap nometa noforwardadd keepalpha fullforwardshadows addshadow vertex:vert
        // Enable instancing for this shader
        #pragma multi_compile_instancing
        #pragma instancing_options procedural:vertInstancingSetup
        #pragma exclude_renderers gles
        #include "UnityStandardParticleInstancing.cginc"
        sampler2D _MainTex;
        struct Input {
            float2 uv_MainTex;
            fixed4 vertexColor;
        };
        fixed4 _Color;
        half _Glossiness;
        half _Metallic;
        void vert (inout appdata_full v, out Input o)
        {
            UNITY_INITIALIZE_OUTPUT(Input, o);
            vertInstancingColor(o.vertexColor);
            vertInstancingUVs(v.texcoord, o.uv_MainTex);
        }

        void surf (Input IN, inout SurfaceOutputStandard o) {
            // Albedo comes from a texture tinted by color
            fixed4 c = tex2D (_MainTex, IN.uv_MainTex) * IN.vertexColor * _Color;
            o.Albedo = c.rgb;
            // Metallic and smoothness come from slider variables
            o.Metallic = _Metallic;
            o.Smoothness = _Glossiness;
            o.Alpha = c.a;
        }
        ENDCG
    }
    FallBack "Diffuse"
}
```

There are a number of small differences to a regular [Surface Shader](SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader) in the above example, which make it work with particle instancing.

Firstly, you must add the following two lines to enable Procedural Instancing, and specify the built-in vertex setup function. This function lives in UnityStandardParticleInstancing.cginc, and loads the per-instance (per-particle) positional data:

```
        #pragma instancing_options procedural:vertInstancingSetup
        #include "UnityStandardParticleInstancing.cginc"
```

The other modification in the example is to the Vertex function, which has two extra lines that apply per-instance attributes, specifically, particle colors and [Texture Sheet Animation](PartSysTexSheetAnimModule.html) texture coordinates:

```
            vertInstancingColor(o.vertexColor);
            vertInstancingUVs(v.texcoord, o.uv_MainTex);
```

Apply GPU instancing for a Particle System in the Built-In Render Pipeline

Example of Particle System GPU instancing in the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)