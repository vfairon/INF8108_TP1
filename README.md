# INF8108 - TP1

Lab exercise for the *Gestion et chasse aux menaces* course (see [Enoncé_lab1.pdf](Enoncé_lab1.pdf) for the assignment).

## Structure

- `USB_BAD/` - Proof-of-concept BadUSB payload: a keylogger (`payload.py`) that exfiltrates captured keystrokes to a local C2 server (`c2_server.py`) over HTTP, plus a helper (`get_cred.py`) to extract credential-like strings from captured logs.
- `malicious-file/` - Sample malicious USB/autorun artifacts used for the exercise (PDF analysis tools, autorun payloads, exported samples).

This is coursework for educational/defensive security purposes only.

## Setup (UV)

From `USB_BAD/`, install dependencies with [uv](https://docs.astral.sh/uv/):

```bash
cd USB_BAD
uv sync
```

## Running

1. Start the C2 server (listens on `127.0.0.1:8080`, saves uploads to `USB_BAD/received/`):

   ```bash
   uv run c2_server.py
   ```

2. In another terminal, run the payload (captures keystrokes and POSTs them to the C2 server):

   ```bash
   uv run payload.py
   ```

3. To extract email-like credentials from a captured log:

   ```bash
   uv run get_cred.py received/log.txt
   ```
