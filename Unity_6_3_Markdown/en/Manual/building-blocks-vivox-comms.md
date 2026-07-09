* [Unity Building Blocks](building-blocks.html)
* [Vivox voice and text chat Building Block](building-blocks-vivox.html)
* Vivox Building Block

Vivox Building Block prerequisites

Unity Editor interface

# Vivox Building Block

Integrate voice and text chat into your project with this Building Block’s pre-made UI elements. Learn what Vivox channels are, how to connect players to them, and how to build chat and roster interfaces from the included components.

## Introduction

This Building Block helps you integrate Vivox into your project to connect players with voice and text chat. It can serve as a starting point for communication features in your multiplayer project, or dropped into an existing project to quickly add voice and chat throughout development.

This Building Block demonstrates how to do the following:

* Join a Vivox voice and/or text channel.
* Select and configure audio input and output devices.
* Display a live channel roster with speaking indicators and mute controls.
* Send and receive text chat messages in a channel.

The Building Block includes example **scenes**A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](CreatingScenes.html)  
See in [Glossary](Glossary.html#Scene), UI Toolkit assets, and runtime components ready to connect players through voice and text.

## Prerequisites

Before you start, make sure you meet the following prerequisites:

* Install the Vivox Building Block [from the Unity Asset Store](https://assetstore.unity.com/packages/slug/369502).
* [Link your Unity Editor project to a cloud project](https://docs.unity.com/en-us/cloud/projects/configure-project-for-unity-cloud).
* Enable the Vivox service in the Unity Dashboard for your project.
  + On the Unity Dashboard, project credentials are available under **Products** > **Vivox Voice and Text** > **Credentials**.
* In the Unity Editor, open the Vivox configuration menu at **Services** > **Vivox** > **Configure** and have your project’s credentials populate the **Environment Configuration** fields.
  + If a Unity project with Vivox credentials is correctly linked to the Editor but the Environment Configuration fields are not populating, entering and exiting Play mode is a secondary way to force credentials to update.

## Initial setup

Validate the Building Block is installed correctly by opening the [included](#included-resources) `RosterWithVoiceAndText` scene under **Assets** > **Blocks** > **Vivox** > **Scenes**.

1. Click **Play** to enter Play mode.
2. Enter a display name and channel name, then select **Join Channel** to connect.
3. The channel roster now populates, and is able to send and receive text chat messages.

## Vivox channels

A Vivox channel is a shared voice and text communication space that players connect to by name. Players who join the same channel name using the same Unity project credentials can hear and chat with each other. Channels are scoped to your project, the same channel name used in a different project creates an entirely separate space with no connection between them.

Channels are lightweight, they don’t require a host, dedicated server, or session, making them easy to use in any multiplayer setup.

Channels are independent of gameplay synchronization. They work alongside Netcode for **GameObjects**The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](class-GameObject.html)  
See in [Glossary](Glossary.html#GameObject), Netcode for Entities, or any other **networking**The Unity system that enables multiplayer gaming across a computer network. [More info](multiplayer.html)  
See in [Glossary](Glossary.html#networking) solution. A typical connection flow looks like the following:

1. Initialize Unity Services.
2. Authenticate the player.
3. Connect to the game network (for example, using [Multiplayer Sessions](https://docs.unity.com/en-us/mps-sdk/sessions)).
4. Join a Vivox channel.
5. Load the gameplay scene.

## Included resources

| **Scene** | **Description** |
| --- | --- |
| `RosterWithVoiceAndText` | A combined view showing the channel join form, a live roster of connected players with speaking indicators and mute controls, and a text chat panel. Configured by default with `ChatSettings_Group` for a standard group voice and text channel. |
| `AudioDeviceSelector` | A standalone audio configuration panel for selecting input and output devices and adjusting their volumes. |

### `RosterWithVoiceAndText`

This scene demonstrates the core Vivox features, a live channel roster with speaking indicators and mute controls, and a text chat panel. A basic join form is included to get players into a channel during prototyping or testing. In a shipped game, replace the connection flow with your own.

`ChannelRoster` UXML:

* `ChannelName`: Displays the name of the currently joined channel.
* `PlayerCountLabel`: Displays the number of participants in the channel.
* `RosterList`: Scrollable list of participants. Each entry shows the player’s display name, a speaking indicator that animates when the player is transmitting audio, and a mute toggle. The mute toggle is visible only when the local user is connected to audio.
* `CopyChannelName`: Displays and copies the current channel name so other players can join.

`TextChat` UXML:

* `MessageLog`: Scrollable history of text messages sent in the channel.
* `MessageInput`: Text field for composing a message.
* `SendButton`: Sends the composed message to the channel.

`JoinChannelMenu` UXML (Used for prototyping and testing only):

* `PlayerName`: Text field for the player’s display name.
* `ChannelName`: Text field for the channel name to join.
* `JoinRoom`: Joins the specified channel, handling Vivox login automatically.

**Note**: The roster and text chat components aren’t dependent on `JoinChannelMenu`. These components listen for the first active Vivox channel and populate automatically, whether that channel was already joined when the components loaded or joined afterward. You can replace or remove `JoinChannelMenu` entirely, and the roster and text chat continue to work with any channel your game joins through the Vivox SDK.

### `AudioDeviceSelector`

`AudioDeviceSelector` has multiple settings available to manage input and output devices.

* `InputDeviceDropdown`: Lists available microphone input devices. Selecting one sets it as the active input device.
* `InputVolumeSlider`: Adjusts microphone input volume. Uses an audio taper curve for natural-feeling control.
* `OutputDeviceDropdown`: Lists available audio output devices. Selecting one sets it as the active output device.
* `OutputVolumeSlider`: Adjusts speaker output volume. Uses an audio taper curve for natural-feeling control.

## Joining with multiple clients locally

Use [Multiplayer Play Mode](https://docs.unity3d.com/Packages/com.unity.multiplayer.playmode@latest) to test with multiple players directly from the Unity Editor.

## Troubleshooting

### Multiplayer Services not available

Unity Services Core must be initialized before Vivox can function. Add the `VivoxServiceInitializer` **prefab**An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](Prefabs.html)  
See in [Glossary](Glossary.html#prefab) to your scene for a zero-configuration setup. The prefab includes `ServicesInitialization`, `PlayerAuthentication`, and Vivox initialization in a single GameObject. Alternatively, add `ServicesInitialization` and `PlayerAuthentication` components individually to your own initialization GameObject.

### Authentication failure

Ensure the Editor is signed in and the correct Project ID is set in **Project Settings** > **Services**. Confirm service enablement in the Unity Dashboard under Authentication and Vivox.

### Can’t join a channel

Verify network connectivity. Confirm Vivox is enabled and your project is linked. Check that the player display name and channel name fields are not empty.

### Players can’t hear or see each other despite joining the same channel name

Confirm that all clients are linked to the same Unity cloud project. Vivox channels are scoped to project credentials, the same channel name in two different projects creates two separate channels with no connection between them.

### No audio after joining

Check that the expected input and output devices are selected using the audio device selector. Ensure the application has microphone permission on the target platform.

### Mute button not visible for a participant

The mute button is only shown when both the target participant and the local user are connected to audio. If the local user is connected as text-only, mute controls are hidden.

### UI not showing channel data

Confirm your root UXML element has the correct ChannelSettings asset set as its Data Source in the UI Builder. Refer to the [Configuration](building-blocks-vivox-prerequisites.html#channelsettings-scriptableobject-and-uxml-binding) section for details.

## Additional resources

* [Unity Services: Vivox Unity SDK](https://docs.unity.com/ugs/en-us/manual/vivox-unity/manual/Unity/Unity)
* [UI Toolkit](https://docs.unity3d.com/Manual/UIElements.html)
* [Unity Authentication](https://docs.unity.com/ugs/en-us/manual/authentication/manual/get-started)

Vivox Building Block prerequisites

Unity Editor interface

Copyright ©2005-2026 Unity Technologies. All rights reserved. Built from job ID 71188284. Built on: 2026-07-07.

[Tutorials](https://learn.unity.com/)[Community Answers](https://answers.unity3d.com)[Knowledge Base](https://support.unity3d.com/hc/en-us)[Forums](https://forum.unity3d.com)[Asset Store](https://unity3d.com/asset-store)[Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)[Legal](https://unity.com/legal)[Privacy Policy](https://unity.com/legal/privacy-policy)[Cookies](https://unity.com/legal/cookie-policy)[Do Not Sell or Share My Personal Information](https://unity.com/legal/do-not-sell-my-personal-information)

[Your Privacy Choices (Cookie Settings)](javascript:void(0);)