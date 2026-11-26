# Space Front — ERP Marines

Space Front — сборка [Space Station 14](https://spacestation14.com/) на основе [RMC-14](https://github.com/RMC-14/RMC-14) (по мотивам [CMSS13](https://github.com/cmss13-devs/cmss13)), работающая на [RobustToolbox](https://github.com/space-wizards/RobustToolbox). Основной режим — «Стенка на стенку»: два корабля «Алмаер» и четыре отряда морской пехоты, которые воюют друг с другом.

Как и в RMC-14, клиент и сервер загружают «контент-пак». Здесь лежат и движок, и контент: это нужный репозиторий, если вы хотите запустить сервер или доработать сборку.

**18+. Сборка содержит материалы для взрослых (ERP). Играть можно только с 18 лет.**

## Ссылки

[Discord](https://discord.gg/PhHV3EeZqs) | [RMC-14](https://github.com/RMC-14/RMC-14) | [Вики RMC-14](https://wiki.rouny-ss14.com/) | [Лаунчер SS14 (Steam)](https://store.steampowered.com/app/1255460/Space_Station_14/) | [Автономный лаунчер](https://spacestation14.io/about/nightlies/)

Сервер играет каждый день в 17:00 по Москве. Сервер виден в списке хаба лаунчера по тегам `ru`, `rp:med`.

## Особенности

### Режим SquadWar («Альфа-Браво против Дельта-Чарли»)
- Единственный режим сервера. Четыре отряда КМП США: А.Б. (Альфа и Браво) против Д.Ч. (Чарли и Дельта). Ксеносов, выживших и разведки нет.
- Два корабля «Алмаер» (`almayer_ab`, `almayer_dch`), у каждого свой шаттл «Аврора». Спавн строго на своём корабле.
- Отряды распределяются автоматически: по балансу кораблей, затем отрядов. Выбор отряда в настройках персонажа убран.
- Бой идёт на планете, зона высадки у каждой команды своя (АБ: ЗП1, ДЧ: ЗП2). Планету делит туман. Победившая команда захватывает планету и летит на вражеский «Алмаер».
- Штурм «Алмаера»: тревога и красный код при взлёте, автоэвакуация и подрыв реакторов после посадки.
- Концовки с удержанием 1 минуту: победа высадкой, победа эвакуацией противника, «команда уничтожена», ничья. Ничья также наступает, если 5 минут подряд нет живых игроков в обеих командах.
- Полёт шаттла длится ровно 300 секунд, навык пилота его не ускоряет.

### Правила игры
- Только люди. У всех максимальные навыки и полный доступ (кроме ВП и брига).
- Вендоры бесплатные, роли в карго стоят по 1$, у всех не меньше 45 очков КолМорТех.
- Радио: у каждой команды только свои два канала (АБ: A и B, ДЧ: C и D). Команды друг друга не слышат, трофейная гарнитура работает.
- Тактическая карта раздельная для каждого корабля, туман отмечен на ней серыми метками.
- Окно смерти призрака: 30 секунд, затем лобби.
- Окно правил показывается при каждом входе.
- Ванильное убрано: ЦК, аварийный шаттл, терминал прибытия, обучающие брошюры, ванильные крафты и рецепты.

### ERP и взаимодействия (18+)
- Система взаимодействий между персонажами, предметы ERP, ToysLeash и QueenCarry из сборки Wega (папки `_Wega`, русская локализация в `ru-RU/_spacefront/_wega`).
- Сервер играет на уровне MRP. ERP разрешено, входя на сервер, игрок подтверждает, что ему 18 лет и что он согласен с ERP (окно правил при входе).
- Уровень отыгрыша и правила поведения описаны в `Resources/ServerInfo/Guidebook/_SpaceFront/SpaceFrontRules.xml`.

### Озвучка (TTS)
- Озвучка чата, радио и объявлений через HTTP-API N/TTS (порт из сборки Space Stories). Ключ API задаётся в конфиге сервера, секция `[tts]`.
- Выбор голоса в редакторе персонажа: категории, поиск, случайный голос, предпрослушивание. Голос хранится в профиле.
- Брифинг в начале раунда озвучивается голосом АРЕС, записи кэшируются.
- Своя вкладка TTS в настройках: громкость для морпехов, радио и объявлений.
- Нельзя отправить новую реплику, пока играет озвучка предыдущей.

### Язык и интерфейс
- Полный русский перевод интерфейса, консолей, брифинга, карго, вендоров и осмотра.
- Своё оформление: иконка, заставка, название окна «Space Front - Marine Corps».
- Ограничение частоты сообщений в чате: 10 сообщений за 2 секунды на игрока.

Полный список изменений: [ИЗМЕНЕНИЯ.md](ИЗМЕНЕНИЯ.md). Реестр правок чужих файлов: [PATCHES.md](PATCHES.md). Каталог модификаций по папкам: [Modifications](Modifications).

## Структура репозитория

- Весь собственный код и ресурсы лежат в папках `_SpaceFront` (`Content.Server`, `Content.Shared`, `Content.Client`, `Resources/Prototypes`, `Resources/Maps`, `Resources/Textures`, `Resources/Audio`, `Resources/Locale/ru-RU`).
- Правки файлов RMC-14 и SS14 сведены к минимуму и перечислены в `PATCHES.md`.
- `_RMC14` — код и ресурсы RMC-14, `_Wega` — ERP и взаимодействия из сборки Wega.

## Сборка

1. Клонируйте репозиторий.
2. Запустите `RUN_THIS.py`.
3. Соберите решение: `dotnet build --configuration Release`. Нужен .NET SDK 9.0.100 или новее.
4. Запуск для разработки: `runserver.sh` / `runserver.bat` и `runclient.sh` / `runclient.bat`.

[Подробная инструкция по сборке SS14.](https://docs.spacestation14.com/en/general-development/setup.html)

Готовые сборки: раздел [Releases](../../releases). Релиз `latest` обновляется автоматически при каждом пуше в `main`.

## Автообновление сервера на Windows

Скрипт `Tools/server-updater/update-server.ps1` сам скачивает новую серверную сборку из релиза `latest` и перезапускает службу. Инструкция: [Tools/server-updater/README.md](Tools/server-updater/README.md).

## Участие

Правила кода: [coding-standards.md](coding-standards.md). Руководство по PR и ченджлогу: [Pull Request and Changelog Guidelines](https://docs.spacestation14.com/en/general-development/codebase-info/pull-request-guidelines.html). Отправляя PR, вы подтверждаете, что у вас есть права на присланные материалы, и берёте на себя ответственность за претензии, связанные с ними.

## Лицензия

Собственные материалы Space Front (папки `_SpaceFront`, `Modifications`, серверные конфиги и документы) предоставляются для личного некоммерческого использования. Подробные условия на русском и английском: [LICENSE-SPACE-FRONT.txt](LICENSE-SPACE-FRONT.txt).

Код [Space Station 14](https://github.com/space-wizards/space-station-14) распространяется под [MIT](LICENSE-UPSTREAM.TXT), код RMC-14 — под [MIT](LICENSE.TXT).

Большинство ресурсов распространяется под [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/), если не указано иное. Лицензия и авторство каждого ресурса указаны в его `meta.json`.

Часть ресурсов лицензирована на некоммерческих условиях ([CC-BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) и похожих). Их нужно удалить при коммерческом использовании.

---

# Space Front — ERP Marines (English)

Space Front is a [Space Station 14](https://spacestation14.com/) build based on [RMC-14](https://github.com/RMC-14/RMC-14), running on [RobustToolbox](https://github.com/space-wizards/RobustToolbox). Its main game mode is "Wall to Wall": two "Almayer" ships and four marine squads fighting each other.

**18+. The build contains adult content (ERP). You must be 18 or older to play.**

## Features

- **SquadWar mode.** The only mode on the server: Alpha+Bravo vs Charlie+Delta. No xenos, survivors or recon. Each side has its own Almayer and its own "Aurora" shuttle. Squads are assigned automatically. A fog line divides the planet. The winner of the planet assaults the enemy Almayer. Endings are decided after a 1-minute hold (landing, enemy evacuation, team wiped out, draw).
- **Rules of play.** Humans only, maximum skills and full access, free vendors, cargo roles cost $1, each team has its own two radio channels, separate tactical maps, a 30-second ghost respawn window, the rules window at every login.
- **ERP and interactions (18+).** Interaction system, ERP items, ToysLeash and QueenCarry from the Wega build (`_Wega` folders). The server plays at MRP level. Entering the server confirms that the player is 18+ and agrees to ERP.
- **TTS.** Voice for chat, radio and announcements through the N/TTS HTTP API (ported from Space Stories), a voice picker in the character editor, an ARES voice for the round briefing.
- **Localization.** Full Russian translation of the interface.

## Building

1. Clone the repository.
2. Run `RUN_THIS.py`.
3. Build: `dotnet build --configuration Release` (.NET SDK 9.0.100 or newer).
4. For development use `runserver.sh` / `runserver.bat` and `runclient.sh` / `runclient.bat`.

Prebuilt packages are in [Releases](../../releases). The `latest` release is updated automatically on every push to `main`. The Windows server auto-updater is described in [Tools/server-updater/README.md](Tools/server-updater/README.md) (Russian).

## License

Own materials of Space Front (the `_SpaceFront` folders, `Modifications`, server configs and documents) are provided for personal, non-commercial use only. Full terms in Russian and English: [LICENSE-SPACE-FRONT.txt](LICENSE-SPACE-FRONT.txt).

Space Station 14 code is under [MIT](LICENSE-UPSTREAM.TXT), RMC-14 code is under [MIT](LICENSE.TXT). Most assets are under [CC-BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/) unless stated otherwise (see each asset's `meta.json`). Some assets are under non-commercial licenses such as [CC-BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/) and must be removed for commercial use.
