* [Packages and package management](PackagesList.html)
* [Package creation](cus-pkg-lp.html)
* [Package development](cus-pkg-development.html)
* Package development workflow

Package development

Package structure

# Package development workflow

Create your own Unity Package Manager (UPM) package to extend the functionality of the Unity Editor.

You can use packages that you create for one of your projects or for multiple projects. You can also share your package with others in your organization or studio so they can use it in any project. You can even distribute your package through official channels, for the wider community to use.

Follow this workflow to create entirely new **UPM packages**A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage). For information about modifying copies of existing packages, refer to [Copy a Unity package to your project folder](upm-embed.html#embed-cached).

To create your own UPM package, complete the following tasks:

1. [Create the package structure](#createPkg).
2. [Add code to your package](#addCode).
3. [Edit the assembly definition](#edit-asmdef).
4. [Edit the package manifest](#editMan).
5. [Create samples for your package](#createSample).
6. [Add tests to your package](#addTests).
7. [Set the package version number](#serVersion).
8. [Update the changelog for your package](#updateLog).
9. [Add legal requirements to your package](#addLegal).
10. [Document your package](#docPkg).

## Prerequisites

Before you begin, determine whether you want to create your package inside or outside your project folder. For more information, refer to [Comparison of package creation locations](cus-location.html).

## Create the package structure

Use Package Manager’s **(+)** > **Create package** feature to create the folder structure and starter files. For more information, refer to [Create the package structure](cus-create.html).

## Add code to your package

Add the code, libraries, and any required assets that make your UPM package unique. For more information, refer to [Add code to your package](cus-add-code.html).

## Edit the assembly definition

Any code in your package must be organized into one or more assemblies using assembly definition files (`.asmdef` assets). Unity creates a separate assembly for each assembly definition, which includes all code in its folder and subfolders.

Package Manager’s **Create package** operation creates these assembly definitions for you, but you might need to modify them as your package evolves.

For more information, refer to [Edit the assembly definition](cus-asmdef.html).

## Edit the package manifest

The **package manifest**Each package has a *manifest*, which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](upm-manifestPkg.html)  
See in [Glossary](Glossary.html#packagemanifest) (`package.json`) defines the metadata for a UPM package, including its name, version, dependencies, and other configuration details.

Package Manager’s **Create package** operation creates this file for you, but it contains the minimum amount of required information. As your package evolves, you usually need to add more information to the package manifest.

For more information, refer to [Edit the package manifest](cus-edit-manifest.html).

## Create samples for your package

Although including samples in your package is optional, they’re a valuable tool for helping users learn how to use your package.

For more information, refer to [Create samples for your package](cus-samples.html).

## Add tests to your package

Including tests in your package is optional, but they’re a useful way to verify that your code works as intended and to help others validate changes safely.

The **Create package** operation creates example test files in the proper subfolder for you to modify.

For more information, refer to [Add tests to your package](cus-tests.html).

## Set the package version number

Your package version number must follow the principles of semantic versioning.

For information about semantic versioning and how to set your package’s version number, refer to [package versioning](upm-semver.html).

## Update the changelog for your package

Update the `CHANGELOG.md` file every time you publish a new version of your package.

For more information, refer to [Update the package changelog](cus-changelog.html).

## Add legal requirements to your package

Your package might have legal requirements or third party elements, which you need to communicate to those who consume it.

For information, refer to [Add required legal files to your package](cus-legal.html).

## Document your package

Including documentation in your package is optional, but offering clear guidance gives users a better experience and makes your package easier to adopt.

For information, refer to [Document your package](cus-document.html).

## Additional resources

* [Package creation](cus-pkg-lp.html)
* [Create and export asset packages](AssetPackagesCreate.html)

Package development

Package structure

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)