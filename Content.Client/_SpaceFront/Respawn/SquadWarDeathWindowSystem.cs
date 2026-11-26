using Content.Shared._SpaceFront.Respawn;
using Robust.Client.GameObjects;
using Robust.Client.UserInterface;
using Robust.Client.UserInterface.Controls;
using Robust.Client.UserInterface.CustomControls;
using Robust.Client.UserInterface;
using Robust.Shared.Network;

namespace Content.Client._SpaceFront.Respawn;

/// <summary>
/// Space Front: показывает неотключаемое окно смерти призрака с таймером.
/// Данные приходят в обычном RespawnResetEvent (поле DeathWindowSeconds).
/// </summary>
public sealed class SquadWarDeathWindowSystem : EntitySystem
{
    [Dependency] private readonly IUserInterfaceManager _ui = default!;

    private SquadWarDeathWindow? _window;

    public override void Initialize()
    {
        base.Initialize();
        SubscribeNetworkEvent<RespawnResetEvent>(OnRespawnReset);
    }

    private void OnRespawnReset(RespawnResetEvent msg)
    {
        if (msg.DeathWindowSeconds < 0)
        {
            _window?.Dispose();
            _window = null;
            return;
        }

        if (msg.DeathWindowSeconds <= 0)
            return; // обычный таймер возрождения — окно не трогаем

        if (_window == null)
        {
            _window = new SquadWarDeathWindow();
            _ui.RootControl.AddChild(_window);
            _window.SetPositionFirst(); // в самый низ: другие окна (роли призраков) поверх
            LayoutContainer.SetAnchorPreset(_window, LayoutContainer.LayoutPreset.Center);
        }

        _window.SecondsLeft = msg.DeathWindowSeconds;
        _window.UpdateTimer();
    }
}
