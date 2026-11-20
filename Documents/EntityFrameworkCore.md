## EF Core


### How to install EntityFramework tools

```bash
dotnet tool install --global dotnet-ef
```

### How to update EntityFramework tools

```bash
dotnet tool update --global dotnet-ef
```

### How to check version of EntityFrameworkCore

```bash
dotnet ef --version
```

### How to add a migration

```bash
dotnet ef migrations add <MigrationName>
```

### How to remove a migration not applied to database yet

```bash
dotnet ef migrations remove
```

### How to revert a migration ALREADY applied to database

```bash
dotnet ef database update <MigrationName-to-which-you-want-to-revert>
dotnet ef migrations remove
```

You need to run the remove command as many times as needed to go back to the MigrationName-to-which-you-want-to-revert

### How to apply migrations to database

```bash
dotnet ef database update
```

### How to get list of migrations

```bash
dotnet ef migrations list
```

### How to delete database

```bash
dotnet ef database drop
```
