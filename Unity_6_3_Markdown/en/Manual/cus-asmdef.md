* [Packages and package management](PackagesList.html)
* [Package creation](cus-pkg-lp.html)
* [Package development](cus-pkg-development.html)
* Create or edit the assembly definitions

Add code to your package

Package manifest

# Create or edit the assembly definitions

When you create a Unity Package Manager (UPM) package that contains code, you must include at least one assembly definition file (`.asmdef`).

The Unity Editor relies on the assembly definition file to compile the **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) in your package as a separate unit. Unlike scripts in your project’s `Assets` folder (which the Editor automatically compiles), the Editor ignores scripts inside the `Packages` folder unless they’re part of an assembly definition.

For more information about assembly definitions, refer to [organizing scripts into assemblies](assembly-definition-files.html).

## Create an assembly definition

When you start developing your package, you need only one assembly definition per package folder that contains code (`Editor`, `Runtime`, `Tests/Editor`, `Tests/Runtime`). When you [create a package](cus-create.html) using the Package Manager window, Unity creates the assembly definitions in these folders for you. If you decide to organize your code into more complex folder structures, you might need more assembly definition files:

* If you create folders at the same level as the four basic code folders, the additional folders require `.asmdef` files.
* If you create subfolders within the four basic code folders, you can optionally create additional `.asmdef` files for the code if you want to put that code in separate assemblies.

If you create a more complex folder structure and need to create additional assembly definitions, refer to [creating assembly assets](assembly-definitions-creating.html).

**Important**: If the code in your `Editor` folder depends on runtime code, then you need to add a reference from the `Editor` assembly definition to the `Runtime` assembly definition. For more information, refer to [Adding a reference to another assembly](assembly-definitions-referencing.html#reference-another-assembly). Runtime code cannot reference Editor code.

## Edit an assembly definition

When you [create a package](cus-create.html) using the Package Manager window, Unity populates some assembly definition fields for you. Use these steps to review the populated fields, add values to optional fields, and add references to other assemblies.

**Note**: Although you can edit `.asmdef` files directly, the recommended best practice is to use the Unity Editor, which helps prevent errors and validates your changes.

To edit an assembly definition:

1. Open the **Project** window and go to the folder for your package.
2. Go to the `Editor`, `Runtime`, or `Test` folder for the assembly definition you want to edit.
3. Select the assembly definition file.
4. Go to the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector)** window.
5. Set the fields as necessary. Common fields that might need editing include:

   * **Name**: The name of the assembly. Other scripts can reference this name in their own `.asmdef` files.
   * **Assembly Definition References**: If your assembly depends on other assemblies, you can add them here. Examples include `UnityEngine.UI` or an `Editor` assembly that depends on a custom `Runtime` assembly.
   * **Platforms**: You can limit this assembly to specific platforms.
6. Select **Apply** at the bottom of the **Inspector** window.

## Additional resources

* [Package layout for UPM packages](cus-layout.html)
* [Introduction to assemblies in Unity](assembly-definitions-intro.html)
* [Organizing scripts into assemblies](assembly-definition-files.html)

Add code to your package

Package manifest

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)