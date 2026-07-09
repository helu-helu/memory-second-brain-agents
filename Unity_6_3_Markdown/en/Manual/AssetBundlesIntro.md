* [Assets and media](assets-and-media.html)
* [Managing assets at runtime](assets-managing-runtime.html)
* [Use AssetBundles to load assets at runtime](assetbundles-section.html)
* Introduction to AssetBundles

Use AssetBundles to load assets at runtime

Creating AssetBundles

# Introduction to AssetBundles

An AssetBundle is an archive file that you can use to group together assets to create downloadable content (DLC), or reduce the initial installation size of your application. You can also use AssetBundles to load optimized platform-specific assets, or lower memory usage at runtime.

An AssetBundle can contain platform-specific non-code assets, such as models, textures, **prefabs**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab), **audio clips**A container for audio data in Unity. Unity supports mono, stereo and multichannel audio assets (up to eight channels). Unity can import .aif, .wav, .mp3, and .ogg audio file format, and .xm, .mod, .it, and .s3m tracker module formats. [More info](class-AudioClip.html)  
See in [Glossary](Glossary.html#AudioClip), or entire **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene) that Unity then loads at runtime. AssetBundles are platform-specific because Unity builds asset data into formats based on the [`BuildTarget`](../ScriptReference/BuildTarget.html) you set when you [create a build](building-introduction.html). For example, an AssetBundle built for iOS isn’t compatible for Android.

You can also [compress AssetBundles](assetbundles-compression-format.html) using LZMA or LZ4 to efficiently distribute the archives.

To build and define AssetBundles, you can use the high-level [Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest) package, which provides a way of defining and building AssetBundles from the Unity Editor. If you prefer low-level API control, you can use the [`BuildPipeline.BuildAssetBundles`](../ScriptReference/BuildPipeline.BuildAssetBundles.html), [`AssetBundle`](../ScriptReference/AssetBundle.html), and [`UnityWebRequestAssetBundle`](../ScriptReference/Networking.UnityWebRequestAssetBundle.html) native APIs.

## Reasons to use AssetBundles

Using AssetBundles can help with content distribution and optimizing your application’s performance. The following are benefits of using the AssetBundle system:

* **Dynamic content delivery**: You can use AssetBundles to load assets on demand, which is especially useful for games with downloadable content (DLC), episodic updates, or live service models. It also helps efficiently manage memory, ensuring only the assets that your application needs are loaded into memory.
* **Reduced build size**: Moving assets to AssetBundles can reduce the initial application build size, which is important for mobile games or platforms with strict size limitations.
* **Platform compatibility**: You can create AssetBundles for different platforms, reducing the need to include platform-specific assets in your application’s build.

AssetBundles are useful if you want to optimize asset loading, such as only streaming content near a character’s location, only loading relevant localized content, or loading assets in the background. However, the AssetBundle system provides low-level asset management, so you might want to consider using the [Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest) package, which provides a higher level way of managing AssetBundles in your project.

If you’re prototyping, or have a particularly small project, you might want to consider using the [Resources system](LoadingResourcesatRuntime.html).

### Limitations

The AssetBundle system has the following limitations:

* You can only use AssetBundles in **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
  See in [Glossary](Glossary.html#Scripts), and there’s no Editor interface to build AssetBundles with.
* The `AssetBundle` API doesn’t keep track of asset dependencies. For example, if you want to load a prefab from an AssetBundle, you need to manually load the AssetBundles, and any AssetBundle that the AssetBundle depends on, before loading the prefab. Safely unloading AssetBundles often requires writing a reference counting system. For more information, refer to [Handling dependencies between AssetBundles](AssetBundles-Dependencies.html).
* You need to manually allocate and deallocate memory, so you might create memory leaks or missing content by unloading assets from an AssetBundle that other code relies on.
* The `AssetBundle` API isn’t aware of whether an AssetBundle is hosted locally or remotely, so you need to keep track of the location of all the AssetBundles in your project.

## Structure of an AssetBundle

The AssetBundle is a container file format, similar to a zip file. It contains the following file types in a binary-format header:

* **Serialized files**: Contains serialized Unity objects. This is the same binary file format used in Player builds. The output depends on what the AssetBundle contains:
  + Only assets: Unity creates a single serialized file.
  + Only scenes: Unity creates two serialized files per scene. One file contains the objects from the scene hierarchy, and the second contains any referenced objects.
* **Resource files:** Contains chunks of binary data stored separately for certain assets such as textures and audio. This separation allows Unity to use multithreaded code to efficiently load the assets from disk.

The AssetBundle file always includes a serialized [`AssetBundle`](../ScriptReference/AssetBundle.html) object that acts like a directory for the contents of the AssetBundle. You can use the `AssetBundle` instance to load assets from a specific AssetBundle archive in your code. For a more detailed look at the internal file format, refer to [AssetBundle file format reference](assetbundles-file-format.html).

## Scene AssetBundles

An AssetBundle not containing scenes is built based on a list of assets. Unity supports assigning scene files to an AssetBundle, but you can’t mix scenes with other assets inside a single AssetBundle. In the API, this type of AssetBundle is called a streaming scene AssetBundle, accessible via [`AssetBundle.isStreamedSceneAssetBundle`](../ScriptReference/AssetBundle-isStreamedSceneAssetBundle.html).

The process of building scenes into AssetBundles is similar to what happens during a Player build, reusing much of the same code.

## AssetBundle support between Unity versions

Any AssetBundles you create with older versions of Unity are usually compatible with newer versions of Unity. However, if there are large changes between versions, Unity might not be able to load the data, and you must rebuild the AssetBundle with a newer version of Unity. Unity doesn’t support forward-compatibility of AssetBundles, so you can’t load an AssetBundle built with a newer version of Unity into an older version of Unity.

If the serialization format for an object has changed, AssetBundle load code reads that object using the safe binary read deserialization method. This method uses type trees to match fields in the serialized data with the current object serialization layout, which affects performance. If AssetBundles are built without type trees (`BuildAssetBundleOptions.DisableWriteTypeTree`), any serialization changes in the newer Unity version prevent a successful load and might lead to a crash. Additionally, safe binary reads are slow, and you can avoid this by rebuilding AssetBundles to match the current Player build.

**Tip**: By default, Unity includes the version of the Unity Editor used to build the AssetBundle inside the AssetBundle header. This information can result in AssetBundles unnecessarily being rebuilt. To avoid this, exclude the Editor version from the header. For more information, refer to [`BuildAssetBundleOptions.AssetBundleStripUnityVersion`](../ScriptReference/BuildAssetBundleOptions.AssetBundleStripUnityVersion.html).

Unity serializes AssetBundles based on the Unity version and the C# types present during their creation. Unity stores the information in type tree structures and uses this information when it loads the objects from different versions of the Unity Editor. For more information on TypeTrees, refer to [Optimizing AssetBundles](assetbundles-optimizing.html#typetrees)

## Script support

AssetBundles can’t contain assemblies, so you can’t use them to distribute new C# classes or changes to existing classes. However, you can use an AssetBundle to distribute serialized object instances, such `ScriptableObject` assets.

Unity matches objects based on their assembly, namespace, and class names. It then creates an object that’s an instance of that class, using the serialized values to set the fields of the object. It uses the information stored in the type tree to adjust field mappings for different versions of Unity.

Unity uses the [conditional compilation](platform-dependent-compilation.html) information in your code to determine the fields to include in an AssetBundle. If a field’s compilation has been made conditional with an `#if` directive and the associated symbol isn’t defined at AssetBundle build time, then Unity doesn’t include that field in the AssetBundle.

For example, in the following code snippet the `always` field is unconditionally included in the AssetBundle, but the `experimental` field is only included if the `EXPERIMENTAL_FEATURE` symbol is defined at build time:

```
public class MyData : ScriptableObject
{
    public int always;
#if EXPERIMENTAL_FEATURE
    public int experimental;
#endif

public int ConditionalDataValue()
{
#if EXPERIMENTAL_FEATURE
    return experimental;
#else  
    return always;
#endif 
}

}
```

## Building AssetBundles

You can use the following method to build AssetBundles:

* **Addressables**: The [Addressables](http://docs.unity3d.com/Packages/com.unity.addressables@latest) package is a user-friendly way of defining and building AssetBundles from the Unity Editor. It simplifies AssetBundle creation and management with a high-level API.
* **Native APIs**: `BuildPipeline.BuildAssetBundles`, `AssetBundle`, and `UnityWebRequestAssetBundle` are native APIs you can use to build AssetBundles, but they require manual dependency management, and you must write your own build script to use them.

For more information, refer to [Build assets into an AssetBundle](AssetBundles-Building.html).

### Building multiple AssetBundles

When you build or rebuild AssetBundles, it’s best practice to use a single [`AssetBundle`](../ScriptReference/AssetBundle.html) API call to build all the project’s AssetBundles together. AssetBundles can reference and have dependencies on other AssetBundles. For example, a material in one AssetBundle can reference a texture in another AssetBundle. When you build AssetBundles together, Unity automatically manages the references and dependencies between them.

## Additional resources

* [Addressables package](http://docs.unity3d.com/Packages/com.unity.addressables@latest)
* [`BuildPipeline.BuildAssetBundles` API documentation](../ScriptReference/BuildPipeline.BuildAssetBundles.html)
* [Organizing assets into AssetBundles](AssetBundles-Preparing.html)

Use AssetBundles to load assets at runtime

Creating AssetBundles

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)