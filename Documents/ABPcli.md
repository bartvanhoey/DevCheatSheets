## ABP CLI

## Install or upgrade the ABP CLI

Since ABP 8.2 the CLI is `Volo.Abp.Studio.Cli` (the old `Volo.Abp.Cli` is only needed for older solutions).

```bash
  dotnet tool install -g Volo.Abp.Studio.Cli || dotnet tool update -g Volo.Abp.Studio.Cli
```

## Upgrade the ABP CLI to a Release Candidate version

```bash
  dotnet tool update -g Volo.Abp.Studio.Cli --prerelease
```

Or pin a specific version:

```bash
  dotnet tool update -g Volo.Abp.Studio.Cli --version <version>
```
