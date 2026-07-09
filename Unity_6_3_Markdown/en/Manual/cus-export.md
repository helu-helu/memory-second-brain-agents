* [Packages and package management](PackagesList.html)
* [Package creation](cus-pkg-lp.html)
* Export and sign your UPM package

Document your package

Share your package

# Export and sign your UPM package

Export and sign your Unity Package Manager (UPM) package so you can share it with others.

Starting with Unity 6.3, publishers can sign their package directly from the Package Manager window.

When you sign a package, you must associate it with one of your organizations, so package consumers can quickly determine who created and owns it.

The only packages you can sign are packages that have the **Custom** or **Local** label in the Package Manager window:

* A **Custom** label appears on packages you’re developing or customizing in the `Packages` folder of your project.
* A **Local** label appears on packages you installed with the Package Manager’s [Install package from disk](upm-ui-local.html) method, or package folders you [reference as dependencies](upm-localpath.html) in your [project manifest file](upm-manifestPrj.html).

**Note:** You can use methods other than the Package Manager window to pack and sign your packages. For a full list of methods, refer to [Methods for signing packages](upm-sign-methods.html).

## Sign a package from the Package Manager window

To sign a package from the Package Manager window:

1. Make sure you’re signed in to the Unity Hub.
2. Open the **Package Manager** Window.
3. Select the package you want to sign.
4. Select **Export**.

   ![The Package Manager window with the Export button for an editable package](../uploads/Main/upm-ui-export.png)


   The Package Manager window with the Export button for an editable package

   **Note**: Another way to access the export dialog is with the menus. Go to the **Project** window and select the base folder for your package in the `Packages` folder. Open the **Assets** menu (or right-click your package folder) and select **Export As **UPM Package**A **Package** managed by the **Unity Package Manager**. Refer to **Packages**.  
   See in [Glossary](Glossary.html#UPMpackage)**.
5. In the **Export Package** dialog that appears, open the **Authoring Org** menu and select the organization you want to associate this package with.

   **Note**: For large projects whose contributors span multiple organizations, be sure to select the wider organization (or company-wide organization). If that organization doesn’t exist yet, refer to [Considerations for companies with multiple organizations](upm-signature.html#multi-org).
6. Select a location to store the signed package and select **Select Folder** (Windows) or **Choose** (macOS).

   **Note**: If the package already exists in that location, a warning message prompts you to confirm overwriting the file.
7. When the export process completes, your file management application opens at the location you specified, showing you the newly created file. A confirmation message also displays in the **Console** window.

The export operation creates a tarball file (`.tgz`), which is a compressed archive file. This tarball file contains an encrypted file (`.attestation.p7m`), which contains the package signature.

Refer to [Share your package](cus-share.html) for information about distributing this tarball file to others.

## Additional resources

* [Package signatures](upm-signature.html)
* [Share your package](cus-share.html)
* [Methods for signing packages](upm-sign-methods.html)
* [Create and export asset packages](AssetPackagesCreate.html)

Document your package

Share your package

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)