* [Programming in Unity](scripting.html)
* [Get started with programming in Unity](scripting-get-started.html)
* Introduction to programming in Unity

Get started with programming in Unity

Creating scripts

# Introduction to programming in Unity

Unity is customizable and extensible by design and almost everything is scriptable to some extent. Many items you can configure through the various [Editor views](unity-editor.html) have a corresponding public C# class representation that you can interact with in code.

You can use Editor APIs to customize and extend the Editor authoring tools to improve your development workflows. You can use Engine APIs to define the runtime functionality of your application, including graphics, physics, character behavior, and responses to user input.

The [Scripting API reference](../ScriptReference/index.html) provides the complete and authoritative reference for all public Unity APIs. The Manual provides additional context and guidance.

## The Unity scripting environment

Unity supports scripting in the C# programming language. C# (pronounced C-sharp) is a managed, object-oriented programming language, which is part of the .NET platform and runs in the cross-platform .NET runtime. Other .NET languages can be used with Unity if they can compile a compatible DLL, refer to [Managed plugins](plug-ins-managed.html) for further details.

The scripting environment refers to both:

* Your own local environment or context in which you’re writing code. This includes your code editor (IDE) and integrated source control solution and operating system.
* The C# scripting enviroment Unity provides. A given version of Unity supports given versions of the .NET platform, which determines the .NET libraries you can use in your code.

For more information on the scripting environment and tools, refer to [Environment and tools](environment-and-tools.html).

## How scripting in Unity works

C# scripts (files with a `.cs` file extension) are [assets](AssetWorkflow.html)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](AssetWorkflow.html)  
See in [Glossary](Glossary.html#asset) in your project, stored in the `Assets` folder and saved as part of the [asset database](AssetDatabase.html). You can create template scripts that derive from the common [built-in Unity types](fundamental-unity-types.html) through the **Scripting** submenu of the **Assets > Create** menu.

You configure a default [External Script Editor](preferences-external-tools.html), which is the program Unity opens your script assets in for editing. Usually this will be one of the [supported IDEs](scripting-ide-support.html) for Unity development.

You can create your own regular C# types and logic to use in your game, as long as the code you write is compatible with the active [.NET profile](dotnet-profile-support.html). But your scripted types gain additional functionality in Unity when they inherit from a built-in Unity type.

If your custom types inherit from [UnityEngine.Object](class-Object.html), they’ll be assignable to fields in the **Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector) window. Inheriting from [MonoBehaviour](class-MonoBehaviour.html) allows a script to be attached to a **GameObject**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject) as a component to control the behaviour of a GameObject in a **scene**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene).

For more information on fundamental Unity types you can inherit from, refer to [Fundamental Unity types](fundamental-unity-types.html).

For more information on viewing **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) and editing script components in the Inspector, refer to [Inspecting scripts](inspecting-scripts.html).

## Editor and runtime scripts

There are two distinct contexts in which your code might run:

* In the Unity Editor at authoring time, usually as part of custom editing tools and windows that support your own development process.
* In your application at runtime, as part of your user’s experience.

Source files that contain Editor-only code are commonly referred to as **Editor scripts**C# source files composed entirely of code that runs in the Unity Editor only and not in the runtime Player build. Keep such scripts in dedicated Editor assemblies either by placing them in a parent folder called Editor or creating an Editor-only assembly definition.  
See in [Glossary](Glossary.html#Editorscripts) and can be excluded from Player builds either by placing them in folders named `Editor` or by using [assembly definition files](assembly-definition-files.html) to define Editor-only assemblies. For more information, refer to [Editor folder](assembly-definitions-intro.html#special-folders).

Regions of code can also be conditionally compiled for Editor-only use with the `#if UNITY_EDITOR` preprocessor directive. For more information, refer to [Conditional compilation](conditional-compilation.html).

The majority of Unity’s core public APIs are in either the `UnityEditor` or `UnityEngine` namespaces. APIs in the `UnityEditor` namespace are only available in the Editor and attempting to use them in runtime code produces compilation errors.

While working in the Editor, you might have some code that you want to run in both Edit mode and Play mode. You might call some `UnityEditor` APIs while in Play mode for the purposes of testing, visualization, or triggering asset operations. Likewise, you might want to call `UnityEngine` APIs in Edit mode by using [`[ExecuteInEditMode]`](../ScriptReference/ExecuteInEditMode.html) or [`[ExecuteAlways]`](../ScriptReference/ExecuteAlways.html) attributes on those sections of code.

However, always remember to exclude Editor scripts and code that uses `UnityEditor` APIs from your runtime Player builds.

## Compilation and code reload

[Compilation](script-compilation.html) transforms the C# code you write into code that runs on a given target platform. Some aspects of compilation are under your control and others aren’t. By [organizing your scripts into assemblies](assembly-definition-files.html) you can reduce unnecessary recompilation and manage your dependencies effectively. With [conditional compilation](conditional-compilation.html) you can selectively include or exclude sections of your code from compilation.

Depending on your settings, Unity [recompiles and reloads your code](compilation-and-code-reload.html) in various contexts. Reloading code is important for changes to take effect or to preserve state when transitioning between Edit mode and Play mode, but it also impacts performance and iteration times. It’s important to understand these costs and how you can configure Unity’s code reload behavior to mitigate them.

## Additional resources

* [Creating scripts](creating-scripts.html)
* [Naming scripts](naming-scripts.html)
* [Scripts in the Inspector window](inspecting-scripts.html)
* [Fundamental Unity types](fundamental-unity-types.html)

Get started with programming in Unity

Creating scripts

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)