* [Materials and shaders](materials-and-shaders.html)
* [Custom shaders](Shaders.html)
* [Troubleshooting shaders](shader-troubleshooting.html)
* [Reducing the size or number of shaders](shader-reducing.html)
* Reduce shader duplication in AssetBundles

Default shader keywords

Control how much memory shaders use

# Reduce shader duplication in AssetBundles

If you use [AssetBundles](AssetBundlesIntro.html), Unity might compile duplicate shaders. For example, if materials in two AssetBundles reference the same **shader**A program that runs on the GPU. [More info](Shaders.html)  
See in [Glossary](Glossary.html#shader), Unity might include a copy of the compiled shader in each AssetBundle. This can increase the memory and storage space your project uses, and break [draw call batching](DrawCallBatching.html).

To avoid duplicate shaders, add your shaders to an AssetBundle, and at runtime make sure you load the shaders AssetBundle first.

Use one of the following approaches:

* Add all your shaders to a single AssetBundle. This is the simplest approach, but it might use more memory at runtime.
* Create a separate AssetBundle for the shaders from each **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
  See in [Glossary](Glossary.html#Scene) or environment type.

## Add all your shaders to a single AssetBundle

Follow these steps:

1. Create a file that contains a list of the shader variants your built application uses.

   If you target DirectX 12, Vulkan, Metal, or WebGPU, create a `.graphicsState` file. For more information, refer to [Trace and manage PSO data collections](shader-pso-trace.html).

   Otherwise, create a `.shaderVariants` file. Refer to [create a shader variant collection](shader-variant-collections.html).

   The list of shader variants provides the build pipeline with the information it needs to compile the shader variants your application uses. Otherwise, the build pipeline might strip shader variants you need, and materials might render using the bright pink [error shader](shader-error.html) at runtime.
2. Assign the generated `.graphicsState` file or `.shadervariants` file to an AssetBundle.
3. Assign all your `.shader` assets to the same AssetBundle.
4. Assign your materials to either the shaders AssetBundle or other AssetBundles. In other AssetBundles, Unity detects the referenced `.shader` assets in the first AssetBundle, and doesn’t include duplicate shaders.
5. Build your project. At build time, Unity uses the information from the `.graphicsState` file or `.shadervariants` file to make sure it compiles all the shader variants your application uses.
6. At runtime, load and instantiate the AssetBundle containing the shaders first. Then load and instantiate the AssetBundles that contain materials.

For information on avoiding Unity including duplicate shaders from both your AssetBundles and your scenes, refer to [Avoiding asset duplication](assets-avoid-duplication.html).

## Create a separate AssetBundle for each scene or environment type

Depending on how many shaders you have, putting all your shaders into a single AssetBundle might use a lot of memory at runtime. Shaders might also stay in memory when they’re no longer needed, because you can’t partially unload an AssetBundle.

To avoid this, create a separate AssetBundle for each group of shaders you use together. For example, an AssetBundle for each scene or each environment type.

For example:

1. Create a file that contains the list of shader variants for one scene or environment.
2. Assign the generated `.graphicsState` file or `.shadervariants` file to an AssetBundle.
3. Assign only the relevant `.shader` assets to the same AssetBundle.
4. Assign your scene materials to either the same AssetBundle or another AssetBundle.
5. Repeat steps 1 to 4 for each scene or environment type, using a different AssetBundle for each.
6. When you load a scene at runtime, load and instantiate the AssetBundle containing its shaders first. Then load and instantiate the AssetBundles that contain scene materials.

## Additional resources

* [AssetBundle dependencies](AssetBundles-Dependencies.html)
* [Avoiding asset duplication](assets-avoid-duplication.html)
* [Loading assets from AssetBundles](AssetBundles-Native.html)

Default shader keywords

Control how much memory shaders use

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)