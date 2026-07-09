* [Materials and shaders](materials-and-shaders.html)
* [Custom textures](Textures-landing.html)
* [Cubemaps](class-Cubemap-landing.html)
* Sample a cubemap array in a shader

Create a cubemap array

Preview a cubemap array

# Sample a cubemap array in a shader

Here is an example of a **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) that uses a **cubemap**A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](class-Cubemap-landing.html)  
See in [Glossary](Glossary.html#Cubemap) array.

```
Shader "CubemapArrayShaderExample" {
Properties {
    _MainTex ("CubemapArray", CubeArray) = "" {}
    _Mip ("Mip", Float) = 0.0
    _Intensity ("Intensity", Float) = 1.0
    _SliceIndex ("Slice", Int) = 0
    _Exposure ("Exposure", Float) = 0.0
}

SubShader {
    Tags {"Queue"="Transparent" "IgnoreProjector"="True" "RenderType"="Transparent" "ForceSupported" = "True"}

    Pass {

        HLSLPROGRAM
        #pragma vertex vert
            #pragma fragment frag
            #pragma require sampleLOD
            #pragma require cubearray
            #include "UnityCG.cginc"
    
    
    
            struct appdata {
                float4 pos : POSITION;
                float3 nor : NORMAL;
            };
    
            struct v2f {
                float3 uv : TEXCOORD0;
                float4 pos : SV_POSITION;
            };
    
            uniform int _SliceIndex;
            float _Mip;
            half _Alpha;
            half _Intensity;
            float _Exposure;
    
           v2f vert (appdata v) {
                v2f o;
                o.pos = UnityObjectToClipPos(v.pos);
                float3 viewDir = -normalize(ObjSpaceViewDir(v.pos));
                o.uv = reflect(viewDir, v.nor);
                return o;
            }
    
            half4 _MainTex_HDR;
            UNITY_DECLARE_TEXCUBEARRAY(_MainTex);
            fixed4 frag (v2f i) : COLOR0
            {
                fixed4 c = UNITY_SAMPLE_TEXCUBEARRAY(_MainTex, float4(i.uv, _SliceIndex));
                fixed4 cmip = UNITY_SAMPLE_TEXCUBEARRAY_LOD(_MainTex, float4(i.uv, _SliceIndex), _Mip);
                if (_Mip >= 0.0)
                    c = cmip;
                c.rgb = DecodeHDR (c, _MainTex_HDR) * _Intensity;
                c.rgb *= exp2(_Exposure);
                c = lerp (c, c.aaaa, _Alpha);
                return c;
            }
            ENDHLSL
        }
    }
    Fallback Off
}
```

If you use this shader with the Cubemap Array created in the example on the [Create a cubemap array](class-CubemapArray-create.html) page, the result looks like this:

![A sphere with the rainbow color pattern the shader draws.](../uploads/Main/cubemap-array-shader-example.png)


A sphere with the rainbow color pattern the shader draws.

Create a cubemap array

Preview a cubemap array

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)