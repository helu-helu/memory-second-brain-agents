* [Packages and package management](PackagesList.html)
* [Package creation](cus-pkg-lp.html)
* [Package development](cus-pkg-development.html)
* [Package structure](cus-pkg-structure.html)
* Package layout for UPM packages

Package name guidelines

Add code to your package

# Package layout for UPM packages

Explore the folder and file layout for Unity Package Manager (UPM) packages.

When you [create the package structure](cus-create.html), the Package Manager creates the following folder and file layout, which is consistent with **UPM packages**A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage) from the Unity Registry:

```
<package-root>
  ├── package.json
  ├── README.md
  ├── CHANGELOG.md
  ├── Third Party Notices.md
  ├── Editor
  │   ├── <organization-name>.<package-name>.Editor.asmdef
  │   └── EditorExample.cs
  ├── Runtime
  │   ├── <organization-name>.<package-name>.asmdef
  │   └── RuntimeExample.cs
  ├── Tests
  │   ├── Editor
  │   │   ├── <organization-name>.<package-name>.Editor.Tests.asmdef
  │   │   └── EditorExampleTest.cs
  │   └── Runtime
  │        ├── <organization-name>.<package-name>.Tests.asmdef
  │        └── RuntimeExampleTest.cs
  ├── Samples
  │        ├── Example
  │        └── ...
  └── Documentation
       └── <package-name>.md
```

| **File or folder** | **Description** |
| --- | --- |
| `package.json` | The [package manifest](upm-manifestPkg.html)Each package has a *manifest*, which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](upm-manifestPkg.html) See in [Glossary](Glossary.html#packagemanifest), which defines the package dependencies and other metadata. |
| `README.md` | Developer package documentation. This documentation helps developers who want to change the package or push a new change on the package’s main branch. |
| `CHANGELOG.md` | Description of package changes in reverse chronological order. It’s good practice to use a standard format, like [Keep a Changelog](http://keepachangelog.com/en/1.0.0/). |
| `Third Party Notices.md` | Contains information that’s required to meet [legal requirements](cus-legal.html) for third-party code or dynamic link libraries (DLL) used in your package. |
| `Editor/` | Contains assets (which can include scripts and libraries) for tools and utilities used in the Unity Editor. Unlike folders under the project’s `Assets` folder, this is only a convention and doesn’t affect the asset import pipeline. Refer to [Create or edit the assembly definitions](cus-asmdef.html) to configure Editor-specific assemblies in this folder. |
| `Runtime/` | Contains assets (which can include scripts and libraries) for tools and utilities used at runtime. This is only a convention and doesn’t affect the asset import pipeline. Refer to [Assembly definition and packages](cus-asmdef.html) to configure runtime assemblies in this folder. |
| `Tests/` | Folder to store any [tests included](cus-tests.html) in the package. |
| `Tests/Editor/` | Editor platform-specific tests folder. Refer to [Create or edit the assembly definitions](cus-asmdef.html) to configure Editor-specific test assemblies in this folder. |
| `Tests/Runtime/` | Runtime platform-specific tests. Refer to [Create or edit the assembly definitions](cus-asmdef.html) to configure runtime test assemblies in this folder. |
| `Samples/` | Folder to store any [samples included](cus-samples.html) in the package. |
| `Documentation/` | Folder to store any [documentation included](cus-document.html) in the package. |

**Note**: The **Create package** function names the `Documentation` and `Samples` folders without a trailing tilde (`~`). This differs from packages installed from the Unity registry, where the included tilde hides these folders in the **Project** window. When you [export your UPM package](cus-export.html), Unity automatically adds the tilde to the `Samples` folder to match the behavior of registry packages. For more information about hidden assets, refer to [Reserved folder name reference](SpecialFolders.html).

## Additional resources

* [Package creation](cus-pkg-lp.html)
* [Package development workflow](CustomPackages.html)
* [Reserved folder name reference](SpecialFolders.html)

Package name guidelines

Add code to your package

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)