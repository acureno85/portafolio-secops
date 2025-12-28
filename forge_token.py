import jwt
import time

# --- ASEGÚRATE QUE ESTA CLAVE COINCIDA CON LA DEL PASO 1 ---
SECRET_KEY = "SecretKeyForAgentZero" 
# -----------------------------------------------------------

current_time = int(time.time())

payload = {
    "iss": "wazuh",
    "aud": "wazuh",
    # TRUCO: Decimos que el token se creó hace 10 minutos (600 seg)
    # Esto evita errores de sincronización de reloj entre Parrot y Docker
    "nbf": current_time - 600, 
    "iat": current_time - 600,
    "exp": current_time + 315360000, # 10 años
    "sub": "admin",
    "rbac_roles": ["administrator"]
}

try:
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    # En versiones nuevas de PyJWT, encode devuelve string, en viejas bytes.
    if isinstance(token, bytes):
        token = token.decode('utf-8')
        
    print("\n--- TOKEN NUEVO (COPIA ESTE) ---")
    print(token)
    print("--------------------------------\n")
except Exception as e:
    print(f"Error generando token: {e}")
