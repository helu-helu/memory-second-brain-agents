* [Programming in Unity](scripting.html)
* [Code optimization](scripting-optimization.html)
* Asynchronous programming with the Awaitable class

Unity programming best practices

Introduction to asynchronous programming with Awaitable

# Asynchronous programming with the Awaitable class

Asynchronous programming allows your code to perform long-running tasks without blocking the main thread. This allows your application to remain responsive and perform other tasks while it waits for an asynchronous task to complete.

Unity supports a simplified asynchronous programming model using the .NET [async](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/async) key word and [await](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/await) operator.

Before reading about asynchronous programming in Unity, make sure you understand the fundamental elements of asynchronous programming in .NET. For important context, refer to [Asynchronous programming with async and await](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/) and [Task asynchronous programming model](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/task-asynchronous-programming-model).

| **Topic** | **Description** |
| --- | --- |
| [Introduction to Awaitable](async-awaitable-introduction.html) | Understand the key features of Unity’s `Awaitable` and how it compares to both .NET `Task` and iterator-based coroutines. |
| [Awaitable completion and continuation](async-awaitable-continuations.html) | Understand how asynchronous code resumes on completion of an awaited task and how this affects the function and performance of your application. |
| [Awaitable code example reference](async-awaitable-examples.html) | Solve common asynchronous programming problems with a reference of `Awaitable` code examples. |

## Additional resources

* [Awaitable API reference](../ScriptReference/Awaitable.html)
* [C# Job System](job-system.html)
* [Coroutines](Coroutines.html)

Unity programming best practices

Introduction to asynchronous programming with Awaitable

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)