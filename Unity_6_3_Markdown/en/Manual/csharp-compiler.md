* [Programming in Unity](scripting.html)
* [Environment and tools](environment-and-tools.html)
* [Unity .NET features](overview-of-dot-net-in-unity.html)
* C# compiler and language version reference

Add class library references to .NET Framework

Object-oriented development

# C# compiler and language version reference

This version of the Unity Editor uses the following C# compiler and language version:

* **C# compiler**: [Roslyn](https://github.com/dotnet/roslyn)
* **C# language version**: [C# 9.0](https://docs.microsoft.com/en-us/dotnet/csharp/whats-new/csharp-9)

The Editor passes a default set of options to the C# compiler. To pass additional options in your project, refer to [Conditional compilation in Unity](platform-dependent-compilation.html).

## Garbage collection

Unity uses the [Boehm-Demers-Weiser garbage collector](https://www.hboehm.info/gc/) for both the Mono and **IL2CPP**A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](./scripting-backends-il2cpp.html)  
See in [Glossary](Glossary.html#IL2CPP) [scripting backends](scripting-backends.html)A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](scripting-backends.html)  
See in [Glossary](Glossary.html#ScriptingBackend) and incremental mode by default. For more information on the available garbage collection modes, their meaning, and how to switch between them, refer to [Garbage collection modes](performance-incremental-garbage-collection.html).

## Unsupported features

### C# 9.0

* Suppress emitting localsinit flag
* Covariant return types
* Module Initializers
* Extensible calling conventions for unmanaged function pointers
* Init only setters

If you try to use unsupported features in your project, compilation generates errors.

### Record support

C# 9 init and record support comes with a few caveats.

* The type `System.Runtime.CompilerServices.IsExternalInit` is required for full record support as it uses init only setters, but is only available in .NET 5 and later (which Unity doesn’t support). Users can work around this issue by declaring the `System.Runtime.CompilerServices.IsExternalInit` type in their own projects.
* You shouldn’t use C# records in serialized types because Unity’s serialization system doesn’t support C# records.

### Unmanaged function pointer support

Unity supports unmanaged functions pointers as introduced in C# 9, but it doesn’t support extensible calling conventions. The following example code provides more detailed information about how to correctly use unmanaged function pointers.

The following example targets Windows platforms and requires **Allow ‘unsafe’ Code** to be enabled in the [Player Settings](class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](class-PlayerSettings.html)  
See in [Glossary](Glossary.html#PlayerSettings). To enable it, go to: **Project Settings** > **Player**. Expand the **Other Settings** panel, navigate to the **Script Compilation** section. For more information on C#’s `unsafe` context, refer to [Microsoft’s unsafe (C# Reference) documentation](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/unsafe) or [Microsoft’s Unsafe code, pointer types, and function pointers documentation](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/unsafe-code).

```
using System;
using System.Runtime.InteropServices;
using UnityEngine;

public class UnmanagedFunctionPointers : MonoBehaviour
{
  [DllImport("kernel32.dll")]
  static extern IntPtr LoadLibrary(string lpLibFileName);
  
  [DllImport("kernel32.dll")]
  static extern IntPtr GetProcAddress(IntPtr hModule, string lpProcName);
  
  // You must enable "Allow 'unsafe' code" in the Player Settings
  unsafe void Start()
  {
#if UNITY_EDITOR_WIN || UNITY_STANDALONE_WIN
    // This example is only valid on Windows
    
    // Get a pointer to an unmanaged function
    IntPtr kernel32 = LoadLibrary("kernel32.dll");
    IntPtr getCurrentThreadId = GetProcAddress(kernel32, "GetCurrentThreadId");

    // The unmanaged calling convention
    delegate* unmanaged[Stdcall]<UInt32> getCurrentThreadIdUnmanagedStdcall = (delegate* unmanaged[Stdcall]<UInt32>)getCurrentThreadId;
    Debug.Log(getCurrentThreadIdUnmanagedStdcall());
#endif
  }
}
```

## Additional resources

* [API compatibility levels for .NET](dotnet-profile-support.html).
* [Platform dependent compilation](platform-dependent-compilation.html).

Add class library references to .NET Framework

Object-oriented development

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)