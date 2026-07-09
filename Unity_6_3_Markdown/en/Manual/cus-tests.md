* [Packages and package management](PackagesList.html)
* [Package creation](cus-pkg-lp.html)
* [Package development](cus-pkg-development.html)
* Add tests to your package

Create samples for your package

Package versioning

# Add tests to your package

Add tests to your Unity Package Manager (UPM) package to verify its behavior and identify issues during development.

Adding tests is relevant if you’re creating a package that contains **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts) or logic you want to validate as your package evolves. Including tests helps you catch bugs, improve reliability, and support safe reuse of the package across projects. Unity’s test framework lets you organize and run these tests from within the Unity Editor or as part of your continuous integration (CI) pipeline.

When you [create your package](cus-create.html) with the Package Manager window, Package Manager creates `Tests/Editor` and `Tests/Runtime` folders with C# and assembly definition (`.asmdef`) files in each, to help you get started.

To complete the test files for your package:

1. Go to your package folder, either by using the **Project** window or your file management application.
2. Go to the `Tests/Editor` or `Tests/Runtime` folder for the tests you want to complete.
3. Open the sample C# script.
4. Add test cases as needed. A good practice is to create at least one test file for each C# script. Refer to [Writing tests](test-framework/writing-tests.html).
5. Save your file.
6. If you create a more elaborate folder structure in your `Tests` folder, you can optionally create additional `asmdef` files for the code you want to put in separate assemblies. If you choose to create additional assembly definitions, refer to [Assembly definition files for tests](#files).
7. [Enable tests](#tests) for your package.
8. Run your tests. For more information, refer to [Running tests](test-framework/running-tests.html).

## Assembly definition files for tests

Use the [Test Framework](test-framework/test-framework-introduction.html)The Test Framework package (formerly called the Test Runner) is a Unity tool that tests your code in both Edit mode and Play mode, and also on target platforms such as Standalone, Android, or iOS. [More info](https://docs.unity3d.com/Packages/com.unity.test-framework@latest)  
See in [Glossary](Glossary.html#TestFramework) to create or edit your assembly definition files. For more information, refer to [Create a test assembly](test-framework/workflow-create-test-assembly.html).

When you [create your package](cus-create.html) with the Package Manager window, Package Manager creates assembly definition files (`.asmdef`) in `Tests/Editor` and `Tests/Runtime` to accompany the test scripts it created in those folders.

The sample assembly definition files have the required properties and values. If you want to add optional properties and values, use the ****Inspector**A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](UsingTheInspector.html)  
See in [Glossary](Glossary.html#Inspector)** window to edit the assembly definitions. For more information, refer to [Assembly Definition properties reference](class-AssemblyDefinitionImporter.html).

You can also edit `.asmdef` files directly, but this method is more error prone. For more information, refer to [Assembly Definition File Format reference](assembly-definition-file-format.html).

### Editor file example

The `.asmdef` file in the `Tests/Editor` folder looks like this:

```
{
  "name": "MyCompany.MyPackage.Editor.Tests",
  "references": [
    "MyPackage.Editor",
    "MyPackage"
  ],
  "optionalUnityReferences": [
    "TestAssemblies"
  ],
  "includePlatforms": [
    "Editor"
  ],
  "excludePlatforms": []
}
```

### Runtime file example

The `.asmdef` file in the `Tests/Runtime` folder looks like this:

```
{
  "name": "MyCompany.MyPackage.Tests",
  "references": [
    "MyPackage"
  ],
  "optionalUnityReferences": [
    "TestAssemblies"
  ],
  "includePlatforms": [],
  "excludePlatforms": []
}
```

## Enable tests for a package

You might need to enable tests depending on the folder where you’re developing your package.

If you’re developing your package in the `Packages` folder of your project, you don’t need to explicitly enable tests.

However, if you’re developing a package outside the project’s `Packages` folder, you need to manually enable its tests. To do this, add the [testables](upm-manifestPrj.html#testables) property to your **project manifest**Each Unity project has a *project manifest*, which acts as an entry point for the Package Manager. This file must be available in the `<project>/Packages` directory. The Package Manager uses it to configure many things, including a list of dependencies for that project, as well as any package repository to query for packages. [More info](upm-manifestPrj.html)  
See in [Glossary](Glossary.html#projectmanifest) and list the packages whose tests you want to run. If you also want to run tests from packages they depend on, include those **indirect dependencies**An **indirect**, or transitive dependency occurs when your project requests a package which itself “depends on” another package. For example, if your project depends on the `alembic@1.0.7` package which in turn depends on the `timeline@1.0.0` package, then your project has an direct dependency on Alembic and an indirect dependency on Timeline. [More info](upm-dependencies.html)  
See in [Glossary](Glossary.html#indirectdependency) as well. For example:

```
{
  "dependencies": {
    "com.unity.some-package": "1.0.0",
    "com.unity.other-package": "2.0.0",
    "com.unity.yet-another-package": "3.0.0"
  },
  "testables": ["com.unity.some-package", "com.unity.other-package"]
}
```

This example adds tests for the `com.unity.some-package` and `com.unity.other-package` packages in Unity’s [Test Framework](test-framework/test-framework-introduction.html) package.

## Additional resources

* [Testing your code](test-framework/test-framework-introduction.html)
* [Organizing scripts into assemblies](assembly-definition-files.html)
* [Assembly Definition properties reference](class-AssemblyDefinitionImporter.html)
* [Comparison of package creation locations](cus-location.html)
* [Package dependency and resolution](upm-dependencies.html)

Create samples for your package

Package versioning

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)