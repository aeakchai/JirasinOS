# NAS Environment

## System

| Item | Value |
| --- | --- |
| Architecture | ARM64 (aarch64) |
| CPU | 4× Cortex-A76 + 4× Cortex-A55 |
| Operating system | Debian GNU/Linux 12 (Bookworm) |
| Docker | 29.4.3 |
| Docker Compose | v5.1.3 |

## Storage and Service Paths

| Item | Path or value |
| --- | --- |
| Shared folder root | `/volume1` |
| Source | `/volume1/JACK` |
| Destination | `/volume1/jirasin789` |
| Docker storage | `/volume1/@docker` |
| Application port | `8000` |

## Deployment Notes

- Build images directly on the NAS so that Docker produces ARM64-compatible images.
- Do not specify `platform` in `compose.yaml`.
- Set `PUID=1007` and `PGID=10` in `.env` to match the NAS user `jack` and group `admin`.
- Rebuild the image after changing `PUID` or `PGID`, because Compose supplies them as image build arguments.

## UGREEN NAS Deployment

1. Copy `.env.nas.example` to `.env`.
2. Build and start the application:

   ```sh
   docker compose build
   docker compose up -d
   ```

3. Confirm that the container uses the NAS identity and can read the source mount:

   ```sh
   docker exec jirasinos id
   docker exec jirasinos ls -la /data/JACK
   ```

   The first command should report `uid=1007(jack) gid=10(admin)`.
