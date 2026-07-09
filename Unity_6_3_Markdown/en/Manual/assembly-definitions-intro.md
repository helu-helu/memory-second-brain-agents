* [Programming in Unity](scripting.html)
* [Compilation and code reload](compilation-and-code-reload.html)
* [Script compilation](script-compilation.html)
* [Organizing scripts into assemblies](assembly-definition-files.html)
* Introduction to assemblies in Unity

Organizing scripts into assemblies

Creating assembly assets

# Introduction to assemblies in Unity

Unity provides two special asset types, Assembly Definitions and Assembly References, to help organize your **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) into assemblies.

An assembly is a C# code library that contains the compiled classes and structs that are defined by your scripts and which also define references to other assemblies. For more information about assemblies in C#, refer to [Assemblies in .NET](https://learn.microsoft.com/en-us/dotnet/standard/assembly/)

By default, Unity compiles almost all of your game scripts into a predefined assembly called `Assembly-CSharp.dll`. Unity also creates a [few smaller, specialized predefined assemblies](script-compile-order-folders.html).

This arrangement works acceptably for small projects, but has some drawbacks as you add more code to your project:

* Every time you change one script, Unity has to recompile all the other scripts, increasing overall compilation time for iterative code changes.
* Any script can directly access types defined in any other script, which can make it more difficult to refactor and improve your code.
* All scripts are compiled for all platforms.

By defining assemblies, you can organize your code to promote modularity and reusability. Scripts in assemblies you define are no longer added to the default assemblies and can only access scripts in your other custom assemblies.

![A conceptual illustration of organizing scripts into multiple custom assemblies as an alternative to compiling them all in the default assembly. An arrow points from the default assembly, Assembly-Csharp, to an alternative setup in which a custom Main assembly directly references two other custom assemblies called Stuff and ThirdParty. Stuff in turn references a fourth custom assembly called Library.](../uploads/Main/ScriptCompilation.png)


A conceptual illustration of organizing scripts into multiple custom assemblies as an alternative to compiling them all in the default assembly. An arrow points from the default assembly, Assembly-Csharp, to an alternative setup in which a custom Main assembly directly references two other custom assemblies called Stuff and ThirdParty. Stuff in turn references a fourth custom assembly called Library.

The previous diagram illustrates how you might split up the code in your project into multiple assemblies. Because *Main* references *Stuff* and not the other way around, you know that any changes to the code in *Main* cannot affect the code in *Stuff*. Similarly, because *Library* doesn’t depend on any other assemblies, you can more easily reuse the code in *Library* in another project.

## Defining assemblies

To organize your project code into assemblies, create a folder for each desired assembly and move the scripts that should belong to each assembly into the relevant folder. Then [create Assembly Definition assets](assembly-definitions-creating.html) to specify the assembly properties.

Unity compiles all the scripts in a folder that contains an Assembly Definition into a single assembly, using the name and other settings defined by the asset. The assembly includes any scripts in subfolders unless a subfolder has its own Assembly Definition or [Assembly Reference](class-AssemblyDefinitionReferenceImporter.html) asset.

To include scripts from a non-child folder in an existing assembly, create an Assembly Reference asset in the non-child folder and set it to reference the Assembly Definition asset that defines the target assembly. For example, you can combine the scripts from all the Editor folders in your project in their own assembly, no matter where those folders are located.

Unity compiles assemblies in an order determined by their dependencies. You can’t specify the order in which compilation takes place.

## Finding which assembly a script belongs to

To identify which assembly a script belongs to, select the script file in the **Project** window to view its properties in the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window. The assembly filename and the Assembly Definition, if one exists, are shown in the **Assembly Information** section of the **Inspector**.

## Editor folder

Unity normally compiles any scripts in folders named `Editor` into the [predefined `Assembly-CSharp-Editor` assembly](script-compile-order-folders.html) no matter where those scripts are located. However, if you create an Assembly Definition asset in a folder that has an `Editor` folder underneath it, Unity no longer puts those **Editor scripts**C# source files composed entirely of code that runs in the Unity Editor only and not in the runtime Player build. Keep such scripts in dedicated Editor assemblies either by placing them in a parent folder called Editor or creating an Editor-only assembly definition.  
See in [Glossary](Glossary.html#Editorscripts) into the predefined Editor assembly. Instead, they go into the new assembly created by your Assembly Definition, where they might not belong. To manage `Editor` folders, you can create Assembly Definition or Reference assets in each `Editor` folder to place those scripts in one or more Editor assemblies. For more information, refer to [Creating an assembly for Editor code](assembly-definitions-creating.html#create-editor-assembly).

For more information on using the reserved folder name `Editor` for Editor scripts, refer to [Reserved folder name reference](SpecialFolders.html).

## Additional resources

* [Creating assembly definitions](assembly-definitions-creating.html)
* [Referencing assemblies](assembly-definitions-referencing.html)
* [Assembly metadata and compilation details](assembly-definition-metadata.html)
* [Assembly Definition properties](class-AssemblyDefinitionImporter.html)
* [Assembly Definition Reference properties](class-AssemblyDefinitionReferenceImporter.html)
* [Assembly Definition File Format](assembly-definition-file-format.html)

Organizing scripts into assemblies

Creating assembly assets

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)