* [Materials and shaders](materials-and-shaders.html)
* [Custom shaders](Shaders.html)
* [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
* [HLSL shader examples in the Built-in Render Pipeline](built-in-shader-examples.html)
* Reflections shader example in the Built-In Render Pipeline

Mesh normals shader example in the Built-In Render Pipeline

Normal map texturing shader example in the Built-In Render Pipeline

# Reflections shader example in the Built-In Render Pipeline

![A cat-like character with a metallic surface that reflects the scene.](../uploads/SL/ExampleSkyReflection.png)


A cat-like character with a metallic surface that reflects the scene.

When a [Skybox](sky-landing.html)A special type of Material used to represent skies. Usually six-sided. [More info](sky-landing.html)  
See in [Glossary](Glossary.html#Skybox) is used in the **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) as a reflection source (see [Lighting window](lighting-window.html)),
then essentially a “default” [Reflection Probe](class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](class-ReflectionProbe.html)  
See in [Glossary](Glossary.html#ReflectionProbe) is created, containing the skybox data.
A reflection probe is internally a [Cubemap](class-Cubemap-landing.html)A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) texture; we will extend the world-space normals **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) above to look into it.

The code is starting to get a bit involved by now. Of course, if you want shaders that automatically work with lights, shadows, reflections and the rest of the lighting system, it’s way easier to use [surface shaders](SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](SL-SurfaceShaders.html)  
See in [Glossary](Glossary.html#SurfaceShader). This example is intended to show you how to use parts of the lighting system in a “manual” way.

```
Shader "Unlit/SkyReflection"
{
    SubShader
    {
        Pass
        {
            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"

            struct v2f {
                half3 worldRefl : TEXCOORD0;
                float4 pos : SV_POSITION;
            };

            v2f vert (float4 vertex : POSITION, float3 normal : NORMAL)
            {
                v2f o;
                o.pos = UnityObjectToClipPos(vertex);
                // compute world space position of the vertex
                float3 worldPos = mul(_Object2World, vertex).xyz;
                // compute world space view direction
                float3 worldViewDir = normalize(UnityWorldSpaceViewDir(worldPos));
                // world space normal
                float3 worldNormal = UnityObjectToWorldNormal(normal);
                // world space reflection vector
                o.worldRefl = reflect(-worldViewDir, worldNormal);
                return o;
            }
        
            fixed4 frag (v2f i) : SV_Target
            {
                // sample the default reflection cubemap, using the reflection vector
                half4 skyData = UNITY_SAMPLE_TEXCUBE(unity_SpecCube0, i.worldRefl);
                // decode cubemap data into actual color
                half3 skyColor = DecodeHDR (skyData, unity_SpecCube0_HDR);
                // output it!
                fixed4 c = 0;
                c.rgb = skyColor;
                return c;
            }
            ENDHLSL
        }
    }
}
```

The example above uses several things from the built-in [shader include files](SL-BuiltinIncludes.html):

* **unity\_SpecCube0**, **unity\_SpecCube0\_HDR**, **Object2World**, **UNITY\_MATRIX\_MVP** from the
  [built-in shader variables](SL-UnityShaderVariables.html). **unity\_SpecCube0** contains data for the active reflection probe.
* **UNITY\_SAMPLE\_TEXCUBE** is a [built-in macro](SL-SamplerStates.html) to sample a cubemap. Most regular cubemaps are declared and
  used using standard HLSL syntax (**samplerCUBE** and **texCUBE**), however the reflection probe cubemaps in Unity are declared in a special way to save on sampler slots. If you don’t know what that is, don’t worry, just know that in order to use **unity\_SpecCube0** cubemap you have to use **UNITY\_SAMPLE\_TEXCUBE** macro.
* **UnityWorldSpaceViewDir** function from **UnityCG.cginc**, and **DecodeHDR** function from the same file. The latter is used to get actual color from the reflection probe data – since Unity stores reflection probe cubemap in specially encoded way.
* **reflect** is just a built-in HLSL function to compute vector reflection around a given normal.

Mesh normals shader example in the Built-In Render Pipeline

Normal map texturing shader example in the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)