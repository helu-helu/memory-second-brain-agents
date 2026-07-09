* [Assets and media](assets-and-media.html)
* [Managing assets with the Asset Database](AssetDatabase.html)
* Programming with the Asset Database

Refreshing the Asset Database

Reusing settings with preset assets

# Programming with the Asset Database

The `AssetDatabase` class has methods that allow you to access and perform operations on assets in the same way the Unity Editor does. You can create, import, delete, copy, move, load, and save assets, and search the asset database.

This means you can create anything from simple adjustments to powerful tools and customizations to your project’s asset workflow, using Unity’s [Editor scripting](../ScriptReference/Editor.html) and [Editor window customization](editor-EditorWindows.html).

For the full list of methods available, and documentation for each of the methods, refer to the [`AssetDatabase`](../ScriptReference/AssetDatabase.html) API reference.

## Batching AssetDatabase operations

You can use batching to save time when making changes to assets from code. If you make changes to multiple assets, the Asset Database’s default behavior is to process each change in turn, and perform a full [refresh process](AssetDatabaseRefreshing.html) for the asset before moving on to the next line of code.

The following example changes three assets, copying `Asset1`, moving `Asset2`, and deleting `Asset3`:

```
AssetDatabase.CopyAsset("Assets/Asset1.txt", "Assets/Text/Asset1.txt");
AssetDatabase.MoveAsset("Assets/Asset2.txt", "Assets/Text/Asset2.txt");
AssetDatabase.DeleteAsset("Assets/Asset3.txt");
```

Without batching, Unity processes each change before moving on to the next line of code. This takes an unnecessarily long time and triggers many callbacks.

To save time you can use the `AssetDatabase` APIs to pause automatic asset importing, define a series of asset operations in your code, and then resume automatic importing. On resumption, the Asset Database processes your defined asset operations as a batch, which is faster than processing them one by one.

For more details and an example implementation, refer to the [`AssetDatabase.StartAssetEditing`](../ScriptReference/AssetDatabase.StartAssetEditing.html) API reference.

## Accessing sub-assets

Asset files can contain multiple serialized objects, each of which can be considered an asset for the purposes of scripting with the `AssetDatabase` class. For example, a **.**prefab**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab)** asset file could contain a serialized **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) with multiple components attached. Each of those components are also serialized as objects in the asset file, and so when accessing the contents of the prefab asset using `AssetDatabase` methods, the component objects within the asset file are considered sub-assets.

When asset types contain more than one serialized asset object, Unity treats one of the assets as the main asset. The main asset is always the first asset added to the file, unless otherwise specified with the [`SetMainObject`](../ScriptReference/AssetDatabase.SetMainObject.html) method.

The Editor displays some types of sub-assets in the **project window**A window that shows the contents of your `Assets` folder (Project tab) [More info](ProjectView.html)  
See in [Glossary](Glossary.html#Projectwindow). In the following example, an FBX asset file containing a `Space Frigate` model is expanded in the **Project** window to reveal a material and a **mesh**The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](mesh.html)  
See in [Glossary](Glossary.html#Mesh) as sub-assets:

![An FBX asset file in the Project window, showing two sub-assets, a material and mesh](../uploads/Main/AssetDatabaseCustomizingSubAssets.png)


An FBX asset file in the Project window, showing two sub-assets, a material and mesh

Some sub-asset types don’t show in the **Project** window. For example, the `Space Frigate` asset file in the previous example actually contains more than the two sub-assets displayed in the project window. You can see the real number of assets when you access the asset file using `AssetDatabase` methods, as demonstrated in the following example:

```
using UnityEngine;
using UnityEditor;

public class Example : MonoBehaviour
{
    [MenuItem("AssetDatabase/InspectAssets")]

    private static void InspectAssets()
    {
        Object[] data = AssetDatabase.LoadAllAssetsAtPath("Assets/Space Frigate.fbx");

        Debug.Log(data.Length + " Assets");
        foreach (Object o in data)
        {
            Debug.Log(o);
        }
    }
}
```

In this case, the output shows that the imported, serialized version of this file contains six assets:

```
6 Assets
Space Frigate (UnityEngine.GameObject)
space_frigate_0 (UnityEngine.Material)
space_frigate_0 (UnityEngine.Mesh)
Space Frigate (UnityEngine.Transform)
Space Frigate (UnityEngine.MeshRenderer)
Space Frigate (UnityEngine.MeshFilter)
```

This is because the GameObject, material, the mesh data itself, and each of the components that Unity automatically added to the GameObject during the import process (the Transform, the MeshFilter, and the MeshRenderer), each count as a separate serialized object. Therefore they are sub-assets of the asset file, and as far as the `AssetDatabase` API is concerned, are each a separate asset.

## Asset import order and code execution

The [asset import order](AssetDatabaseRefreshing.html#refresh-process) has some important implications for your code. **Scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) are always imported and compiled before all other non-default assets, because they can include custom [asset post-processors](../ScriptReference/AssetPostprocessor.html) or [scripted importers](../ScriptReference/AssetImporters.ScriptedImporter.html) that are used later to import non-script assets.

The [`[InitializeOnLoad]`](../ScriptReference/InitializeOnLoadAttribute.html) attribute is a common way to run code on project startup or when scripts change. This callback runs after domain reload, but before import of non-script assets. Methods such as [`AssetDatabase.LoadAssetAtPath`](../ScriptReference/AssetDatabase.LoadAssetAtPath.html) that rely on the asset being imported won’t work as intended if called from `[InitializeOnLoad]`. They will return null for assets being imported for the first time, and return the outdated version of assets being reimported.

Code for custom [scripted importers](ScriptedImporters.html), asset pre-processors, and asset post-processors should not rely on specific assets being imported in a determined order. The import process groups assets into queues by type. The types are imported in a predefined order, but the import order among assets of the same type is not deterministic, unless you use [`ScriptedImporter.GatherDependenciesFromSourceFile`](../ScriptReference/AssetImporters.ScriptedImporter.GatherDependenciesFromSourceFile.html). Using `GatherDependenciesFromSourceFile` also creates a dependency between the assets, so modifying an asset triggers reimport of any assets that depend on it.

**Note:** Default assets are imported by the [built-in DefaultImporter](BuiltInImporters) before script assets, so any script-defined [`OnPostProcessAllAssets`](../ScriptReference/AssetPostprocessor.OnPostprocessAllAssets.html) won’t run for default assets.

## Additional resources

* [Contents of the Asset Database](asset-database-contents.html)
* [Refreshing the Asset Database](AssetDatabaseRefreshing.html)

Refreshing the Asset Database

Reusing settings with preset assets

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)