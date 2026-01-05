# 🛡️ Portafolio SecOps: Automatización de Seguridad con Wazuh y n8n

## 📋 Descripción del Proyecto
Este proyecto implementa un entorno de **Security Orchestration, Automation, and Response (SOAR)** utilizando Docker. El objetivo es orquestar la seguridad defensiva mediante la integración de **Wazuh (SIEM)** y **n8n (Workflow Automation)**.

## 🚀 Hitos Alcanzados (Fase 1)
- **Despliegue de Infraestructura:** Implementación de Wazuh Manager, Indexer y Dashboard mediante Docker Compose.
- **Gestión de Identidad (IAM):** Recuperación y endurecimiento de credenciales API (RBAC) en entorno contenedorizado.
- **Automatización de Autenticación:** Desarrollo de un flujo en n8n para la gestión rotativa de Tokens JWT.
- **Conectividad Interna:** Configuración de networking seguro en Docker () para comunicación API Server-to-Server.

## 🛠️ Stack Tecnológico
- **OS:** Parrot Security OS
- **SIEM:** Wazuh 4.7.2
- **Orquestación:** n8n (Dockerized)
- **Contenerización:** Docker & Docker Compose
- **Scripting:** Python & Bash

## 📂 Estructura del Repositorio
- `docker-compose.yml`: Definición de la infraestructura como código (IaC).
- `workflows/`: Flujos de automatización de n8n (JSON).

## 🚀 Hitos Alcanzados (Fase 2)
- **Despliegue de Agente (Endpoint):** Instalación y configuración de Wazuh Agent en Parrot Security OS.
- **Troubleshooting Avanzado:** Resolución de conflictos de dependencias (DPKG), alineación de versiones (APT Pinning) y gestión de identidades duplicadas.
- **Conexión SIEM:** Establecimiento de canal seguro TCP/1514 entre el Host y el Manager Dockerizado.
- ![Despliegue de SIEM (Wazuh) exitoso](evidencias/fase2_agente_activo.png)
- **[📄 Ver Reporte Técnico Detallado de Fase 2](documentation/phase2/REPORT.md)**

## 🌐 Fase 3: Seguridad de Red (NIDS con Suricata)

Se ha implementado una capa de seguridad perimetral utilizando **Suricata** como Sistema de Detección de Intrusos en Red (NIDS).

### 🛡️ Arquitectura de Red
* **Motor NIDS:** Suricata instalado en el host (Parrot OS) escuchando en modo promiscuo sobre la interfaz de red principal.
* **Integración:** El Agente Wazuh lee el archivo `eve.json` de Suricata en tiempo real.
* **Correlación:** El Manager decodifica los eventos JSON y genera alertas de seguridad basadas en reglas de amenazas emergentes (ET Open Rules).

### 📸 Evidencia de Detección
Prueba de concepto realizada simulando una respuesta de comando malicioso (`uid=0(root)`). Suricata inspeccionó el paquete, detectó la firma y Wazuh generó la alerta de nivel alto.

![Alerta de Suricata en Wazuh](evidencias/fase3_suricata_alert.png)

### ⚙️ Configuración Realizada
1.  Instalación de Suricata y actualización de reglas (47,000+ firmas).
2.  Configuración de escucha en interfaz `wlp4s0`.
3.  Modificación de `ossec.conf` en el agente para ingestión de logs:
    ```xml
    <localfile>
      <log_format>json</log_format>
      <location>/var/log/suricata/eve.json</location>
    </localfile>
    ```

---
*Proyecto Finalizado - Infraestructura SecOps 100% Operativa.*

## 🧠 Fase 4: Inteligencia de Amenazas (VirusTotal Integration)

Se ha enriquecido la capacidad de detección integrando el SIEM con fuentes de inteligencia externas.

### 🔬 Capacidad Implementada
* **Integración API VirusTotal:** Automatización de consultas de hashes de archivos.
* **FIM Real-time:** Monitoreo en tiempo real de directorios críticos (`/Descargas`) para detección inmediata de "droppers".
* **Detección de Malware:** Identificación automática de binarios maliciosos basada en la reputación de 70+ motores antivirus.

### 📸 Evidencia de Detección
Prueba realizada descargando el archivo estandarizado EICAR. El sistema detectó la escritura en disco (FIM), extrajo el hash, consultó la API y generó una alerta de Nivel 12 (Crítico) en segundos.

![Alerta de Malware VirusTotal](evidencias/fase4_virustotal_detect.png)

### ⚙️ Configuración Realizada
1.  Obtención y configuración de API Key de VirusTotal en Wazuh Manager.
2.  Configuración de FIM en el Agente (Parrot OS) para monitoreo `realtime`:
    ```xml
    <directories realtime="yes" check_all="yes">/home/abraham/Descargas</directories>
    ```

---
*Próximos Pasos: Fase 5 - Respuesta Automatizada con IA (SOAR).*
