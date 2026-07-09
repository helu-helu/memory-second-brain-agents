* [Programming in Unity](scripting.html)
* [Compilation and code reload](compilation-and-code-reload.html)
* [Script compilation](script-compilation.html)
* [Organizing scripts into assemblies](assembly-definition-files.html)
* Assembly metadata and compilation details

Conditionally including assemblies

Assembly Definition Inspector window reference

# Assembly metadata and compilation details

You can define additional metadata for your assemblies and retrieve information on the assemblies included in a [project build](building-introduction.html).

## Setting assembly attributes

You can use assembly attributes to set metadata properties for your assemblies. Although not a requirement, it’s good practice to define these attributes in a separate file named `AssemblyInfo.cs` alongside your Assembly Defintion.

For example, the following assembly attributes specify several .NET assembly metadata values and the Unity-defined [`Preserve`](../ScriptReference/PreserveAttribute.html) attribute, which affects how unused code is removed from an assembly when you build your project:

```
[assembly: System.Reflection.AssemblyCompany("Bee Corp.")]
[assembly: System.Reflection.AssemblyTitle("Bee's Assembly")]
[assembly: System.Reflection.AssemblyCopyright("Copyright 2020.")]
[assembly: UnityEngine.Scripting.Preserve]
```

## Getting assembly information in build scripts

Use the [`CompilationPipeline`](../ScriptReference/Compilation.CompilationPipeline.html) class to retrieve information about all assemblies built by Unity for a project, including those created based on Assembly Definition assets.

For example, the following script uses the `CompilationPipeline` class to list all the current Player assemblies in a project:

```
using UnityEditor;
using UnityEditor.Compilation;
public static class AssemblyLister
{
    [MenuItem("Tools/List Player Assemblies in Console")]
    public static void PrintAssemblyNames()
    {
        UnityEngine.Debug.Log("== Player Assemblies ==");
        Assembly[] playerAssemblies =
            CompilationPipeline.GetAssemblies(AssembliesType.Player);

        foreach (var assembly in playerAssemblies)
        {
            UnityEngine.Debug.Log(assembly.name);
        }
    }
}
```

## Additional resources

* [Creating assembly definitions](assembly-definitions-creating.html)
* [Referencing assemblies](assembly-definitions-referencing.html)
* [Assembly Definition properties](class-AssemblyDefinitionImporter.html)
* [Assembly Definition Reference properties](class-AssemblyDefinitionReferenceImporter.html)
* [Assembly Definition File Format](assembly-definition-file-format.html)

Conditionally including assemblies

Assembly Definition Inspector window reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)