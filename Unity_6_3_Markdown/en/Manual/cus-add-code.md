* [Packages and package management](PackagesList.html)
* [Package creation](cus-pkg-lp.html)
* [Package development](cus-pkg-development.html)
* Add code to your package

Package layout for UPM packages

Create or edit the assembly definitions

# Add code to your package

Continue the development of your Unity Package Manager (UPM) package by adding the assets (including code) that make your package unique.

Before you begin this phase of development, consider how others will use your **UPM package**A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
See in [Glossary](Glossary.html#UPMpackage). Determine whether the package falls into one or both of the following categories:

* Code for tools that helps others as they develop a project. This code typically placed in the package’s `Editor` subfolder. Final builds of the project don’t include these packages. Examples include:
  + A custom debugger
  + A memory profiler
  + A level design tool for painting spawn points
* Code that runs during gameplay, whether that’s in the Editor’s Play mode or a built project. This code is typically placed in the package’s `Runtime` subfolder. Final builds of the project include these packages. Examples include:
  + A dialog system for branching conversations
  + A procedural generation engine
  + An input remapping system that let players customize controls at runtime

Follow these steps as you iterate on the development of your package:

1. Add Editor code to your package’s `Editor` subfolder and runtime code to the `Runtime` subfolder.

   **Note**: If your package also contains non-code assets, include them in the relevant folder.
2. Optional: You can organize your content in a more complex folder structure. However, complex structures might require you to update the package’s [assembly definition files](cus-asmdef.html).
3. Check the package’s [assembly definition files](cus-asmdef.html) to make sure they’re correct. They usually don’t need updating, unless you change the location of your **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
   See in [Glossary](Glossary.html#Scripts).
4. [Edit the package manifest](cus-edit-manifest.html), making sure all [required and recommended fields](upm-manifestPkg.html#required) have values. Consider supplying values for the relevant [optional fields](upm-manifestPkg.html#optional).
5. Test your package.

## Next steps

When your package is functioning as expected, you can proceed with other activities in the [package development workflow](CustomPackages.html). Typical activities at this stage of package development include:

* [Create or edit the assembly definition](cus-asmdef.html)
* [Add tests to your package](cus-tests.html)
* [Create samples for your package](cus-samples.html)

## Additional resources

* [Package creation](cus-pkg-lp.html)
* [Package development workflow](CustomPackages.html)

Package layout for UPM packages

Create or edit the assembly definitions

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)