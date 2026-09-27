---
name: approval-gated-agent-teams
description: "Use for autonomous agent teams with human approval gates."
---

# Approval-Gated Agent Teams

Usá esta skill cuando una organización quiera un equipo de agentes que trabaje solo pero no pueda gastar, publicar, enviar mensajes o modificar sistemas externos sin aprobación humana explícita.

## Principio central

Separá el **control plane** de los perfiles de trabajo:

```text
cron/evento → tablero → perfil trabajador → artefacto/revisión
                                      ↓
                              broker de aprobación
                                      ↓
                         snapshot + hash + expiración
                                      ↓
                              revalidación en vivo
                                      ↓
                              executor autorizado
```

Un botón visible no es una autorización suficiente. La aprobación debe referirse a un snapshot concreto y la ejecución debe volver a comparar el estado vivo antes de producir el efecto externo.

## Procedimiento

1. **Definí límites antes de crear agentes.** Separá lectura, redacción, preparación pausada y ejecución. Marcá explícitamente qué acciones requieren aprobación.
2. **Creá un tablero persistente.** Usá estados como `triage`, `todo`, `running`, `review`, `blocked`, `done` y `archived`. Guardá dependencias, responsable, prioridad, evidencia y artefacto de salida.
3. **Creá perfiles livianos por rol.** Cada perfil debe tener un `SOUL.md` con personalidad, misión, fuente de verdad, formato de entregable, límites de autonomía y política de no-acción. No clones credenciales ni todas las skills si se pueden cargar por tarea.
4. **Mantené un broker de aprobación separado.** El gateway/canal de notificaciones es el único que habla con el dueño. Los trabajadores crean solicitudes; no convierten su propio razonamiento en autorización.
5. **Congelá el pedido.** Persistí ID, tipo, texto mostrado, payload canónico, hash, fecha de creación, expiración, actor y estado. El texto debe poner la plata y el riesgo primero.
6. **Procesá el callback sin ejecutar.** Una aprobación cambia el estado a `approved_pending_revalidation`; postergar, rechazar, vencer y repetir una decisión deben ser estados explícitos.
7. **Revalidá inmediatamente antes de ejecutar.** Leé de nuevo precio, stock, presupuesto, destino, permisos, versión del tema o cualquier dato mutable. Compará el payload canónico. Si hay diferencias, marcá `blocked_changed` y pedí una nueva aprobación.
8. **Ejecutá con un executor acotado.** Solo el executor conoce la operación externa. Debe aceptar únicamente solicitudes `ready_to_execute`, verificar autorización y registrar resultado real.
9. **Probá con una acción inocua.** Antes de conectar dinero o publicaciones: aprobación ficticia, snapshot idéntico aceptado y snapshot modificado rechazado. No declares listo el sistema sin las tres pruebas.
10. **Arrancá por fases.** Primero control plane y auditorías de solo lectura; después borradores; luego acciones reversibles; por último gasto/publicación. Para pauta, “campaña creada en pausa” y “campaña prendida” son capacidades distintas.

## Economía de contexto

- Despertá perfiles bajo demanda por horario/evento en vez de mantener una conversación permanente por agente.
- Pasá artefactos resumidos y contratos de handoff, no historiales completos.
- Cargá skills específicas por tarea.
- Guardá resultados en disco y hacé que el coordinador lea resúmenes.
- Usá un modelo barato para clasificación, extracción y chequeos rutinarios; reservá el más capaz para síntesis y decisiones.

## Entregables mínimos

- Diagrama del control plane.
- Inventario de roles y límites.
- Tablero con estados y dependencias.
- Broker persistente de aprobaciones.
- Registro de snapshots y decisiones.
- Prueba de aprobación, revalidación idéntica y bloqueo ante cambio.
- Política explícita de acciones bloqueadas.

## Errores frecuentes

- Crear botones primero y conectar la lógica después.
- Dejar que el callback ejecute directamente una API.
- Revalidar solo el presupuesto y olvidar stock, precio, destino o versión.
- Clonar perfiles completos y duplicar secretos/skills sin necesidad.
- Encender cron antes de probar el gate.
- Confundir “perfil creado” con “agente operativo”: falta definir prompt, herramientas, modelo, tarea, evidencia y verificador.
- Prometer un dashboard visual completo sin verificar qué parte del tablero expone realmente la instalación.

## Referencia

Para un patrón concreto de implementación con Hermes, snapshots, estados y pruebas, leer `references/hermes-approval-gate-pattern.md`.
