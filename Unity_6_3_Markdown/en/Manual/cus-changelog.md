* [Packages and package management](PackagesList.html)
* [Package creation](cus-pkg-lp.html)
* [Package development](cus-pkg-development.html)
* Update the package changelog

Package versioning

Add required legal files to your package

# Update the package changelog

Update the changelog file (`CHANGELOG.md`) each time you publish a new version of your package.

Use the changelog to summarize new features, major fixes, and significant changes in each release. The changelog explains to users what’s changed between versions to help them decide whether to upgrade.

Maintaining a changelog is optional for packages that you don’t share, but strongly recommended for packages you share or distribute. Users rely on this information to know which version best suits their needs.

When you [create your package](cus-create.html) using the Package Manager window, the Unity Editor creates the changelog file for you.

To update the changelog:

1. Open the `CHANGELOG.md` file in the base folder of your package.
2. Document key additions, fixes, and breaking changes. Aim for clarity so users understand what changed and why.
3. Save the file.
4. (Optional) Link to an external changelog. If you host the changelog on a website or repository, [edit the package manifest](cus-edit-manifest.html#edit-manifest) by adding a `changelogUrl` property. For example:

   ```
   "changelogUrl": "https://example.com/your-package/changelog"
   ```

For more information about changelogs, refer to the [Keep a Changelog](http://keepachangelog.com) documentation.

## Additional resources

* [Package development workflow](CustomPackages.html)

Package versioning

Add required legal files to your package

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)