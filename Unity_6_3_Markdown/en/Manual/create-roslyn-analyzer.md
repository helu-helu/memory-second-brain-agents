* [Programming in Unity](scripting.html)
* [Debugging and diagnostics](debugging-and-diagnostics.html)
* [Code analysis and source generation](roslyn-analyzers.html)
* Create and use a Roslyn analyzer

Create and use a source generator

Install and use an existing analyzer or source generator

# Create and use a Roslyn analyzer

You can use code analyzers to inspect your code for errors, rule violations, and coding style issues. As with source generators, you can use existing analyzers or create your own.

To create a Roslyn analyzer in your IDE and then apply it for use in your Unity project:

1. In your IDE, create a C# class library project that targets .NET Standard 2.0 and name the project `ExampleAnalyzer`.
2. Install the `Microsoft.CodeAnalysis.Csharp` NuGet package for the project. Your analyzer must use [Microsoft.CodeAnalysis.Csharp 4.3](https://www.nuget.org/packages/Microsoft.CodeAnalysis.CSharp/4.3.0) to work with Unity.
3. In your IDE project, create a new C# file and add the following code:

   ```
   using System.Collections.Immutable;
   using Microsoft.CodeAnalysis;
   using Microsoft.CodeAnalysis.CSharp;
   using Microsoft.CodeAnalysis.CSharp.Syntax;
   using Microsoft.CodeAnalysis.Diagnostics;

   namespace ExampleAnalyzer
   {
   [DiagnosticAnalyzer(LanguageNames.CSharp)]
   public class DebugLogAnalyzer : DiagnosticAnalyzer
   {
       public const string DiagnosticId = "EX0001";

       private static readonly LocalizableString Title =
           "Avoid using Debug.Log";

       private static readonly LocalizableString MessageFormat =
           "Debug.Log call detected - consider removing it before shipping";

       private static readonly LocalizableString Description =
           "Debug.Log calls can impact performance and clutter the console in production builds.";

       private const string Category = "Usage";

       private static readonly DiagnosticDescriptor Rule = new DiagnosticDescriptor(
           DiagnosticId,
           Title,
           MessageFormat,
           Category,
           DiagnosticSeverity.Warning,
           isEnabledByDefault: true,
           description: Description);

       public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics =>
           ImmutableArray.Create(Rule);

       public override void Initialize(AnalysisContext context)
       {
           context.ConfigureGeneratedCodeAnalysis(GeneratedCodeAnalysisFlags.None);
           context.EnableConcurrentExecution();
           context.RegisterSyntaxNodeAction(AnalyzeInvocation, SyntaxKind.InvocationExpression);
       }

       private static void AnalyzeInvocation(SyntaxNodeAnalysisContext context)
       {
           var invocation = (InvocationExpressionSyntax)context.Node;

           if (!(invocation.Expression is MemberAccessExpressionSyntax memberAccess))
               return;

           // Match calls where the method name is "Log"
           if (memberAccess.Name.Identifier.Text != "Log")
               return;

           // Verify the symbol belongs to UnityEngine.Debug
           var symbolInfo = context.SemanticModel.GetSymbolInfo(memberAccess);
           if (!(symbolInfo.Symbol is IMethodSymbol methodSymbol))
               return;

           var containingType = methodSymbol.ContainingType;
           if (containingType?.ToDisplayString() != "UnityEngine.Debug")
               return;

           var diagnostic = Diagnostic.Create(Rule, memberAccess.GetLocation());
           context.ReportDiagnostic(diagnostic);
       }
   }
      }
   ```
4. Build your analyzer with a **release** build configuration.
5. In your analyzer’s project folder, find the `bin/Release/netstandard2.0/ExampleAnalyzer.dll` file.
6. Copy this file into your Unity project, inside the `Assets` folder.
7. Inside the Asset Browser, click on the .dll file to open the [Plugin Inspector](plug-in-inspector.html) window.
8. Under **Select platforms for plugin**, uncheck **Any Platform**.
9. Under **Include Platforms**, uncheck **Editor** and **Standalone** and any other checked platforms.
10. Under **Asset Labels**, click on the label icon to open the Asset labels sub-menu.
11. Create and assign a new label called **RoslynAnalyzer**. To do this, type `RoslynAnalyzer` in the **text input field**A field that allows the user to input a Text string [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-InputField.html)  
    See in [Glossary](Glossary.html#TextInputField) of the Asset labels sub-menu and press Enter. This label must match exactly and is case sensitive. Once created, the label appears in the Asset labels sub-menu from then on. You can click on the name of the label in the menu to assign it to other analyzers.
12. To test the analyzer is working, [create a new MonoBehaviour script](creating-scripts.html) in the Editor with the following code:

    ```
    using UnityEngine;

    public class TestScript : MonoBehaviour
    {
        void Start()
        {
            Debug.Log("Hello world"); // Should trigger EX0001 warning
        }
    }
    ```

After Unity recompiles **scripts**A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](creating-scripts.html)  
See in [Glossary](Glossary.html#Scripts), the following warning appears in the Console:

```
TestScript.cs(8,9): warning EX0001: Debug.Log call detected - consider removing it before shipping
```

For more information on creating Roslyn analyzers, refer to [Tutorial: Write your first analyzer and code fix](https://learn.microsoft.com/en-us/dotnet/csharp/roslyn-sdk/tutorials/how-to-write-csharp-analyzer-code-fix) in the Microsoft documentation.

## Report analyzer diagnostics

To view information such as the total execution time of your analyzers and source generators or the relative execution times of each analyzer or source generator, go to **Edit** > **Preferences** (macOS: **Unity** > **Settings**) > **Editor Diagnostics** > **Core** and enable **EnableDomainReloadTimings**. When enabled, the information is displayed in the console window.

## Additional resources

* [Install and use an existing analyzer or source generator](install-existing-analyzer.html)
* [Create and use a source generator](create-source-generator.html)

Create and use a source generator

Install and use an existing analyzer or source generator

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)