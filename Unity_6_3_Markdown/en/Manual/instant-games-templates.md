* [Platform development](PlatformSpecific.html)
* [Web](webgl.html)
* [Facebook Instant Games](instant-games.html)
* Facebook Instant Games templates

Facebook Instant Games setup process

Upload to Facebook Instant Games

# Facebook Instant Games templates

Load required settings for Facebook Instant Games and customize the appearance of the HTML page that hosts your Web player.

The default templates for Facebook Instant Games have the same structure and functionality as the [Web templates](webgl-templates.html) but are tailored for the Facebook Instant Games environment. There are separate templates for portrait and landscape orientations. They also include the required `fbapp-config.json` file necessary for uploading to Facebook Instant Games.

**Note:** The HTML templates include a Facebook SDK script tag comment. If you edit the templates, leave in the comment. While the [Facebook Instant Games SDK for Unity package](https://docs.unity3d.com/Packages/com.unity.meta-instant-games-sdk@latest?subfolder=/manual/index.html) automatically downloads and initializes the Facebook Instant Games SDK, the comment is still required for a successful upload.

## Facebook Instant Games configuration file

The `fbapp-config.json` file stores Facebook Instant Games configuration values including orientation, play configuration, and custom template variables.

When you [make custom templates](web-templates-add.html), you can modify settings in the configuration file to customize your game. For example, you can configure the template to send out custom updates.

Refer to [Facebook’s Bundle Configuration Reference documentation](https://developers.facebook.com/docs/games/build/instant-games/reference/bundle-config) for examples of customizations and more information about the configuration file.

## Additional resources

* [Using Web templates](web-templates-intro.html)
* [Web template variables](web-templates-variables.html)
* [Web template structure and instantiation](web-templates-structure.html)
* [Web template build configuration and interaction](web-templates-build-configuration.html)
* [Upload to Facebook Instant Games](instant-games-upload.html)

Facebook Instant Games setup process

Upload to Facebook Instant Games

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)