# 📑 Reporte Fase 2: Despliegue de Agentes y Endurecimiento de Endpoints

**Fecha:** 28 de Diciembre, 2025
**Responsable:** Abraham Cureño
**Estado:** ✅ Completado (Conectividad Establecida)

## 🎯 Objetivo
Extender la capacidad de monitoreo del SIEM (Wazuh Manager) desde el entorno contenerizado hacia el sistema operativo anfitrión (**Parrot Security OS**).

## 🛠️ Desafíos Técnicos Resueltos (Troubleshooting)
1. **Conflicto de Versiones:** Se realizó un downgrade de v4.9 a v4.7.2 mediante APT Pinning para igualar la versión del Manager.
2. **Error DPKG 127:** Se reconstruyó la base de datos de dpkg eliminando scripts corruptos (prerm/postrm) que impedían la reinstalación.
3. **Identidad Duplicada:** Se purgó la base de datos del Manager para eliminar registros huérfanos del agente anterior.

## 📊 Resultados
* Agente **Active** verificado en CLI y Dashboard.
* Conexión encriptada TCP/1514 establecida.
