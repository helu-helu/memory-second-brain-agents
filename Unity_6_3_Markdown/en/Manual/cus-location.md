* [Packages and package management](PackagesList.html)
* [Package creation](cus-pkg-lp.html)
* Comparison of package creation locations

Get started with package creation

Package development

# Comparison of package creation locations

Compare the different locations where you can place the package you create.

By default, Unity places packages you create in the `Packages` folder of your project. However, you can move a package outside the project folder during development and optionally link it back to the project.

Packages in either location are identical in structure, but each supports different workflows, especially involving modularity, reuse, and collaboration. Understanding these differences can help you avoid refactoring later.

Use the following table to understand the key differences between packages you create inside and outside of your project:

| **Feature or characteristic** | **Packages in your project folder** | **Packages outside your project folder** |
| --- | --- | --- |
| Package location | Inside the `Packages` subfolder of your Unity project | Outside the `Packages` subfolder of your Unity project |
| Typical use | Develop a package within a single project (the current project) | Develop and reuse the package across multiple projects |
| Creation method | Package Manager window | Package Manager window with some manual steps |
| **Project manifest**Each Unity project has a *project manifest*, which acts as an entry point for the Package Manager. This file must be available in the `<project>/Packages` directory. The Package Manager uses it to configure many things, including a list of dependencies for that project, as well as any package repository to query for packages. [More info](upm-manifestPrj.html) See in [Glossary](Glossary.html#projectmanifest) file reference | Implicit (Unity automatically detects packages in the `Packages` subfolder) | Explicit reference required |
| **Version control**A system for managing file changes. You can use Unity in conjunction with most common version control tools, including Perforce, Git, Mercurial and Unity Version Control (UVCS). [More info](VersionControl.html) See in [Glossary](Glossary.html#versioncontrol) | Same repository as the project | Different repository than the project |
| Portability during development | Highly portable if the project uses version control | Limited due to environment-specific paths and system configuration |
| Identifying label that appears in Package Manager window | **Custom** | **Local** |

After you decide on a location for the package you will create, begin the package creation process by referring to [package development workflow](CustomPackages.html).

## Additional resources

* [Package creation](cus-pkg-lp.html)
* [Package development workflow](CustomPackages.html)
* [Project manifest file](upm-manifestPrj.html)
* [Local folder or tarball paths](upm-localpath.html)

Get started with package creation

Package development

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)