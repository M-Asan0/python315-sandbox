# Python 3.15 Sandbox

A sandbox repository for experimenting with new features in Python 3.15.

## Environment

* Python 3.15.0b3
* Docker (`python:3.15-rc-slim`)

## Features

* Lazy Import (PEP 810)
* Sentinel (PEP 661)
* frozendict (WIP)

## Run

Start the Docker container:

```bash
docker compose up -d
```

Enter the container:

```bash
docker compose exec python315 bash
```

Check the Python version:

```bash
python3 --version
```

## Related Article

* Qiita: *Python 3.15 Beta 3の新機能を検証してみた（lazy import・sentinel）*

