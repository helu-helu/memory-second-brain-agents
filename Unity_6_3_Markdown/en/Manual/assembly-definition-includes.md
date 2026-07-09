* [Programming in Unity](scripting.html)
* [Compilation and code reload](compilation-and-code-reload.html)
* [Script compilation](script-compilation.html)
* [Organizing scripts into assemblies](assembly-definition-files.html)
* Conditionally including assemblies

Referencing assemblies

Assembly metadata and compilation details

# Conditionally including assemblies

You can use preprocessor symbols to control whether an assembly is compiled and included in builds of your application (including Play mode in the Editor). You can specify which symbols must be defined for an assembly to be used with the **Define Constraints** list in the Assembly Definition options:

1. Select the Assembly Definition for the assembly to view its properties in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
   See in [Glossary](Glossary.html#Inspector).
2. In the **[Define Constraints](class-AssemblyDefinitionImporter.html#define-constraints)** section, click the **+** button to add a new symbol to the list of constraints.
3. Enter the symbol name.
4. Click **Apply**.

For more information on which scripting symbols you can use for define constraints, refer to [Define Constraints](class-AssemblyDefinitionImporter.html#define-constraints).

## Defining symbols based on Unity and project package versions

If you need to compile different code in an assembly according to whether a project uses specific versions of Unity or of a package, you can add entries to the **Version Defines** list. This list specifies rules for when a symbol should be defined. For version numbers, you can specify a logical expression that evaluates to a specific version or a range of versions.

To conditionally define a symbol:

1. Select the Assembly Definition asset for the assembly to view its properties in the **Inspector**.
2. In the **[Version Defines](class-AssemblyDefinitionImporter.html#version-defines)** section, click the **+** button to add an entry to the list.
3. Set the properties:

   * **If resource**: Choose **Unity** or the package or module that must be installed in order for this symbol to be defined.
   * **version is**: An expression that evaluates to a specific version or a range of versions. Refer to [Version Define expressions](#version-define-expressions) for the syntax rules.
   * **set define**: The scripting symbol to define when the version conditions are met.

   The **Version expression outcome** shows which versions the expression evaluates to. If the outcome displays, **Invalid**, then the expression syntax is incorrect.
4. Click **Apply**.

Symbols defined in the Assembly Definition are only in scope for the **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) in the assembly created for that definition.

**Note**: You can use the symbols defined using the **[Version Defines](class-AssemblyDefinitionImporter.html#version-defines)** list as **[Define Constraints](class-AssemblyDefinitionImporter.html#define-constraints)**. This means you can specify that an assembly is only used when specific versions of a given package are also installed in the project.

### Version define expressions

You can use expressions to specify an exact version or a range of versions.

A version expression uses mathematical [interval notation](https://en.wikipedia.org/wiki/Interval_(mathematics)), where square brackets `[]` designate that the range includes the endpoint and parentheses `()` designate that the range excludes the endpoint.

The following table illustrates the syntax:

| Expression | Evaluates to |
| --- | --- |
| `[1.3,3.4.1]` | `1.3.0 <= x <= 3.4.1` |
| `(1.3.0,3.4)` | `1.3.0 < x < 3.4.0` |
| `[1.1,3.4)` | `1.1.0 <= x < 3.4.0` |
| `(0.2.4,5.6.2-preview.2]` | `0.2.4 < x <= 5.6.2.-preview.2` |
| `[2.4.5]` | `x = 2.4.5` |
| `2.1.0-preview.7` | `x >= 2.1.0-preview.7` |

**Note:** No spaces are allowed in an expression. No wildcard characters are supported.

### Unity versioning scheme

Current versions of Unity (and all versions that support Assembly Definitions) use a version designator with three parts: `MAJOR.MINOR.REVISION`, for example, `6000.0.33f1`.

* The `MAJOR` version is four digits representing the release year for Unity `2022.x.z` and earlier, or the major technical version from Unity 6 (`6000.x.z`) onwards.
* The `MINOR` version is the target release quarter, such as `1`, `2`, `3`, or `4`.
* The `REVISION` designator has three parts of its own, with the format: `RRzNN`, where:
  + `RR` is a one or two digit revision number
  + `z` is a letter designating the release type:
    - `a` = alpha release
    - `b` = beta release
    - `f` = a normal public release
    - `c` = China release version (equivalent to f)
    - `p` = patch release
    - `x` = experimental release
  + `NN` is a one or two digit incremental number

Release type designators are compared as follows:

> `a < b < f = c < p < x`

An alpha release is considered earlier than a beta, which is earlier than a normal (`f`) or China (`c`) release. A patch release is always later than a normal or China release with the same revision number and an experimental release is later than any other release type. Note that experimental releases do not use an incremental number at the end.

The following example expression includes any 6000.0 or 6000.1 version of Unity, but not any version in 6000.2 or later:

```
[6000.0,6000.2)
```

### Package and module version numbers

Package and module version designators have four parts, following the [Semantic Versioning](https://semver.org/) format: `MAJOR.MINOR.PATCH-LABEL`. The first three parts are always numbers, but the label is a string. Unity packages in preview use the string, `preview` or `preview.n`, where `n > 0`.

The following example expression includes all versions of a package with `MAJOR.MINOR` versions between 3.2 and 6.1 (inclusive):

```
[3.2,6.1]
```

## Additional resources

* [Package versioning](upm-semver.html)
* [Creating assembly definitions](assembly-definitions-creating.html)
* [Referencing assemblies](assembly-definitions-referencing.html)
* [Assembly metadata](assembly-definition-metadata.html)
* [Assembly Definition properties](class-AssemblyDefinitionImporter.html)
* [Assembly Definition Reference properties](class-AssemblyDefinitionReferenceImporter.html)
* [Assembly Definition File Format](assembly-definition-file-format.html)

Referencing assemblies

Assembly metadata and compilation details

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)