* [Platform development](PlatformSpecific.html)
* [Cross-platform features and considerations](cross-platform-features.html)
* [Device Simulator](device-simulator.html)
* Extending the device simulator

Adding a device

Android

# Extending the device simulator

The Device Simulator supports plugins to extend its functionality and change the UI of the Control Panel in the Simulator view.

## Creating a plugin

To create a Device Simulator plugin, extend the [DeviceSimulatorPlugin](../ScriptReference/DeviceSimulation.DeviceSimulatorPlugin.html) class.

To insert UI into the Device Simulator view, your plugin must:

* Override the `title` property to return a non-empty string.
* Override the `OnCreateUI` method to return a [VisualElement](../ScriptReference/UIElements.VisualElement.html) that contains the UI.

If your plugin doesn’t meet these conditions, the Device Simulator instantiates the plugin but doesn’t display its UI in the Simulator view.

The following example demonstrates how to create a plugin that overrides the title property and adds UI to the Simulator view.

```
public class TouchInfoPlugin : DeviceSimulatorPlugin
{
    public override string title => "Touch Info";
    private Label m_TouchCountLabel;
    private Label m_LastTouchEvent;
    private Button m_ResetCountButton;

    [SerializeField]
    private int m_TouchCount = 0;

    public override void OnCreate()
    {
        deviceSimulator.touchScreenInput += touchEvent =>
        {
            m_TouchCount += 1;
            UpdateTouchCounterText();
            m_LastTouchEvent.text = $"Last touch event: {touchEvent.phase.ToString()}";
        };
    }

    public override VisualElement OnCreateUI()
    {
        VisualElement root = new VisualElement();
        
        m_LastTouchEvent = new Label("Last touch event: None");
        
        m_TouchCountLabel = new Label();
        UpdateTouchCounterText();

        m_ResetCountButton = new Button {text = "Reset Count" };
        m_ResetCountButton.clicked += () =>
        {
            m_TouchCount = 0;
            UpdateTouchCounterText();
        };

        root.Add(m_LastTouchEvent);
        root.Add(m_TouchCountLabel);
        root.Add(m_ResetCountButton);
            
        return root;
    }

    private void UpdateTouchCounterText()
    {
        if (m_TouchCount > 0)
            m_TouchCountLabel.text = $"Touches recorded: {m_TouchCount}";
        else
            m_TouchCountLabel.text = "No taps recorded";
    }
}
```

Adding a device

Android

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)