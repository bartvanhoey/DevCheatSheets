## Azurite emulator for local Azure Storage development

### Install Azurite

```bash
   npm install -g azurite
```

### Run Azurite from the command line

```bash
  azurite --silent --location c:\azurite --debug c:\azurite\debug.log
```

### Azurite ConnectionString

```bash
DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;
```
