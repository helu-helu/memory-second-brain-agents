* [Optimization](analysis.html)
* [Graphics performance and profiling](graphics-performance-profiling.html)
* [Optimize rendering lots of objects](reduce-draw-calls-landing.html)
* [GPU instancing](GPUInstancing-landing.html)
* Troubleshooting GPU instancing

Enable GPU instancing for a prebuilt material

Combine meshes using batching

# Troubleshooting GPU instancing

Meshes that have a low number of vertices can’t be processed efficiently using GPU instancing because the GPU can’t distribute the work in a way that fully uses the GPU’s resources. This processing inefficiency can have a detrimental effect on performance. The threshold at which inefficiencies begin depends on the GPU, but as a general rule, don’t use GPU instancing for meshes that have fewer than 256 vertices.

If you want to render a **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) with a low number of vertices many times, best practice is to create a single buffer that contains all the mesh information and use that to draw the meshes.

## Additional resources

* [Make materials incompatible with the SRP Batcher in URP](SRPBatcher-Incompatible.html)

Enable GPU instancing for a prebuilt material

Combine meshes using batching

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)