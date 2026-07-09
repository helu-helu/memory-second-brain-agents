* [Assets and media](assets-and-media.html)
* [Managing assets at runtime](assets-managing-runtime.html)
* [Use the Resources system to load assets at runtime](assets-resources-system.html)
* Load and unload assets with the Resources system

Introduction to the Resources system

Use AssetBundles to load assets at runtime

# Load and unload assets with the Resources system

To load assets with the Resources system:

1. Create a new folder called `Resources` in your project, and add assets to it. Unity then makes these assets available even if they’re not directly referenced in a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
   See in [Glossary](Glossary.html#Scene). **Note:** You can have multiple `Resources` folders located in different subfolders within your `Assets` folder, and packages can also contain `Resources` folders.
2. Whenever you want to load an asset from one of these folders, call [`Resources.Load`](../ScriptReference/Resources.Load.html) in your code. Only assets in the `Resources` folder can be accessed in this way.

For example, you can apply the following script to load and apply a texture to it:

```
using UnityEngine;

public class LoadTexture : MonoBehaviour
{
    // Reference a material to apply the texture to
    public Renderer targetRenderer;

    void Start()
    {
        // Load a texture from the Textures folder inside the Resources folder
        Texture2D loadedTexture = Resources.Load<Texture2D>("Textures/MyTexture");

        if (loadedTexture != null)
        {
            // Apply the loaded texture to the material of the target renderer
            targetRenderer.material.mainTexture = loadedTexture;

            Debug.Log("Texture successfully loaded and applied.");
        }
        else
        {
            Debug.LogError("Failed to load texture from Resources.");
        }
    }
}
```

Unity stores all assets in the `Resources` folders and their dependencies in a file in the build output called `resources.assets`. If a scene in the build references an asset, Unity serializes that asset into a `sharedAssets*.assets` file instead.

Additional assets might end up in the `resources.assets` file if they’re dependencies. For example, a material in the `Resources` folder might reference a texture outside of the `Resources` folder. In that case the texture is also included in the `resources.assets` file, but isn’t available to load directly.

## Unload assets

If you want to destroy objects that [`Resources.Load`](../ScriptReference/Resources.Load.html) loaded before loading another scene, call [`Object.Destroy`](../ScriptReference/Object.Destroy.html) on them. To recover memory used by unreferenced objects, use [`Resources.UnloadUnusedAssets`](../ScriptReference/Resources.UnloadUnusedAssets.html).

## Additional resources

* [Introduction to the Resources system](LoadingResourcesatRuntime.html)
* [Introduction to asset management](assets-managing-introduction.html)
* [`Resources.Load` API](../ScriptReference/Resources.Load.html)

Introduction to the Resources system

Use AssetBundles to load assets at runtime

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)