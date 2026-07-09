* [Assets and media](assets-and-media.html)
* [Managing assets at runtime](assets-managing-runtime.html)
* [Use AssetBundles to load assets at runtime](assetbundles-section.html)
* AssetBundle platform considerations

Handling dependencies between AssetBundles

Verifying downloaded AssetBundles

# AssetBundle platform considerations

AssetBundles are platform specific, meaning at runtime you can only load AssetBundles built for the target platform. This is because AssetBundles contain platform-specific asset formats, which leads to unexpected behavior if loaded on other platforms. This restriction prevents the accidental delivery of incorrect content to the wrong platform.

## Android specifics

To distribute AssetBundle content for the Android platform, you have the following options:

* Build AssetBundles into the [`StreamingAssets` folder](StreamingAssets.html).
* Package AssetBundles into custom asset packs.
* Deploy AssetBundles through a CDN.

The option you choose depends on the requirements of your project.

### Build AssetBundles into the StreamingAssets folder

AssetBundles placed in the [`StreamingAssets` folder](StreamingAssets.html) are automatically packaged as part of your application’s **APK**The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](android-BuildProcess.html)  
See in [Glossary](Glossary.html#APK) or OBB file.

You can’t load these files directly from the APK or OBB file with the standard file path APIs. Instead, you must load them with the [`UnityWebRequestAssetBundle`](../ScriptReference/Networking.UnityWebRequestAssetBundle.html) API with a `file:///` URL scheme. For example:

```
var assetBundlePath = "file://" + Application.streamingAssetsPath + "/" + assetbundleToLoad;
var loadOp = UnityWebRequestAssetBundle.GetAssetBundle(assetBundlePath);
yield return loadOp.SendWebRequest();
var assetBundle = DownloadHandlerAssetBundle.GetContent(loadOp);
```

Avoid using LZMA **compression**A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) for AssetBundles in the `StreamingAssets` folder because it’s inefficient to decompress LZMA files to a temporary memory file. Use LZ4 compression or leave them uncompressed. For more information, refer to [AssetBundles compression format](assetbundles-compression-format.html).

### Package AssetBundles into custom asset packs

You can place AssetBundles into Android’s asset pack format and deliver them to the Google Play Store. For more information, refer to [Asset packs in Unity](android-asset-packs-in-unity.html).

### Deploy AssetBundles through a CDN

You can host AssetBundles on a web server and download them as needed with [`UnityWebRequestAssetBundle`](../ScriptReference/Networking.UnityWebRequestAssetBundle.html).

You can use Unity’s [Cloud Content Delivery (CCD)](https://docs.unity.com/ugs/manual/ccd/manual/UnityCCD) service to simplify deployment, especially when integrated with Addressables. This approach is suitable for applications with large, dynamic content. Downloaded AssetBundles are typically saved to the application cache directory or `Application.persistentDataPath`.

## Console downloads and CRC

Typically, AssetBundles for consoles aren’t downloaded directly from the web using in-game code. Instead, they’re usually delivered via the platform’s own DLC (Downloadable Content) mechanisms. These DLCs are securely purchased, downloaded, and stored locally by the platform’s system, external to the game’s direct control. Once installed, the game can detect and load these new files.

When loading an AssetBundle on console platforms, don’t perform CRC. Consoles often have weaker CPUs that can take significant time to validate the CRC for a newly opened AssetBundle. Even on platforms with fast storage, a CPU-bound CRC check can slow down loading considerably.

## Additional resources

* [Downloading AssetBundles](AssetBundles-Integrity.html)
* [AssetBundle compression formats](assetbundles-compression-format.html)
* [AssetBundles in Web](webgl-assetbundles.html)

Handling dependencies between AssetBundles

Verifying downloaded AssetBundles

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)