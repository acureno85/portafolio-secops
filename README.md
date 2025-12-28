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
