* [Assets and media](assets-and-media.html)
* [Managing assets at runtime](assets-managing-runtime.html)
* [Use AssetBundles to load assets at runtime](assetbundles-section.html)
* [Creating AssetBundles](assetbundles-creating.html)
* Assign assets to an AssetBundle

Organizing assets into AssetBundles

Build assets into AssetBundles

# Assign assets to an AssetBundle

To build assets into an AssetBundle, you must first assign assets to an AssetBundle, either in the Unity Editor or through a script. You can then [create and use a script](AssetBundles-Building.html) to build the AssetBundles. For information on the best approaches for organizing assets into AssetBundles, refer to [Organizing assets into AssetBundles](AssetBundles-Preparing.html).

**Note**: This workflow describes the creation of AssetBundles with the built-in [`BuildPipeline.BuildAssetBundles`](../ScriptReference/BuildPipeline.BuildAssetBundles.html) API. An alternative is to use the [Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest/index.html) package, which is built on top of AssetBundles and provides a UI to organize the assets in your project.

## Assign assets to AssetBundles in the Editor

To assign a given asset to an AssetBundle in the Unity Editor, perform the following steps:

1. Select the asset in the **Project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
   See in [Glossary](Glossary.html#Projectwindow) and view it in the [Inspector](UsingTheInspector.html)A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector).
2. Use the **AssetBundle** left-hand dropdown menu at the bottom of the Inspector window to assign or create an AssetBundle:
   * To create a new AssetBundle, select the left-hand dropdown and select **New**, or choose an existing AssetBundle from the list. **Tip:** To organize AssetBundles with subfolders, use the `/` character. For example, use the AssetBundle name `environment/forest` to create an AssetBundle named `forest` under an `environment` subfolder.
3. Optionally use the right-hand menu to assign or create an [AssetBundle variant](AssetBundles-Preparing.html#assetbundle-variants):
   * To create a new variant, select the right-hand dropdown and select **New**, or choose an existing variant from the list.

### Assigning multiple assets to an AssetBundle

You can assign an AssetBundle to a folder in your project. By default, all assets in that folder are assigned to the same AssetBundle as the folder. However, the AssetBundle assignments for individual assets takes precedence. To assign an AssetBundle to a folder:

1. Select the folder in its containing parent folder the Project window.
2. Use the **AssetBundle** dropdown to assign a new or existing AssetBundle to the folder.

You can also select multiple assets and assign them to an AssetBundle. However, assigning assets to an AssetBundle in this way overrides any existing AssetBundle assignments for those assets.

## Assign assets to AssetBundles with a script

To assign assets to AssetBundles in your code, use the [`BuildPipeline.BuildAssetBundles`](../ScriptReference/BuildPipeline.BuildAssetBundles.html) method with an array of [`AssetBundleBuild`](../ScriptReference/AssetBundleBuild.html) structures. This approach overrides any AssetBundle assignments made in the Inspector.

If you want your script to respect AssetBundle assignments made in the Inspector, use [`AssetDatabase.GetAllAssetBundleNames`](../ScriptReference/AssetDatabase.GetAllAssetBundleNames.html) and [`AssetDatabase.GetAssetPathsFromAssetBundle`](../ScriptReference/AssetDatabase.GetAssetPathsFromAssetBundle.html) to retrieve the necessary information and populate the `AssetBundleBuild` array.

## Additional resources

* [Organizing assets into AssetBundles](AssetBundles-Preparing.html)
* [Build assets into AssetBundles](AssetBundles-Building.html)

Organizing assets into AssetBundles

Build assets into AssetBundles

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)