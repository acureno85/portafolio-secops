## Detalles Técnicos - Fase 1

### Infraestructura Desplegada:
- **SIEM:** Wazuh (Indexer, Manager, Dashboard) para centralización de eventos.
- **IDS:** Suricata configurado en modo escucha para detección de intrusiones.
- **IA/Automation:** n8n y Agent Zero listos para orquestación.

### Troubleshooting de Infraestructura:
Durante el despliegue en Parrot OS, se identificó un error de compatibilidad con `docker-credential-desktop`.
- **Causa:** El motor Docker intentaba usar un gestor de credenciales de entornos Desktop en un entorno Server/CLI.
- **Resolución:** Limpieza manual de `~/.docker/config.json` eliminando la directiva `credsStore`. 
- **Evidencia del error:** Ver archivo `config.json.old`.
