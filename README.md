# 📊 Ocelotl Watch

**Security Operations Center & Continuous Monitoring**

[![License: MIT](https://img.shields.io/badge/License-MIT-FFB800.svg)](LICENSE)
[![Wazuh](https://img.shields.io/badge/Wazuh-4.9.2-0D0D0D.svg)](https://wazuh.com/)
[![Grafana](https://img.shields.io/badge/Grafana-11.x-FF6F00.svg)](https://grafana.com/)
[![Part of Ocelotl](https://img.shields.io/badge/Ocelotl-Watch-004D40.svg)](https://github.com/acureno85)

> *"Como el jaguar que vigila desde las sombras, Ocelotl Watch observa cada movimiento sin ser detectado."*

**[🎨 View Interactive Logo](docs/index.html)**

---

## 🎯 Overview

**Ocelotl Watch** es el ojo vigilante de la Ocelotl Security Platform - un SOC completo con monitoreo 24/7, detección de amenazas y análisis de comportamiento.

```
    OFENSIVO   →   DEFENSIVO   →   RESPUESTA
       🔐             📊              🛡️
   
     ATTACK         WATCH          STRIKE
  (El Atacante)  (El Vigilante)  (El Vengador)
                      ↑
                  YOU ARE HERE
```

---

## ✨ Features

### 📊 Security Monitoring
- **Wazuh SIEM** - Security Information & Event Management
- **Real-time Alerts** - Instant threat notifications
- **Log Aggregation** - Centralized logging
- **File Integrity** - FIM monitoring
- **Vulnerability Detection** - Continuous scanning

### 📈 Dashboards & Visualization
- **Grafana Integration** - Custom security dashboards
- **Kibana Analytics** - Deep log analysis
- **Executive Views** - Business-level metrics
- **Compliance Reports** - Automated reporting

### 🔍 Threat Detection
- **Behavioral Analysis** - Anomaly detection
- **IOC Matching** - Indicator correlation
- **MITRE ATT&CK** - Technique mapping
- **Threat Intelligence** - Feed integration

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/acureno85/portafolio-secops.git ocelotl-watch
cd ocelotl-watch

# Deploy stack
docker-compose up -d

# Verify services
docker-compose ps
```

**Access Points:**
- 🌐 Wazuh Dashboard: https://localhost:443
- 📊 Grafana: http://localhost:3000
- 🔍 Kibana: http://localhost:5601

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    OCELOTL WATCH                        │
├─────────────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐   │
│  │  Wazuh  │  │ Grafana │  │ Elastic │  │  Threat │   │
│  │  SIEM   │  │  Dash   │  │ Search  │  │  Intel  │   │
│  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘   │
│       │            │            │            │         │
│       └────────────┴────────────┴────────────┘         │
│                         │                               │
│              ┌──────────┴──────────┐                   │
│              │   Data Lake / SIEM  │                   │
│              └─────────────────────┘                   │
└─────────────────────────────────────────────────────────┘
```

---

## 🐆 Ocelotl Philosophy

> *"El jaguar observa en silencio. Conoce cada movimiento de su territorio."*

**Características del Jaguar Vigilante:**

| Rasgo | Aplicación en SOC |
|-------|-------------------|
| 👁️ **Visión nocturna** | Detección en la oscuridad |
| 🔇 **Silencio** | Monitoreo pasivo |
| 🎯 **Atención** | Alertas precisas |
| 🧠 **Memoria** | Correlación histórica |
| 🌍 **Territorio** | Cobertura completa |

---

## 🎨 Brand Colors

```css
/* Ocelotl Watch Color Palette */
--ocelotl-jade: #004D40;       /* Primary - Jungle jade */
--ocelotl-teal: #00695C;       /* Secondary - Deep teal */
--ocelotl-mint: #00FFB8;       /* Accent - Electric mint */
--ocelotl-cyan: #00FFFF;       /* Info - Cyan glow */
--ocelotl-gold: #FFB800;       /* Warning - Alert gold */
```

---

## 🐆 Part of Ocelotl Security Platform

| Product | Focus | Status |
|---------|-------|--------|
| **[Ocelotl Attack](https://github.com/acureno85/pentester-pro)** | Offensive Testing 🔐 | Active |
| **[Ocelotl Watch](https://github.com/acureno85/portafolio-secops)** | Security Monitoring 📊 | ← YOU ARE HERE |
| **[Ocelotl Strike](https://github.com/acureno85/soar-ai-platform)** | Incident Response 🛡️ | Active |

---

## 📄 License

MIT License - Free as the jaguar in the jungle

---

## 👤 Author

**Abraham Cureno** - *Ocelotl Warrior*

- 🐆 GitHub: [@acureno85](https://github.com/acureno85)
- 💼 LinkedIn: [Abraham Cureno](https://linkedin.com/in/abrahamcureno)

---

<div align="center">

**📊 Ocelotl Watch** - *Tlachialistli in Ocelotl*

*"La vigilancia del Jaguar"*

Made with ❤️ in Mexico 🇲🇽

</div>
