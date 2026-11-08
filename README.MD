<img src="https://github.com/PixelOS-CI/blog_assets/blob/main/banner.png?raw=True">

# Ready for adding your device into our list of official devices? [Click Me](https://blog.pixelos.net/docs/JoinTheTeam)

## API format

- `API/devices/<codename>.json` lists its maintainers by GitHub handle in `maintainers`.
- `API/team.json` holds everyone's details, keyed by `github`. Optional fields:
  - `core`: `true` for core team members.
  - `former`: `true` for people who have left the team (core members and maintainers alike).
  - `labels`: free-form titles shown on the website as-is, e.g. `["Core-Member"]` or `["PixelOS Co-founder"]`. `core` itself isn't displayed.

Maintainers aren't flagged in `team.json`: anyone listed in a device's `maintainers` is one, and the device files say which devices they maintain.
