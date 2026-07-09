* [Assets and media](assets-and-media.html)
* [Unity Asset Store](AssetStore.html)
* [Downloading and managing Asset Store packages](asset-store-downloads.html)
* Manage Asset Store packages in the Editor

Purchase or download an Asset Store package

Manage packages in the Asset Store

# Manage Asset Store packages in the Editor

Asset Store packages are collections of files and data from Unity projects, or elements of projects. An **Asset Store**A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](AssetStore.html)  
See in [Glossary](Glossary.html#AssetStore) package type is either [a UPM package](asset-store-upm.html) or an **asset package**A collection of files and data from Unity projects, or elements of projects, which are compressed and stored in one file, similar to Zip files, with the `.unitypackage` extension. Asset packages are a handy way of sharing and re-using Unity projects and collections of assets. [More info](AssetPackages.html)  
See in [Glossary](Glossary.html#assetpackage) (`.unitypackage` format). When you add an Asset Store package to your project, the [Unity Package Manager](upm-ui.html) unpacks the package and maintains its directory structure and metadata about assets. This metadata includes information such as import settings and links to other assets.

## Using Asset Store packages

To use an Asset Store package, perform the following steps:

1. Open the [Unity Package Manager window](upm-ui.html)
2. Select the [My Assets](upm-ui-nav.html#contexts) context to view the [list of available Asset Store packages](upm-ui-list.html). You can also [search by name](upm-ui-search.html) for Asset Store packages.
3. The method to add the package to your project depends on the type you’ve downloaded:
   * For asset packages (`.unitypackage`), refer to [Download and import an asset package](upm-ui-import.html).
   * For **UPM packages**A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
     See in [Glossary](Glossary.html#UPMpackage), refer to [Install a UPM package from Asset Store](upm-ui-install2.html).

If the Asset Store package has a newer version available, you can also update it directly in the Package Manager window. To update an asset package (`.unitypackage`), refer to [Updating an asset package](upm-ui-update2.html), and to update a UPM package, refer to [Switch to another version of a UPM package](upm-ui-update.html).

## Location of downloaded asset package files

**Note**: This information applies only to asset packages (`.unitypackage`) you get from the Asset Store. It doesn’t apply to UPM packages you get from the Asset Store.

You can use the Package Manager window to manage your Asset Store packages within your project. However, if you need to access files from an asset package directly, you can find them in the cache for asset packages. This cache, which is separate from the [global cache](upm-cache.html), makes reusing and sharing asset packages more efficient. You can find the cache for asset packages in the following paths (which might be within hidden folders depending on your computer settings):

* macOS: `~/Library/Unity/Asset Store-5.x`
* Windows: `C:\Users\accountName\AppData\Roaming\Unity\Asset Store-5.x`
* Linux: `~/.local/share/unity3d/Asset Store-5.x`

These folders contain subfolders that correspond to particular Asset Store vendors and are available after download and import. The Package Manager stores asset files inside the subfolders using a structure defined by the Asset Store package publisher.

You can override the default location of the cache for asset packages. For information, refer to [Customize the asset package cache location](upm-config-cache-as.html).

## Additional resources

* [Package types](upm-package-types.html)
* [Manage packages in the Asset Store](AssetPackagesOrganize.html)
* [Publishing Asset Store packages](asset-store-publishing.html)

Purchase or download an Asset Store package

Manage packages in the Asset Store

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)