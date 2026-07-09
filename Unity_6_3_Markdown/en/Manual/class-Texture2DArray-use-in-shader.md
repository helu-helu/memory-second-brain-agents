* [Materials and shaders](materials-and-shaders.html)
* [Custom textures](Textures-landing.html)
* [2D texture arrays](class-Texture2DArray.html)
* Sample a 2D texture array in a shader

Render to a 2D texture array

Cubemaps

# Sample a 2D texture array in a shader

To sample a texture array in a custom **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader), follow these steps:

1. To create a texture array material property, add a `2DArray` material property declaration. For example:

   ```
   Properties
   {
       _MainTex ("Texture array", 2DArray) = "" {}
   }
   ```
2. To set the texture array as a shader input, add a `UNITY_DECLARE_TEX2DARRAY` macro. For example:

   ```
   UNITY_DECLARE_TEX2DARRAY(_MainTex);
   ```
3. To sample a slice of the texture array, use the `UNITY_SAMPLE_TEX2DARRAY` method. For example to sample slice 1 of the texture array:

   ```
   half4 frag (v2f i) : SV_Target {
       float4 color = UNITY_SAMPLE_TEX2DARRAY(_MainTex, float3(0, 0, 1));
   }
   ```
4. To sample a mipmap level of a slice of the texture array, use the `UNITY_SAMPLE_TEX2DARRAY_LOD` method. For example to sample slice 1 of the texture array at mipmap level 0:

   ```
   half4 frag (v2f i) : SV_Target {
       float4 color = UNITY_SAMPLE_TEX2DARRAY_LOD(_MainTex, float3(0, 0, 1), 0);
   }
   ```

## Target platforms that support 2D texture arrays

To target custom shaders only at platforms that support texture arrays, use either of the following:

* `#pragma target 3.5` to target shader model 3.5 and higher.
* `#pragma require 2darray` to target GPUs that support texture arrays.

## Example

The following shader example samples a texture array using object space vertex positions as coordinates, and runs only on GPUs that support texture arrays.

```
Shader "Example/Sample2DArrayTexture"
{
    Properties
    {
        // Create material properties for the 2D texture array and the slices to sample 
        _MyArr ("Tex", 2DArray) = "" {}
        _SliceRange ("Slices", Range(0,16)) = 6

        _UVScale ("UVScale", Float) = 1.0
    }
    SubShader
    {
        Pass
        {
            HLSLPROGRAM

            #pragma vertex vert
            #pragma fragment frag

            // Compile the shader only on platforms that support texture arrays
            #pragma require 2darray

            #include "UnityCG.cginc"

            struct v2f
            {
                float3 uv : TEXCOORD0;
                float4 vertex : SV_POSITION;
            };

            float _SliceRange;
            float _UVScale;

            v2f vert (float4 vertex : POSITION)
            {
                v2f o;
                o.vertex = mul(UNITY_MATRIX_MVP, vertex);
                o.uv.xy = (vertex.xy + 0.5) * _UVScale;

                // Set the z coordinate to the slice indices
                o.uv.z = (vertex.z + 0.5) * _SliceRange;

                return o;
            }
            
            // Set the texture array as a shader input
            UNITY_DECLARE_TEX2DARRAY(_MyArr);

            half4 frag (v2f i) : SV_Target
            {
                // Sample the texture array
                return UNITY_SAMPLE_TEX2DARRAY(_MyArr, i.uv);
            }

            ENDHLSL
        }
    }
}
```

## Additional resources

* [Texture samplers](SL-SamplerStates.html)
* [Set a shader to require a shader model or GPU feature](SL-ShaderCompileTargets.html)

Render to a 2D texture array

Cubemaps

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)