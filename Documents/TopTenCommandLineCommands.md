## Command Line Commands

1. Find out which process runs on a given port

    ```bash
    netstat -ano | findstr :<port-number>
    ```

2. Kill a process running on a given port

    ```bash
    taskkill /F /PID <process-id>
    ```

3. Install or update the latest ABP CLI

    ```bash
    dotnet tool install -g Volo.Abp.Cli || dotnet tool update -g Volo.Abp.Cli
    ```

4. Update EF tool

    ```bash
    dotnet ef --version
    dotnet tool update --global dotnet-ef
    ```

5. Add EF migrations to a project

    ```bash
    dotnet ef migrations add <MigrationName>
    ```

6. Remove EF migrations to a project

    ```bash
    dotnet ef migrations remove
    ```

7. Apply EF migrations to the database

    ```bash
    dotnet ef database update
    ```

8. Remove EF migrations already applied to the database

    ```bash
    dotnet ef database update <MigrationName-to-which-you-want-to-revert>
    dotnet ef migrations remove
    ```

9. Create a new .NET Solution

    ```bash
    dotnet new sln --name mysolution
    ```

10. Add a project to your solution

    ```bash
    dotnet sln add [yourProjectName]\[yourProjectName].csproj
    ```

11. Add a reference to a project from another project

    ```bash
    dotnet add reference ../../src/Volo.Abp.AspNetCore.Components.WebAssembly.BasicTheme/Volo.Abp.AspNetCore.Components.WebAssembly.BasicTheme.csproj
    ```

12. Add a Nuget package to your project

    ```bash
    dotnet add package [PackageName]
    ```

13. Create a new Blazor Webassembly app

    ```bash
    dotnet new blazorwasm -o [yourAppName]
    ```

14. Update Node.js to the latest version

    ```bash
    n latest
    ```

15. Generate a random secret key

    ```bash
    openssl rand -base64 32
    ```
