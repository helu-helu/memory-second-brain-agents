* [Building and publishing](building-and-publishing.html)
* Cache location reference

AssetBundle and Addressables determinism

Unity Services

# Cache location reference

If you need to investigate build problems, then it can be useful to understand where Unity stores the caches and metadata files related to a Player build.

| **File location** | **Description** |
| --- | --- |
| `Library/Bee` | Contains most cached build content. |
| `Library/BuildPlayerData` | Contains TypeDB files that record the schema of each C# type in your project at build time. Unity’s serialization system uses these files to reconcile differences between the Editor and Player builds, such as fields that are conditionally compiled and excluded from the Player. |
| `Library/PlayerDataCache` | Contains staged and cached content from the build in a platform-specific subdirectory of this directory.  The content reuse aspect of the incremental build pipeline relies on the files `ScriptsOnlyCache.yaml` and `DataBuildDirtyInfo.json` inside the `Library/PlayerDataCache` directory. These record information about the most recent build of the content, and Unity uses them to determine if that content can be reused. If either of those files are missing then Unity performs a clean build. |
| `Temp/StagingArea/Data/Managed` | Contains assemblies if you use the [`OnPostBuildPlayerScriptDLLs`](../ScriptReference/Build.IPostBuildPlayerScriptDLLs.OnPostBuildPlayerScriptDLLs.html) callback. |
| `BEE_CACHE_DIRECTORY` | A machine-level cache that reuses specific parts of builds, such as non-embedded packages and libIL2CPP artifacts across different projects. The location of this cache is set using the `BEE_CACHE_DIRECTORY` environment variable, and defaults to a different location depending on your operating system:  * **Windows:**`%USERPROFILE%\AppData\Local\Unity\Caches\bee` * **macOS:** `$HOME/Library/Unity/cache/bee` * **Linux:** `$XDG_CONFIG_HOME/.cache/unity3d/bee` (if `$XDG_CONFIG_HOME` is set) or `$HOME/.cache/unity3d/bee` |

The `Library` directory also stores the [shader cache](Shaders.html) and the [AssetDatabase](AssetDatabase.html) cache, both of which cache data and help speed up subsequent Player builds.

Modifying or deleting these files outside of Unity can lead to unexpected issues during subsequent builds. These locations and filenames are subject to change between versions of Unity. If you experience build problems related to caching, consider performing a [clean build](build-clean-build.html).

## Additional resources

* [Content output of a build](build-content-output.html)
* [Create a clean build](build-clean-build.html)

AssetBundle and Addressables determinism

Unity Services

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)