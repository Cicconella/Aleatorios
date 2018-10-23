### Para fazer o download de arquivos do Google Drive 

1. Baixar um dos arquivos daqui: https://github.com/prasmussen/gdrive

2. Pelo terminal, ir na pasta que tem o arquivo baixado:

```bash
chmod +x gdrive
```
3. Para fazer o download de arquivo:

```
./gdrive download FILE_ID
```

4. Para fazer o download da pasta:

```
./gdrive download --recursive FOLDER_ID
```

Se o arquivo/pasta forem privados, pedirá a autenticação.
