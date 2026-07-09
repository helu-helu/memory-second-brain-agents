* [Lighting](LightingOverview.html)
* [Direct and indirect lighting](direct-and-indirect-lighting.html)
* [Precalculating indirect light with Light Probes](LightProbes-landing.html)
* Load Light Probes in multiple scenes

Set a GameObject to use light from Light Probes

Move Light Probes at runtime

# Load Light Probes in multiple scenes

Unity updates its **Light Probe**Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](LightProbes.html)  
See in [Glossary](Glossary.html#LightProbe) data differently depending on how you load or unload **Scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

Unity uses a [LightProbes](../ScriptReference/LightProbes.html) C# object to store Light Probe data for all currently loaded Scenes. The `LightProbes` object contains an internal data structure called a tetrahedral tessellation. Unity uses the tetrahedral tessellation in its calculations to determine how Light Probes light **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject).

When you load or unload a Scene, Unity automatically updates the `LightProbes` object to contain the positions and coefficients of all Light Probes in all currently loaded Scenes. However, whether Unity updates the tetrahedral tessellation depends on how you load or unload the Scene.

When you load a Scene with [LoadSceneMode.Single](../ScriptReference/SceneManagement.LoadSceneMode.html), Unity updates the tetrahedral tessellation automatically as part of the load process, because the new light probe data completely replaces the previous light probe data.

When you load a Scene with [LoadSceneMode.Additive](../ScriptReference/SceneManagement.LoadSceneMode.html), or unload a Scene with [UnloadSceneAsync](../ScriptReference/SceneManagement.SceneManager.UnloadSceneAsync.html), Unity does not automatically update the tetrahedral tessellation, because the new or removed light probe data needs to be recalculated - which is a computationally expensive operation, and there may be subsequent scenes to be loaded or unloaded after this operation.

Therefore Unity provides you with the [needsRetetrahedralization](../ScriptReference/LightProbes-needsRetetrahedralization.html) event to allow you to decide when to retetrahedralize the new light probe data. For example, if you are additively loading five new scenes, you would not want to retetrahedralize the data five times, once after each scene loads. Instead, you would only want to retetrahedralize the data after all five scenes have loaded and all the new light probe data is ready.

If Unity performs calculations using an out-of-date tetrahedral tessellation, the results do not take into account any newly loaded or unloaded Light Probes. This means that Light Probes might not light GameObjects as expected, and calls to [LightProbes.CalculateInterpolatedLightAndOcclusionProbes()](../ScriptReference/LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html) or [LightProbes.GetInterpolatedProbe()](../ScriptReference/LightProbes.GetInterpolatedProbe.html) might return unexpected results.

To force Unity to update the tetrahedral tessellation, you can call [LightProbes.Tetrahedralize](../ScriptReference/LightProbes.Tetrahedralize.html) or [LightProbes.TetrahedralizeAsync()](../ScriptReference/LightProbes.TetrahedralizeAsync.html). These functions cause Unity to update the tetrahedral tessellation with data from all Light Probes for all currently loaded Scenes.

Updating the tetrahedral tessellation is CPU-intensive, and the CPU impact increases with the number of Light Probes. If you are loading and unloading multiple Scenes, and you experience a performance impact from updating the tetrahedral tessellation, then it might be beneficial to delay the update until you have loaded or unloaded a certain amount of content, or until a time when the CPU impact is not likely to affect the performance of your application.

Set a GameObject to use light from Light Probes

Move Light Probes at runtime

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)