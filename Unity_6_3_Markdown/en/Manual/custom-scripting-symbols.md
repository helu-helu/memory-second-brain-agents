* [Programming in Unity](scripting.html)
* [Compilation and code reload](compilation-and-code-reload.html)
* [Script compilation](script-compilation.html)
* [Conditional compilation](conditional-compilation.html)
* Custom scripting symbols

Unity scripting symbol reference

Test conditional compilation

# Custom scripting symbols

In addition to Unity’s [built-in scripting symbols](scripting-symbol-reference.html), you can define your own custom scripting symbols. Where you define custom scripting symbols determines the scope in which they apply. You can define custom symbols in the following places:

* An [asset file](#asset), for symbols that apply for all Editor and Player code in the project, regardless of the active [build profile](build-profiles.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](build-profiles.html)  
  See in [Glossary](Glossary.html#buildprofile).
* [Player Settings](#player-settings)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
  See in [Glossary](Glossary.html#PlayerSettings), for symbols that apply for all Editor and Player code when the given platform or one of its build profiles are active.
* A [build profile](#build-profile), for symbols that apply for all Editor and Player code when the given build profile is active.
* [From code](#code), for symbols that apply for the active platform or for individual Player builds, depending on the API used.

## Custom symbols for the whole project

You can define custom scripting symbols that apply for the whole project with a [response file](https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild-response-files?view=vs-2022) asset as follows:

1. Name the file `csc.rsp` and place it in the root of your project’s **Assets** folder.
2. Define scripting symbols on lines that start with `-define:`, followed by one or more semicolon-separated scripting symbols.

Unity reads this file at startup and applies it before compiling any code. For example, if you include the single line `-define:UNITY_DEBUG;UNITY_TEST` in your `csc.rsp` file, the symbols `UNITY_DEBUG` and `UNITY_TEST` are included as globally defined scripting symbols for all C# **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) in the project.

**Note**: Changes to `.rsp` files don’t take effect until Unity recompiles scripts. You can trigger recompilation by updating or reimporting a single script file.

## Custom symbols for a platform

You can define custom scripting symbols specific to a platform as follows:

1. Open [Player settings](class-PlayerSettings.html).
2. Navigate to the **Scripting Define Symbols** list in the **Other Settings** > **Script Compilation** section.
3. Add new scripting symbols to the list by selecting the **+** button and typing the name of the symbol in the text field. Remove existing list items with the **-** button.
4. When you’ve finished editing the list, select **Apply** to apply your changes. Unity recompiles the scripts in your project using the new symbols.

**Note**: The **Copy Defines** button copies the current set of custom scripting symbols from the list into your clipboard as a string of semicolon-separated values.

## Custom symbols for a build profile

You can define custom scripting symbols for a build profile as follows:

1. Select the build profile you want to define symbols for in the [Build Profiles window](build-profiles-reference.html).
2. Select **Add Settings** > **Scripting Defines**.
   A scripting defines list appears in the **Scripting Defines** foldout.
3. Add new scripting symbols to the list by selecting the **+** button and typing the name of the symbol in the text field. Remove existing list items with the **-** button. Modifications to the list save and apply automatically.

**Note**: You can launch the Editor with the `-activeBuildProfile` [command line argument](EditorCommandLineArguments.html) to make the specified build profile and its custom scripting symbols applicable from startup.

## Custom symbols defined from code

You can use the following APIs to define scripting symbols:

* [`PlayerSettings.SetScriptingDefineSymbols`](../ScriptReference/PlayerSettings.SetScriptingDefineSymbols.html)
* [`BuildPlayerOptions.extraScriptingDefines`](../ScriptReference/BuildPlayerOptions-extraScriptingDefines.html)
* [`Build.Player.ScriptCompilationSettings-extraScriptingDefines`](../ScriptReference/Build.Player.ScriptCompilationSettings-extraScriptingDefines.html)

`BuildPlayerOptions.extraScriptingDefines` and `Build.Player.ScriptCompilationSettings-extraScriptDefines` only apply to Player builds, so when defining scripting symbols that apply to your **Editor scripts**C# source files composed entirely of code that runs in the Unity Editor only and not in the runtime Player build. Keep such scripts in dedicated Editor assemblies either by placing them in a parent folder called Editor or creating an Editor-only assembly definition.  
See in [Glossary](Glossary.html#Editorscripts), use [`PlayerSettings.SetScriptingDefineSymbols`](../ScriptReference/PlayerSettings.SetScriptingDefineSymbols.html). This is the code equivalent of configuring platform-specific scripting symbols in the [Player settings](#player-settings).

**Important**: Symbols created from code with `SetScriptingDefineSymbols` don’t take effect until the Editor regains control and recompiles your scripts. For example, if you create scripting symbols with `SetScriptingDefineSymbols` in an Editor script and then call `BuildPipeline.BuildPlayer` on the next line, the new symbols created in the previous line won’t be in effect yet. In this case any Editor code that runs as part of the `BuildPlayer` execution runs without the new symbols and the Player might not build as intended.

### Custom symbols in batch mode

When the Editor runs in batch mode, there’s no mechanism to trigger recompilation of scripts. If you need specific symbols to be defined in an Editor running in batch mode, they must be in place from startup [using a csc.rsp asset file](#asset).

## Scripting symbol inheritance

If you define custom scripting symbols in several places, Unity adds together all the symbols that apply for the current build configuration. Symbols are inherited from each scope rather than overwritten, as follows: Project-wide symbols (from `csc.rsp`) + Platform-specific symbols (from Player settings) + Build profile symbols (from Build Data). Platform and build profile symbols are only included if they match the active build profile.

For example, assume your project has the following custom scripting symbols defined in the following locations:

| **Location** | **Symbols defined** |
| --- | --- |
| `csc.rsp` | `SYMBOL_A` |
| Windows Player Settings | `SYMBOL_B` |
| WindowsBuildProfile1 | `SYMBOL_C` |
| WindowsBuildProfile2 | `SYMBOL_D` |

Given this example configuration, the following table shows which symbols are active for your Editor and Player code when different build profiles are active:

| **Active build profile** | **Active symbols** |
| --- | --- |
| Android | `SYMBOL_A` |
| Windows | `SYMBOL_A`, `SYMBOL_B` |
| WindowsBuildProfile1 | `SYMBOL_A`, `SYMBOL_B`, `SYMBOL_C` |
| WindowsBuildProfile2 | `SYMBOL_A`, `SYMBOL_B`, `SYMBOL_D` |

You can test this behavior with `#if` directives in your code. For more information, refer to [Test conditional compilation](test-conditional-compilation.html).

## Additional resources

* [Unity scripting symbol reference](scripting-symbol-reference.html)
* [Referencing additional class library assemblies](dotnet-profile-assemblies.html)

Unity scripting symbol reference

Test conditional compilation

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)