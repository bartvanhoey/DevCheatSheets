## PowerShell

### How to convert csv to JSON

```powershell
    Import-Csv .\items.csv | ConvertTo-Json | Set-Content items.json
```

### Count the numbers of lines in a C# codebase

```powershell
    (gci -include *.cs,*.xaml -recurse | select-string .).Count
```

### Export a table from (LocalDb)\MSSQLLocalDB to a CSV file

```powershell
 bcp <DatabaseName>.dbo.<TableName> out "C:\Temp\<TableName>.csv" -c -t "," -S "(localdb)\MSSQLLocalDB" -T
```
