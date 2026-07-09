* [Programming in Unity](scripting.html)
* [Environment and tools](environment-and-tools.html)
* [Unity .NET features](overview-of-dot-net-in-unity.html)
* Add class library references to .NET Framework

API compatibility levels for .NET

C# compiler and language version reference

# Add class library references to .NET Framework

By default, Unity references the following assemblies when your project uses the .NET Framework [API compatibility level](dotnet-profile-support.html):

* `mscorlib.dll`
* `System.dll`
* `System.Core.dll`
* `System.Runtime.Serialization.dll`
* `System.Xml.dll`
* `System.Xml.Linq.dll`

If your Unity project uses a part of the .NET class library API that Unity doesn’t compile by default, you can provide the C# compiler with a list of additional assemblies to reference during compilation.

## Prerequisites

* Your project’s [API compatibility level](dotnet-profile-support.html) must be set to .NET Framework. If your project targets .NET Standard, all parts of the .NET class library API that can be referenced are already referenced by default. To change the setting, in the Unity Editor go to **Edit** > **Project Settings**. In the **Player** tab, navigate to the **Other Settings** tab and in the **Configuration** section, set **Api Compatibility Level** to **.NET Framework**.

## Create a response file

To reference any other class library assemblies, you can create a [response](https://learn.microsoft.com/en-us/visualstudio/msbuild/msbuild-response-files?view=vs-2022) (.rsp) file with a list of command-line arguments to pass to the C# compiler as follows:

1. Create a file named `csc.rsp` in the `Assets` folder of your Unity project.
2. Move any assembly files you want to reference into the `Assets` folder of your project, if they aren’t already in this folder.
3. Populate the `csc.rsp` file with command-line arguments for the assemblies you want to reference.

For example, if your project uses the [`HttpClient`](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient?view=net-9.0) class, which is defined in the `System.Net.Http.dll` assembly, the C# compiler might produce this initial error message if the assembly isn’t present:

```
The type `HttpClient` is defined in an assembly that is not referenced. You must add a reference to assembly 'System.Net.Http, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a'.
```

To resolve this error, add a `csc.rsp` file that contains the following command-line argument to the project:

```
-r:System.Net.Http.dll
```

Add a new line with the appropriate command-line argument for each assembly you want to reference.

**Important**: If you change from .NET Framework to .NET Standard and your `csc.rsp` file references an assembly that doesn’t exist in .NET Standard, then compilation fails. To solve the issue, edit the `csc.rsp` file to remove any references to assemblies that are exclusive to the .NET Framework profile before you change to .NET Standard.

## Additional resources

* [.NET Profile Support](dotnet-profile-support.html).
* [Third-party .NET libraries](dotnet-third-party-libraries).

API compatibility levels for .NET

C# compiler and language version reference

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)