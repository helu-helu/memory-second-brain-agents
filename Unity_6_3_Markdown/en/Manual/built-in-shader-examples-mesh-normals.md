* [Materials and shaders](materials-and-shaders.html)
* [Custom shaders](Shaders.html)
* [Writing custom shaders in the Built-In Render Pipeline](writing-shaders-birp.html)
* [HLSL shader examples in the Built-in Render Pipeline](built-in-shader-examples.html)
* Mesh normals shader example in the Built-In Render Pipeline

Simple unlit shader example in the Built-In Render Pipeline

Reflections shader example in the Built-In Render Pipeline

# Mesh normals shader example in the Built-In Render Pipeline

![A cat-like character rendered with different colors that represent the direction each surface faces.](../uploads/SL/ExampleWorldSpaceNormals.png)


A cat-like character rendered with different colors that represent the direction each surface faces.

```
Shader "Unlit/WorldSpaceNormals"
{
    // no Properties block this time!
    SubShader
    {
        Pass
        {
            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            // include file that contains UnityObjectToWorldNormal helper function
            #include "UnityCG.cginc"

            struct v2f {
                // we'll output world space normal as one of regular ("texcoord") interpolators
                half3 worldNormal : TEXCOORD0;
                float4 pos : SV_POSITION;
            };

            // vertex shader: takes object space normal as input too
            v2f vert (float4 vertex : POSITION, float3 normal : NORMAL)
            {
                v2f o;
                o.pos = UnityObjectToClipPos(vertex);
                // UnityCG.cginc file contains function to transform
                // normal from object to world space, use that
                o.worldNormal = UnityObjectToWorldNormal(normal);
                return o;
            }
            
            fixed4 frag (v2f i) : SV_Target
            {
                fixed4 c = 0;
                // normal is a 3D vector with xyz components; in -1..1
                // range. To display it as color, bring the range into 0..1
                // and put into red, green, blue components
                c.rgb = i.worldNormal*0.5+0.5;
                return c;
            }
            ENDHLSL
        }
    }
}
```

Besides resulting in pretty colors, normals are used for all sorts of graphics effects – lighting, reflections, silhouettes and so on.

In the **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) above, we started using one of Unity’s built-in [shader include files](SL-BuiltinIncludes.html).
Here, **UnityCG.cginc** was used which contains a handy function **UnityObjectToWorldNormal**. We have also used the utility function **UnityObjectToClipPos**, which transforms the vertex from object space to the screen. This just makes the code easier to read and is more efficient under certain circumstances.

We’ve seen that data can be passed from the vertex into fragment shader in so-called “interpolators” (or sometimes called “varyings”). In HLSL shading language they are typically labeled with **TEXCOORDn** semantic, and each of them can be up to a 4-component vector (see [Input vertex data into a shader](SL-VertexProgramInputs.html) page for details).

Also we’ve learned a simple technique in how to visualize normalized vectors (in –1.0 to +1.0 range) as colors: just multiply them by half and add half. For more vertex data visualization examples, see [Visualizaing vertex data](built-in-shader-examples-vertex-data.html).

Simple unlit shader example in the Built-In Render Pipeline

Reflections shader example in the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)