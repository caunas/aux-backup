# aux-backup

Pequeno script em Python para copiar pastas entre um dispositivo Android conectado via ADB e um computador Windows. O código reúne três operações: backup de arquivos do dispositivo, restauração de arquivos para o dispositivo e remoção de alguns aplicativos pré-configurados.

## Como funciona

O script chama o executável do Android Debug Bridge (ADB) usando `subprocess.run`:

- **Backup (`do_backup`)**: executa `adb pull` para cada pasta configurada no dispositivo e copia seu conteúdo para o diretório local de backup.
- **Restauração (`do_restore`)**: executa `adb push` para enviar ao dispositivo o conteúdo correspondente no diretório local.
- **Remoção de aplicativos (`do_debloat`)**: executa `adb shell pm uninstall -k --user 0 <pacote>` para cada pacote listado. A opção `-k` mantém os dados e o cache do aplicativo; `--user 0` aplica a remoção ao usuário principal do Android.

As pastas remotas estão listadas em `DIRECTORIES` e os pacotes de aplicativos em `do_debloat()`. O dispositivo é endereçado a partir de `/sdcard`.

## Configuração

Antes de usar, ajuste no início de `main.py` os caminhos para o seu ambiente:

```python
ADB = r"C:\platform-tools\adb.exe"
BACKUP_DIR = r"C:\Users\caunas\Desktop\backup"
ANDROID_ROOT = r"/sdcard"
```

Instale ou extraia o Android Platform Tools para que o executável exista no caminho configurado. Conecte o dispositivo, habilite a depuração USB e autorize o computador quando o Android solicitar. Verifique a conexão com `adb devices` antes de executar o script.

## Execução

Com Python e ADB disponíveis, execute no Windows:

```powershell
python main.py
```

**Atenção:** atualmente, a última linha de `main.py` chama `do_restore()` diretamente. Portanto, executar o arquivo inicia uma restauração e envia as pastas configuradas ao dispositivo. As funções de backup e remoção de aplicativos estão implementadas, mas não são selecionadas pela linha de comando; para usá-las, é necessário alterar a chamada final no código.

## Pastas e limitações atuais

O script tenta processar estas pastas sob `/sdcard`:

```text
/DCIM/Camera
/cu
/Secret
/Download
emu
/Music/eu
```

O diretório de backup é fixo e não há criação automática de pastas, seleção de dispositivo, interface de linha de comando ou validação prévia dos caminhos. Erros em cada pasta são impressos e o processamento continua; as chamadas ADB usam `check=True`, então uma falha em um comando gera uma exceção. Os caminhos de origem/destino da restauração são montados diretamente a partir dos valores da lista e podem precisar de ajustes para a estrutura de backup desejada.
