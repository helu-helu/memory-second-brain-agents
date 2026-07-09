* [Assets and media](assets-and-media.html)
* [Managing assets at runtime](assets-managing-runtime.html)
* [Use AssetBundles to load assets at runtime](assetbundles-section.html)
* Verifying downloaded AssetBundles

AssetBundle platform considerations

AssetBundle caching

# Verifying downloaded AssetBundles

You can distribute AssetBundles with your application or set up remote servers to download the AssetBundles from.

When downloading AssetBundles, precautions are necessary to prevent data corruption and attacks from malicious actors. Data corruption in downloaded AssetBundles is a common cause of crashes on user devices. While AssetBundles can’t contain executable code, altered serialized data might exploit vulnerabilities in your application code or the Unity runtime. A validation layer can help prevent random crashes or bad behavior.

## Download using a secure protocol

Use [`UnityWebRequestAssetBundle`](../ScriptReference/Networking.UnityWebRequestAssetBundle.html) to download AssetBundles from a remote web server. Always use HTTPS in your URL, unless it’s for a local web server on the same machine. HTTP is insecure and susceptible to man-in-the-middle attacks.

## Cyclic redundancy checks

To check that AssetBundles aren’t corrupted, you can use cyclic redundancy checks (CRC) against the 32-bit checksum that Unity generates during the AssetBundle build process. The checksum is stored in the `.manifest` file, and accessible via [`BuildPipeline.GetCRCForAssetBundle`](../ScriptReference/BuildPipeline.GetCRCForAssetBundle.html). When downloading AssetBundles via `UnityWebRequestAssetBundle.GetAssetBundle`, provide the expected CRC value to prevent invalid AssetBundles from [being cached](assetbundles-caching.html).

If you handle AssetBundle downloads directly outside Unity’s cache, perform integrity checks before using retrieved content. Optional parameters in the AssetBundle load APIs let you pass CRC values for validation. If the calculated CRC doesn’t match, the AssetBundle doesn’t load. For LZ4-compressed AssetBundles, this check is resource-intensive because it requires full decompression into RAM. LZMA-compressed AssetBundles already require full decompression for loading, so CRC checks don’t add significant overhead. To avoid repeated checks during loads, validate the AssetBundle once when it’s retrieved and saved on the device. Refer to [AssetBundle compression formats](assetbundles-compression-format.html) for more information.

The following are important considerations to take when validating AssetBundles:

* Don’t use common hashing algorithms such as md5 to validate AssetBundles that use [LMZA compression](assetbundles-compression-format.html#lzma-compression). Unity might recompress AssetBundles without changing their content, which changes the file hash despite valid content. Unity calculates CRC values from the uncompressed content and the values remain consistent after compressing the content.
* The `IncrementalBuildHash` in the `.manifest` file isn’t a hash of the full file content. It serves as a version identifier and is unsuitable for file corruption detection.
* The `AssetFileHash` in the `.manifest` file, accessible via [`BuildPipeline.GetHashForAssetBundle`](../ScriptReference/BuildPipeline.GetHashForAssetBundle.html), is a true hash of the content.

## User-generated content

For user-generated content (UGC) distributed to other players, filter submissions to prevent inappropriate or malicious content. Don’t allow users to upload binary AssetBundle files directly. Instead, require them to upload source assets and build the AssetBundle files yourself. This process enables manual and automated filtering and allows you to rebuild AssetBundles for newer Unity versions if needed.

## Patching AssetBundles

When you make a new AssetBundle build, you can update existing installations with new or changed AssetBundles, and delete any unreferenced AssetBundles. An update to existing AssetBundles is called a patch. Unity supports a basic level of patching through the [AssetBundle cache](assetbundles-caching.html), and you can replace an existing version of an AssetBundle with [`UnityWebRequestAssetBundle.GetAssetBundle`](../ScriptReference/UnityWebRequestAssetBundle.GetAssetBundle.html). However, Unity doesn’t support differential patching, where you selectively update the content of the existing file to match the new file. If you want to create differential patches, you must extend or replace the AssetBundle cache with your own logic.

Using [`UnityWebRequestAssetBundle.GetAssetBundle`](../ScriptReference/UnityWebRequestAssetBundle.GetAssetBundle.html) with a different version or hash parameter triggers the download of updated AssetBundles.

The main challenge is identifying which AssetBundles need replacement. A patching system must manage two lists:

* Local AssetBundles: Currently downloaded AssetBundles and their version info.
* Server AssetBundles: Available AssetBundles on the server and their version info.

The patching system compares these lists, re-downloading AssetBundles that are missing or have updated version information.

Unity doesn’t support differential patching by default. `UnityWebRequestAssetBundle.GetAssetBundle` downloads entire files, even with the built-in cache system. If you need differential patching, implement custom downloaders. Unity orders AssetBundle data deterministically, so patch files for rebuilt AssetBundles can be much smaller. Uncompressed AssetBundles or those using LZ4 **compression**A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](texture-choose-format-by-platform.html), [Animation Compression](class-AnimationClip.html#AssetProperties), [Audio Compression](class-AudioClip.html), [Build Compression](ReducingFilesize.html).  
See in [Glossary](Glossary.html#compression) are more patch-efficient than LZMA-compressed AssetBundles.

For custom systems, use JSON for AssetBundle file lists and [.NET cryptography APIs](https://learn.microsoft.com/en-us/dotnet/standard/security/cryptography-model) to compute file hashes. These hashes can act as version identifiers, or you can use traditional version numbers if your build systems support them.

## Additional resources

* [`UnityWebRequestAssetBundle` API documentation](../ScriptReference/Networking.UnityWebRequestAssetBundle.html)
* [`Caching` API documentation](../ScriptReference/Caching.html)
* [Loading assets from AssetBundles](AssetBundles-Native.html)

AssetBundle platform considerations

AssetBundle caching

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)