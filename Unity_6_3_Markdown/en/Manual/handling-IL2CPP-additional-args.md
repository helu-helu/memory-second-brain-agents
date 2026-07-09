* [Programming in Unity](scripting.html)
* [Compilation and code reload](compilation-and-code-reload.html)
* [Script compilation](script-compilation.html)
* [Scripting back ends](scripting-backends.html)
* [IL2CPP scripting back end](scripting-backends-il2cpp.html)
* Additional IL2CPP compiler arguments

IL2CPP managed stack traces

Linux IL2CPP cross-compiler

# Additional IL2CPP compiler arguments

You can provide additional arguments for the **IL2CPP**A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) compiler using the [`PlayerSettings.SetAdditionalIl2CppArgs`](../ScriptReference/PlayerSettings.SetAdditionalIl2CppArgs.html) API or by setting the `IL2CPP_ADDITIONAL_ARGS` environment variable.

**Warning**: Passing additional arguments to the IL2CPP compiler is an experimental feature for debugging and optimizing IL2CPP code generation in complex projects. Like [diagnostics switches](preferences-editor-diagnostics.html), it’s intended for use by advanced developers in coordination with Unity support staff. Arguments are passed directly to the C++ compiler with no interpretation, which means there is a high risk of breaking builds. Unity reserves the right to change or remove this feature without notice.

The following table displays the arguments you can use to provide additional flags to the IL2CPP compiler:

| **Argument** | **Description** |
| --- | --- |
| `--compiler-flags="<flags>"` | Passes additional flags to the C++ compiler. Replace `<flags>` with the desired flags. For example, `--compiler-flags=\"COMPILER_FLAG_1 COMPILER_FLAG_2\"` passes the compiler flags `COMPILER_FLAG_1` and `COMPILER_FLAG_2` to the C++ compiler. |
| `--linker-flags="<flags>"` | Passes additional flags to the linker. Replace `<flags>` with the desired flags. For example, `--linker-flags="\LINKER_FLAG_1 LINKER_FLAG_2\"` passes the linker flags `LINKER_FLAG_1` and `LINKER_FLAG_2` to the linker. |

Multiple arguments must be space separated as follows:

```
PlayerSettings.SetAdditionalIl2CppArgs("--compiler-flags=\"COMPILER_FLAG_1 COMPILER_FLAG_2\" --linker-flags="\LINKER_FLAG_1 LINKER_FLAG_2\"");
```

**Note**: Calling `SetAdditionalIl2CppArgs` more than once overwrites any flags provided previously. Pass an empty string to this method to remove any previously provided additional arguments.

Valid compiler and linker flags differ by platform, depending on which underlying C++ compiler (msvc or clang) IL2CPP uses on that platform. For a list of valid compiler and linker options, refer to the relevant third-party documentation for msvc [compiler](https://learn.microsoft.com/en-us/cpp/build/reference/compiler-options?view=msvc-170), [linker](https://learn.microsoft.com/en-us/cpp/build/reference/linker-options?view=msvc-170) options, or [clang compiler and linker](https://clang.llvm.org/docs/ClangCommandLineReference.html) options.

## Check if arguments are set

If your project has additional IL2CPP arguments set, then compiling for more than one platform might not work as expected, especially when [cross-compiling for Linux](linux-il2cpp-crosscompiler.html).

To check if any additional IL2CPP arguments are already set, do one of the following:

* Check if the environment variable `IL2CPP_ADDITIONAL_ARGS` is set.
* In `ProjectSettings/ProjectSettings.asset`, check if the Editor script has a value called `additionalIl2CppArgs`.

**Important**: Additional IL2CPP arguments are globally applied to all platforms, which can cause compilation issues if set for a platform other than the desired platform. Use the `IPreprocessBuildWithContext` hook to ensure IL2CPP arguments are set only for the platform that requires them.

### IPreprocessBuildWithContext hook

You can use the [`IPreprocessBuildWithContext`](../ScriptReference/Build.IPreprocessBuildWithContext.html) callback to build **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) or the Build dialog to set the additional arguments:

```
class MyCustomPreprocessBuild: IPreprocessBuildWithContext
{
    public int callbackOrder { get { return 0; } }
    public void OnPreprocessBuild(BuildCallbackContext ctx)
    {
        string addlArgs = "";
        if (ctx.Report.summary.platform == BuildTarget.StandaloneWindows || ctx.Report.summary.platform == BuildTarget.StandaloneWindows64)
            addlArgs = "--compiler-flags=\"d2ssa-cfg-jt\"";
        UnityEngine.Debug.Log($"Setting Additional IL2CPP Args = \"{addlArgs}\" for platform {report.summary.platform}");
        PlayerSettings.SetAdditionalIl2CppArgs(addlArgs);
    }
}
```

## Additional resources

* [Linux IL2CPP cross-compiler](linux-il2cpp-crosscompiler.html)
* [Managed stack traces](il2cpp-managed-stack-traces.html)
* [Discussions: How to add compiler or linker flags for IL2CPP invocation](https://discussions.unity.com/t/how-to-add-compiler-or-linker-flags-for-il2cpp-invocation/221183)

IL2CPP managed stack traces

Linux IL2CPP cross-compiler

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)