* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Graphics performance and profiling in the Built-In Render Pipeline](graphics-performance-birp.html)
* [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](gpu-instancing-shader.html)
* [Examples of GPU instancing shaders in the Built-In Render Pipeline](gpu-instancing-samples.html)
* Example of changing per-instance data at runtime in the Built-In Render Pipeline

Example of a shader that supports GPU Instancing in the Built-In Render Pipeline

Prevent Unity stripping GPU instancing shaders in the Built-In Render Pipeline

# Example of changing per-instance data at runtime in the Built-In Render Pipeline

The following example demonstrates how to use MaterialPropertyBlock objects to set per-instance data for a group of **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) at runtime. It sets the `_Color` property from the above **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader) examples to a random color.

**Important**: MaterialPropertyBlocks break SRP Batcher compatibility. For more information, see [GPU instancing: Requirements and Compatibility](GPUInstancing.html#requirements-and-compatibility).

```
using UnityEngine;

public class MaterialPropertyBlockExample : MonoBehaviour
{
    public GameObject[] objects;

    void Start()
    {
        MaterialPropertyBlock props = new MaterialPropertyBlock();
        MeshRenderer renderer;

        foreach (GameObject obj in objects)
        {
            float r = Random.Range(0.0f, 1.0f);
            float g = Random.Range(0.0f, 1.0f);
            float b = Random.Range(0.0f, 1.0f);
            props.SetColor("_Color", new Color(r, g, b));

            renderer = obj.GetComponent<MeshRenderer>();
            renderer.SetPropertyBlock(props);
        }
    }
}
```

Example of a shader that supports GPU Instancing in the Built-In Render Pipeline

Prevent Unity stripping GPU instancing shaders in the Built-In Render Pipeline

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)